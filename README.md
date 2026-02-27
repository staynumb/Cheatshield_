# Cheatshield_

AI-Based Online Cheating Prevention System in Online Exams
<img width="1211" height="668" alt="417264134-e7b86718-0883-40bd-b92b-0097c7c9784a" src="https://github.com/user-attachments/assets/c568fe52-e451-41a4-b6c4-af1bf8ecade9" />
📝 Overview

The AI-Based Online Cheating Prevention System is an intelligent proctoring solution designed to maintain fairness and integrity during online examinations. With the rise of remote learning, ensuring secure virtual assessments has become a critical challenge. This system leverages advanced artificial intelligence techniques to monitor candidates in real time, detect cheating behaviors, and enforce exam rules, reducing the need for human invigilators while fostering trust in digital education.

The system integrates multiple detection modules—object detection (YOLOv5), face detection (MTCNN), and audio detection (YAMNet)—alongside system control mechanisms to create a comprehensive invigilation framework. It monitors for prohibited items (e.g., mobile phones, books), ensures the candidate’s presence, detects suspicious sounds (e.g., speech, whispering), and enforces rules like fullscreen mode and shortcut restrictions. A user-friendly interface built with PyQt5 displays live webcam feeds, violation counts, and warnings, empowering proctors to oversee exams effectively.

🚀 Features
Object Detection: Identifies prohibited items like mobile phones and books using YOLOv5 with a custom-trained model (best.pt).
Face Detection: Ensures the candidate’s presence and flags multiple faces using MTCNN, preventing impersonation.
Audio Detection: Detects suspicious sounds like speech or whispering using YAMNet, with a lowered threshold for improved sensitivity.
System Control: Enforces exam rules using QWebEngineView, maintaining fullscreen mode and disabling shortcuts (e.g., Alt+Tab, F11).
Real-Time Monitoring: Displays live webcam feeds, violation counts, and warnings in a PyQt5-based interface.
Violation Handling: Implements a 15-second cooldown between violations and ends the test after 10 violations.
Resource Optimization: Reduces webcam update rate to 10 FPS, lowers resolution to 160x120, and adjusts detection frequencies for smooth performance.
Scalability: Designed to handle multiple candidates, making it suitable for large-scale institutional assessments.
Transparency: Logs violations with timestamps for post-exam review and dispute resolution.

🛠️ Technologies Used
Python 3.x: Core programming language for the system.
YOLOv5: For object detection to identify prohibited items like mobile phones and books.
MTCNN: For face detection to ensure candidate presence and prevent impersonation.
YAMNet: For audio detection to flag suspicious sounds like speech or whispering.
PyQt5: For building the user interface, displaying webcam feeds, and showing warnings.
QWebEngineView: For enforcing exam rules like fullscreen mode and shortcut disabling.
TensorFlow Hub: For loading pre-trained YAMNet model for audio detection.
OpenCV: For webcam frame processing and display.
NumPy: For numerical computations and array manipulations.
SoundDevice: For audio capture and processing.

📂 Project Structure
AI-Based-Online-Cheating-Prevention-System

│
├── models/
│   ├──best.pt               # Custom-trained YOLOv5 model for object detection
├── modules/                 # Source code directory
│   ├── object_detection.py  # Module for YOLOv5 object detection
│   ├── face_detection.py    # Module for MTCNN face detection
│   ├── audio_detection.py   # Module for YAMNet audio detection
│   ├── system_control.py    # Module for enforcing exam rules (fullscreen, shortcuts)
├── index.html               # Frontend UI that appears on the external website
├── styles.css               # Stylesheet for the UI
├── main.py                  # Main script to run the proctoring system
├── requirements.txt         # List of required Python packages
└── README.md                # Project documentation    
