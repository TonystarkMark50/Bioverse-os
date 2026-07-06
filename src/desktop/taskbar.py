from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt, QTimer
from datetime import datetime


class Taskbar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(45)

        self.setStyleSheet("""
            QWidget{
                background:#1E293B;
                color:white;
            }

            QPushButton{
                background:#2563EB;
                color:white;
                border:none;
                border-radius:6px;
                padding:6px 12px;
            }
        """)

        layout = QHBoxLayout()

        self.start = QPushButton("BioVerse")

        layout.addWidget(self.start)

        layout.addStretch()

        self.clock = QLabel()

        layout.addWidget(self.clock)

        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.update_clock)
        timer.start(1000)

        self.update_clock()

    def update_clock(self):
        self.clock.setText(datetime.now().strftime("%H:%M:%S"))