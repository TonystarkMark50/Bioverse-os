from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class Desktop(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("BioVerse OS Developer Preview")
        self.showMaximized()

        self.setStyleSheet("""
        QWidget{
            background-color:#0f172a;
            color:white;
        }
        """)

        layout = QVBoxLayout()

        title = QLabel("BioVerse OS")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 36))

        subtitle = QLabel("Developer Preview 0.1")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont("Segoe UI", 16))

        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()

        self.setLayout(layout)