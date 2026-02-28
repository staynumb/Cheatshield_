import sys
import os

# --- TECHNICAL MITIGATIONS (V2) ---
# Disable sandbox for stability
os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"

# Try Desktop OpenGL instead of Software to fix the blank window issue
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
QApplication.setAttribute(Qt.AA_UseDesktopOpenGL)
# Also enable context sharing which helps with multiple WebEngine windows
QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

print("Mitigations applied (V2).", flush=True)

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class MinimalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cheatshield Minimal Test V2")
        self.setGeometry(100, 100, 800, 600)
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        
        self.label = QLabel("Minimal UI V2 - Checking if text and web render correctly.")
        self.label.setStyleSheet("font-size: 20px; color: blue;")
        layout.addWidget(self.label)
        
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)
        # Using a reliable external site for this test
        self.web_view.load(QUrl("https://www.google.com"))
        
        print("UI Assembly complete.", flush=True)

if __name__ == "__main__":
    print("Starting QApplication...", flush=True)
    app = QApplication(sys.argv)
    print("Creating MinimalWindow...", flush=True)
    window = MinimalWindow()
    window.show()
    print("Entering event loop...", flush=True)
    sys.exit(app.exec_())
