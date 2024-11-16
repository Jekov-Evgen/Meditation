from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Медитация")
        self.setFixedSize(350, 250)
        self.setWindowIcon(QIcon(r"Image\icon.webp"))
        
        self.error = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        greet = QLabel(text="Введите сколько времени вам нужно для медитации")
        self.enter_time = QLineEdit()
        start_meditation = QPushButton(text="Начать медитацию")
        
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
            self.error = QMessageBox()
            self.error.setWindowTitle("Ошибка")
            self.error.setText("Вводить можно только числа")
            
        