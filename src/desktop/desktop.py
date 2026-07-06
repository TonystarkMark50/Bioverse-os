from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from taskbar import Taskbar
from dock import Dock


class Desktop(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("BioVerse OS")

        self.showMaximized()

        self.setStyleSheet("""
        QWidget{
            background:#0F172A;
            color:white;
        }
        """)

        layout = QVBoxLayout()

        self.taskbar = Taskbar()

        layout.addWidget(self.taskbar)

        title = QLabel("BioVerse Desktop")

        title.setAlignment(Qt.AlignCenter)

        title.setFont(QFont("Segoe UI",32))

        layout.addStretch()

        layout.addWidget(title)

        layout.addStretch()

        self.dock = Dock()

        layout.addWidget(self.dock)

        self.setLayout(layout)