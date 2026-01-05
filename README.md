# Smart Packaging & Inspection System

A comprehensive Industrial IoT solution integrating Computer Vision, PLC Automation, and Mobile Monitoring to detect packaging defects in real-time.

![Project Status](https://img.shields.io/badge/Status-Under_Development-yellow)
![Tech Stack](https://img.shields.io/badge/Stack-Python_|_Flutter_|_PLC-blue)

## 📖 Project Overview
This project aims to automate quality control in packaging lines. By connecting an edge computing device (Raspberry Pi) with industrial hardware (PLC) and a mobile dashboard, the system ensures defective products are detected and rejected automatically.

### Key Features
* **Automated Inspection:** Uses Computer Vision to detect printing or packaging errors.
* **Industrial Control:** Integrates with PLC (Ladder Logic) to control conveyors and rejection mechanisms.
* **Remote Monitoring:** A Flutter-based mobile app for real-time alerts and production stats.
* **Data Logging:** A backend server to store defect history and performance metrics.

---

## 🏗️ System Architecture

The repository is organized into four main modules representing the different layers of the system:

### 1. 🧠 Raspberry Pi (`/rpi`)
* **Role:** The "Edge" processing unit.
* **Function:** Connects to the camera to capture images, runs the computer vision algorithms, and sends signals to the PLC.
* **Tech:** Python, OpenCV, GPIO Control.

### 2. 📱 Mobile Application (`/flutter`)
* **Role:** The User Interface (UI).
* **Function:** Allows factory managers to view live status, receive error alerts, and stop the machine remotely.
* **Tech:** Flutter (Dart), Provider/Riverpod.

### 3. ⚙️ Industrial Control (`/plc`)
* **Role:** Hardware Actuation.
* **Function:** Contains the Ladder Logic responsible for driving motors, reading sensors, and executing the physical rejection of bad packages.
* **Tech:** [Insert PLC Brand, e.g., Siemens/Delta], Ladder Logic.

### 4. ☁️ Backend API (`/backend`)
* **Role:** Data Management.
* **Function:** Handles communication between the mobile app and the hardware, and stores production data in the database.
* **Tech:** Python (FastAPI/Flask) or Node.js.

---

## 🚀 Getting Started

### Prerequisites
* **Hardware:** Raspberry Pi 4, Camera Module, PLC Unit.
* **Software:** Python 3.9+, Flutter SDK, PLC Programming Software.

### Installation
*Note: Specific instructions for each module are located in their respective folders.*

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/REPO_NAME.git](https://github.com/YOUR_USERNAME/REPO_NAME.git)
    ```

2.  **Set up the Raspberry Pi:**
    Navigate to `/rpi` and install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
---
*Created for [Mansura University] - 2026*
