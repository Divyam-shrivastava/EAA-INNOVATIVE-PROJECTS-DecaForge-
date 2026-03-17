import serial
import serial.tools.list_ports
import speech_recognition as sr
import threading
import time

# --- Find ESP32 Port Automatically ---
def find_esp32_port():
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if any(k in p.description for k in ["CP210", "CH340", "USB Serial", "UART"]):
            return p.device
    return None

ESP32_PORT = find_esp32_port()
if ESP32_PORT is None:
    ESP32_PORT = "COM8"  # <-- change this manually if auto-detect fails
    print(f"ESP32 not found automatically. Trying {ESP32_PORT}")
else:
    print(f"ESP32 found on {ESP32_PORT}")

try:
    esp32 = serial.Serial(ESP32_PORT, baudrate=115200, timeout=1)
    print("Serial connection established")
except serial.SerialException as e:
    print(f"Error: Could not connect to {ESP32_PORT}. {e}")
    exit()

# --- Voice Recognition ---
listening = True

def listen_voice():
    global listening
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Voice assistant ready. Say 'light on' or 'light off'")
    except Exception as e:
        print(f"Microphone not available: {e}")
        return
    
    while listening:
        try:
            with sr.Microphone() as source:
                audio = r.listen(source, timeout=2)
            try:
                command = r.recognize_google(audio).lower()
                print("Listening...")
                print(f"Voice: {command}")
                if "light on" in command:
                    esp32.write(b'L1')
                    print("Sent: L1 (Light ON)")
                elif "light off" in command:
                    esp32.write(b'L0')
                    print("Sent: L0 (Light OFF)")
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"API Error: {e}")
        except sr.RequestError:
            pass
        except Exception as e:
            print(f"Error: {e}")

print("Voice assistant running...")
print("Say 'light on' or 'light off'")
print("Press Ctrl+C to quit.\n")

# Start voice recognition in background thread
voice_thread = threading.Thread(target=listen_voice, daemon=True)
voice_thread.start()

try:
    while listening:
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nExiting...")
    listening = False
    esp32.close()
    print("Serial connection closed.")