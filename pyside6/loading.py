from PySide6.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.group_box = QGroupBox("Group Box Title", self)

        layout = QVBoxLayout()

        self.image_label = QLabel(self)
        self.pixmap = QPixmap("pyside6/images/1.png")  # Replace with your image path
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.loading_label = QLabel("Loading...", self)
        self.loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.image_label)
        layout.addWidget(self.loading_label)

        self.group_box.setLayout(layout)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.group_box)

        self.setLayout(main_layout)

        self.setWindowTitle("Image and Text in GroupBox")
        self.resize(300, 300)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
