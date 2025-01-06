from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

class ToggleSwitch(QPushButton):
    def __init__(self):
        super().__init__()
        self.setCheckable(True)  
        self.setIconSize(QSize(30, 30))  
        self.setFixedSize(100, 40)
        self.update_style() 
        
        self.toggled.connect(self.update_style)

    def update_style(self):
        if self.isChecked():
            self.setIcon(QIcon("/Users/leeyilin/playground/pyside6/images/2.png"))
            self.setStyleSheet(
                "QPushButton {"
                "    background-color: #555555; "
                "    border: 2px solid #cccccc; "
                "    border-radius: 20px; "
                "    padding-left: 15px; "  
                "    padding-right: 4px; "  
                "    text-align: right; "
                "    color: #ffffff; "
                "}"
            )
        else:
            self.setIcon(QIcon("/Users/leeyilin/playground/pyside6/images/1.png"))
            self.setStyleSheet(
                "QPushButton {"
                "    background-color: #f5f5f5; "
                "    border: 2px solid #cccccc; "
                "    border-radius: 20px; "
                "    padding-left: 4px; "  
                "    padding-right: 15px; " 
                "    text-align: left; "
                "    color: #333333; "
                "}"
            )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Toggle Switch")
        self.setFixedSize(200, 100)
        
        toggle_switch = ToggleSwitch()
        toggle_switch.setParent(self)
        toggle_switch.setGeometry(40, 30, 120, 40)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
