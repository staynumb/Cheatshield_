# cheatshield
# AI-Based Online Cheating Prevention System in Online Exams

![image](https://github.com/user-attachments/assets/e7b86718-0883-40bd-b92b-0097c7c9784a)  
*Ensuring academic integrity in online exams through AI-powered proctoring.*

---

## 📝 Overview

The **AI-Based Online Cheating Prevention System** is an intelligent proctoring solution designed to maintain fairness and integrity during online examinations. With the rise of remote learning, ensuring secure virtual assessments has become a critical challenge. This system leverages advanced artificial intelligence techniques to monitor candidates in real time, detect cheating behaviors, and enforce exam rules, reducing the need for human invigilators while fostering trust in digital education.

The system integrates multiple detection modules—**object detection (YOLOv5)**, **face detection (MTCNN)**, and **audio detection (YAMNet)**—alongside system control mechanisms to create a comprehensive invigilation framework. It monitors for prohibited items (e.g., mobile phones, books), ensures the candidate’s presence, detects suspicious sounds (e.g., speech, whispering), and enforces rules like fullscreen mode and shortcut restrictions. A user-friendly interface built with **PyQt5** displays live webcam feeds, violation counts, and warnings, empowering proctors to oversee exams effectively.

---

## 🚀 Features

- **Object Detection**: Identifies prohibited items like mobile phones, books, and laptops using YOLOv5 with a custom-trained model (`best.pt`).
- **Face Detection**: Ensures the candidate’s presence and flags multiple faces using MTCNN, preventing impersonation.
- **Audio Detection**: Detects suspicious sounds like speech or whispering using YAMNet, with a lowered threshold for improved sensitivity.
- **System Control**: Enforces exam rules using `QWebEngineView`, maintaining fullscreen mode and disabling shortcuts (e.g., Alt+Tab, F11).
- **Real-Time Monitoring**: Displays live webcam feeds, violation counts, and warnings in a PyQt5-based interface.
- **Violation Handling**: Implements a 15-second cooldown between violations and ends the test after 10 violations.
- **Resource Optimization**: Reduces webcam update rate to 10 FPS, lowers resolution to 160x120, and adjusts detection frequencies for smooth performance.
- **Scalability**: Designed to handle multiple candidates, making it suitable for large-scale institutional assessments.
- **Transparency**: Logs violations with timestamps for post-exam review and dispute resolution.

---

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language for the system.
- **YOLOv5**: For object detection to identify prohibited items like mobile phones, books, and laptops.
- **MTCNN**: For face detection to ensure candidate presence and prevent impersonation.
- **YAMNet**: For audio detection to flag suspicious sounds like speech or whispering.
- **PyQt5**: For building the user interface, displaying webcam feeds, and showing warnings.
- **QWebEngineView**: For enforcing exam rules like fullscreen mode and shortcut disabling.
- **TensorFlow Hub**: For loading pre-trained YAMNet model for audio detection.
- **OpenCV**: For webcam frame processing and display.
- **NumPy**: For numerical computations and array manipulations.
- **SoundDevice**: For audio capture and processing.

---

## 📂 Project Structure
AI-Based-Online-Cheating-Prevention-System 
```
│
├── models/
│   └── best.pt              # Custom-trained YOLOv5 model for object detection
├── modules/                 # Detection modules package
│   ├── __init__.py          # Package initializer
│   ├── object_detection.py  # YOLOv5 object detection module
│   ├── face_detection.py    # MTCNN face detection module
│   ├── audio_detection.py   # YAMNet audio detection module
│   └── system_control.py    # Exam rule enforcement (fullscreen, shortcuts)
├── index.html               # Local exam page (served via Python http.server)
├── styles.css               # Stylesheet for the exam page
├── main.py                  # Main script to run the proctoring system
├── requirements.txt         # List of required Python packages
└── README.md                # Project documentation
```

---

## ⚙️ Installation and Setup

### Prerequisites
- Python 3.11 (Recommended)
- [Microsoft Visual C++ Redistributable (2015-2022)](https://aka.ms/vs/17/release/vc_redist.x64.exe) - **Required for PyTorch on Windows**
- A webcam and microphone
- Internet connection (for initial package installation)

### Steps to run this project
1. **Clone the Repository**
   ```bash
   git clone https://github.com/staynumb/Cheatshield_.git
   cd Cheatshield_
   ```
2. **Create a Virtual Environment (Optional but Recommended)**
   ```
   python -m venv venv
   ```
   ***For Windows***
   ```
   venv\Scripts\activate
   ```
   ***For Mac/Linux***
   ```
   source venv/bin/activate
   ```
3. **Install Dependencies**
   First, install the CPU-optimized version of PyTorch to ensure compatibility:
   ```powershell
   pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cpu
   ```
   Then install the remaining requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. **Start the Local Exam Server** (in a separate terminal)
   ```
   python -m http.server 8000
   ```
   This serves `index.html` at `http://localhost:8000/`.

5. **Run the Proctoring System** (in another terminal)
   ```
   python main.py
   ```
   The monitoring window and exam web view will launch automatically.

> **Note:** Both the local server and the proctoring system must be running simultaneously. The proctoring system connects to `http://localhost:8000/` to load the exam page.

  ## 🖥️ Usage

1. **Start Local Server**: Run `python -m http.server 8000` to serve the exam page locally.
2. **Launch the Application**: Run `python main.py` to start the proctoring system.  
3. **Exam Setup**: The system loads the local exam page (`http://localhost:8000/`) in a `QWebEngineView` window, enforcing fullscreen mode and disabling shortcuts.  
4. **Monitoring**: The PyQt5 interface displays the webcam feed, violation count, and warnings in real-time.  
5. **Violation Handling**:  
   - Issues warnings for detected violations (e.g., mobile phone detected, multiple faces, speech).  
   - A **15-second cooldown** prevents rapid triggers.  
   - The test **ends after 10 violations**.  
6. **End Test**:  
   - The test can be ended **manually via a password-protected dialog** or **automatically after 10 violations**.  

---

## 📊 Performance and Outcomes

- **Enhanced Supervision**: MTCNN ensures continuous face detection with high reliability, flagging impersonation attempts.  
- **Precise Object Detection**: YOLOv5 detects prohibited items accurately with confidence thresholds:  
  - **Mobile Phones** → `0.4`  
  - **Books/Laptops** → `0.2`  
- **Effective Audio Detection**: YAMNet detects speech with a **0.3 threshold**, optimized with a **5-second detection interval**.  
- **System Control**: `QWebEngineView` enforces exam rules, preventing unauthorized access.  
- **Resource Efficiency**: Optimized to run smoothly even during YouTube playback with:  
  - **10 FPS webcam update rate**  
  - **160x120 resolution**  
  - **Reduced detection frequencies**  
- **Scalability**: Can handle **multiple candidates**, making it suitable for large-scale exams.  

---

## 🔍 Challenges and Solutions

- **High Resource Usage**  
  - **Solution**: Reduced webcam FPS (`10`), lowered resolution (`160x120`), and optimized detection frequencies (`every 8th frame` for object/face detection, `every 5 seconds` for audio).  

- **Misclassification in Object Detection**  
  - **Solution**: Improved by setting confidence thresholds (`0.4` for mobile phones, `0.2` for books and laptops) and using a **custom-trained YOLOv5 model**.  

- **White Box Issue in UI**  
  - **Solution**: Made the warning display (`QWebEngineView`) **transparent** in the PyQt5 interface.  

- **Noisy Audio Environments**  
  - **Solution**: Lowered **YAMNet speech detection threshold** (`0.3`) and added **debug prints** to verify audio capture.  

---

## 🌟 Future Enhancements

- **Lighter Models**:  
  - Replace YOLOv5 with a **smaller variant (`yolov5s`)**.  
  - Use a **lighter face detection model** instead of MTCNN to reduce resource usage.  

- **Advanced Logging**:  
  - Implement **detailed logging** of all detections (objects, faces, audio) for **post-exam analysis**.  

- **Eye-Gaze Tracking**:  
  - Detect off-screen glances **more accurately**.  

- **Keystroke Dynamics**:  
  - Monitor **typing patterns** to detect unusual behavior.  

- **Noise Filtering**:  
  - Enhance audio detection with **advanced noise filtering** for better performance in noisy environments.  

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are **welcome!** To contribute:  

1. **Fork** the repository.  
2. **Create a new branch** for your changes.  
3. **Submit a pull request** with appropriate documentation.  

Ensure your code follows the **project’s coding style**.  

---

## 📧 Contact

For questions, suggestions, or collaboration, feel free to reach out:  

- **Email**: sathana.ec22@bitsathy.ac.in 
- **GitHub Issues**: Open an **issue** in this repository.  

---

## 🙏 Acknowledgments

- [YOLOv5](https://github.com/ultralytics/yolov5) → Object detection.  
- [MTCNN](https://github.com/ipazc/mtcnn) → Face detection.  
- [YAMNet](https://tfhub.dev/google/yamnet/1) → Audio detection.  
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/) → UI development.  
- **The open-source community** for invaluable resources and tools.  

---

*Built with ❤️ to ensure fairness in online education.*  

