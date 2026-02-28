import sys
import os
import traceback

def diagnostic():
    print("--- DIAGNOSTIC START ---", flush=True)
    
    try:
        print("1. Testing basic imports...", end=" ", flush=True)
        import cv2
        import numpy as np
        import torch
        print("OK", flush=True)
    except Exception:
        print("\nFAILED at basic imports:")
        traceback.print_exc()
        return

    try:
        print("2. Testing PyQt5 imports...", end=" ", flush=True)
        from PyQt5.QtWidgets import QApplication
        from PyQt5.QtWebEngineWidgets import QWebEngineView
        print("OK", flush=True)
    except Exception:
        print("\nFAILED at PyQt5 imports:")
        traceback.print_exc()
        return

    try:
        print("3. Testing Local Module imports...", end=" ", flush=True)
        from modules.object_detection import ObjectDetector
        from modules.face_detection import FaceDetector
        from modules.audio_detection import AudioDetector
        from modules.system_control import SystemController
        print("OK", flush=True)
    except Exception:
        print("\nFAILED at local module imports:")
        traceback.print_exc()
        return

    try:
        print("4. Initializing QApplication...", end=" ", flush=True)
        app = QApplication(sys.argv)
        print("OK", flush=True)
    except Exception:
        print("\nFAILED at QApplication init:")
        traceback.print_exc()
        return

    try:
        print("5. Initializing ObjectDetector...", end=" ", flush=True)
        obj_detector = ObjectDetector()
        print("OK", flush=True)
    except Exception:
        print("\nFAILED at ObjectDetector init:")
        traceback.print_exc()
        return

    try:
        print("6. Initializing FaceDetector...", end=" ", flush=True)
        face_detector = FaceDetector()
        print("OK", flush=True)
    except Exception:
        print("\nFAILED at FaceDetector init:")
        traceback.print_exc()
        return

    try:
        print("7. Initializing AudioDetector...", end=" ", flush=True)
        audio_detector = AudioDetector()
        print("OK", flush=True)
    except Exception:
        print("\nFAILED at AudioDetector init:")
        traceback.print_exc()
        return

    try:
        print("8. Initializing SystemController...", end=" ", flush=True)
        sys_controller = SystemController()
        print("OK", flush=True)
    except Exception:
        print("\nFAILED at SystemController init:")
        traceback.print_exc()
        return

    print("\n--- ALL CORE COMPONENTS INITIALIZED SUCCESSFULLY ---")
    print("If you see this, the issue is likely in the MonitoringWindow UI assembly or event loop.")

if __name__ == "__main__":
    diagnostic()
