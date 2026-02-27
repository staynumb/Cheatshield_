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
⚙️ Installation and Setup
Prerequisites
Python 3.8 or higher
A webcam and microphone
Internet connection (for initial package installation)
Steps to run this project
Clone the Repository
git clone https://github.com/vishal017/cheatshield.git
cd AI-Based-Online-Cheating-Prevention-System
Create a Virtual Environment (Optional but Recommended)
python -m venv venv
For Windows
venv\Scripts\activate
For Mac
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Run the project
python main.py
🖥️ Usage
Launch the Application: Run main.py to start the proctoring system.
Exam Setup: The system loads the exam website in a QWebEngineView window, enforcing fullscreen mode and disabling shortcuts.
Monitoring: The PyQt5 interface displays the webcam feed, violation count, and warnings in real-time.
Violation Handling:
Issues warnings for detected violations (e.g., mobile phone detected, multiple faces, speech).
A 15-second cooldown prevents rapid triggers.
The test ends after 10 violations.
End Test:
The test can be ended manually via a password-protected dialog or automatically after 10 violations.
Violations are logged in the logs/ directory with timestamps.
📊 Performance and Outcomes
Enhanced Supervision: MTCNN ensures continuous face detection with high reliability, flagging impersonation attempts.
Precise Object Detection: YOLOv5 detects prohibited items accurately with confidence thresholds:
Mobile Phones → 0.4
Books → 0.2
Effective Audio Detection: YAMNet detects speech with a 0.3 threshold, optimized with a 5-second detection interval.
System Control: QWebEngineView enforces exam rules, preventing unauthorized access.
Resource Efficiency: Optimized to run smoothly even during YouTube playback with:
10 FPS webcam update rate
160x120 resolution
Reduced detection frequencies
Scalability: Can handle multiple candidates, making it suitable for large-scale exams.
🔍 Challenges and Solutions
High Resource Usage

Solution: Reduced webcam FPS (10), lowered resolution (160x120), and optimized detection frequencies (every 8th frame for object/face detection, every 5 seconds for audio).
Misclassification in Object Detection

Solution: Improved by setting confidence thresholds (0.4 for mobile phones, 0.2 for books) and using a custom-trained YOLOv5 model.
White Box Issue in UI

Solution: Made the warning display (QWebEngineView) transparent in the PyQt5 interface.
Noisy Audio Environments

Solution: Lowered YAMNet speech detection threshold (0.3) and added debug prints to verify audio capture.
🌟 Future Enhancements
Lighter Models:

Replace YOLOv5 with a smaller variant (yolov5s).
Use a lighter face detection model instead of MTCNN to reduce resource usage.
Advanced Logging:

Implement detailed logging of all detections (objects, faces, audio) for post-exam analysis.
Eye-Gaze Tracking:

Detect off-screen glances more accurately.
Keystroke Dynamics:

Monitor typing patterns to detect unusual behavior.
Noise Filtering:

Enhance audio detection with advanced noise filtering for better performance in noisy environments.
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch for your changes.
Submit a pull request with appropriate documentation.
Ensure your code follows the project’s coding style.

📧 Contact
For questions, suggestions, or collaboration, feel free to reach out:

Email: vsm52125@gmail.com
GitHub Issues: Open an issue in this repository.
🙏 Acknowledgments
YOLOv5 → Object detection.
MTCNN → Face detection.
YAMNet → Audio detection.
PyQt5 → UI development.
The open-source community for invaluable resources and tools.
Built with ❤️ to ensure fairness in online education.
