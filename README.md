# DecaForge: IoT Smart Room Controller 🏠💡

Welcome to the **DecaForge** project! Developed by the EAA-INNOVATIVE-PROJECTS team, this repository contains the source code, hardware configurations, and resources for an advanced, fully integrated Smart Home platform. 

## 📖 Overview

DecaForge transforms a standard room into an intelligent environment. By combining an ESP32 microcontroller with a Python-based computer vision and voice-recognition script, this system provides hands-free control, automated environmental adaptations, and real-time telemetry via both local OLEDs and a live Web Dashboard.

## ✨ Key Features

* 🎙️ **Voice Assistant (New!)**: Control room lighting using natural speech (e.g., *"light on"*, *"dim to fifty"*). 
* ✌️ **Gesture Control**: Uses a webcam and MediaPipe hand-tracking to dynamically adjust LED brightness by pinching or spreading your fingers.
* 🌡️ **Automated Environment**: Monitors temperature and automatically scales fan speed (PWM) to maintain comfort. Also tracks humidity and air quality (MQ-135).
* 🚪 **Smart Entry & Tracking**: Uses a Hall effect sensor to monitor door state and dual IR sensors for a bidirectional "People Counter". 
* ⚡ **Auto-Relay Power**: Intelligently toggles room power/appliances based on room occupancy or door state.
* 🌐 **Real-Time Dashboards**: Features a local dual-OLED setup and a live, responsive Web Dashboard powered by Server-Sent Events (SSE).

## 🛠️ Tech Stack & Hardware

**Software:**
* **Python:** OpenCV, MediaPipe (Hand Landmarker), SpeechRecognition, PySerial
* **C++ (Arduino IDE):** ESP32 WiFi Server, Adafruit GFX/SSD1306, DHT Sensor Library

**Hardware:**
* ESP32 Development Board
* DHT11 (Temp/Humidity) & MQ-135 (Air Quality Gas Sensor)
* 2x IR Sensors & 1x Hall Effect Sensor
* 5V Relay Module
* 2x 0.96" OLED Displays (I2C)

## 🚀 Getting Started

### 1. Hardware Setup (ESP32)
1. Clone the repository:
   ```bash
   git clone [https://github.com/EAA-INNOVATIVE-PROJECTS/DecaForge.git](https://github.com/EAA-INNOVATIVE-PROJECTS/DecaForge.git)
