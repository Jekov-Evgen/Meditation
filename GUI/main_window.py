from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMessageBox
from GUI.style import CONST_MAIN_WINDOW, CONST_MASSAGE_BOX
import pygame

def result():
    pygame.mixer.music.stop()
    res = QMessageBox()
    res.setWindowIcon(QIcon(r"Image\icon.webp"))
    res.setWindowTitle("Время вышло")
    res.setStyleSheet(CONST_MASSAGE_BOX)
    res.setText("Вы постарались")
    res.exec()

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Медитация")
        self.setStyleSheet(CONST_MAIN_WINDOW)
        self.setFixedSize(800, 600)
        self.setWindowIcon(QIcon(r"Image\icon.webp"))
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        greet = QLabel(text="Введите сколько времени вам нужно для медитации(время в секундах)")
        self.enter_time = QLineEdit()
        
        start_meditation = QPushButton(text="Начать медитацию")
        start_meditation.clicked.connect(self.start_med)
        
        control_UI.addWidget(greet, alignment=Qt.AlignmentFlag.AlignHCenter)
        control_UI.addWidget(self.enter_time)
        control_UI.addWidget(start_meditation)
        
        central_widget.setLayout(control_UI)
        self.setCentralWidget(central_widget)       
        self.show()
        
    def start_med(self):
        try:
            time = int(self.enter_time.text())
        except:
            error = QMessageBox()
            error.setStyleSheet(CONST_MASSAGE_BOX)
            error.setWindowIcon(QIcon(r"Image\icon.webp"))
            error.setWindowTitle("Ошибка")
            error.setText("Вводить можно только числа")
            error.exec()
        
        pygame.mixer.init() 
        pygame.mixer.music.load(r"Music\Earth Essence - Winds of Meditation.mp3")
        pygame.mixer.music.play(-1)
        
        timing = QTimer()
        timing.singleShot(time * 1000, result)
            
        