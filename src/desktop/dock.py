from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class Dock(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(70)

        self.setStyleSheet("""
        QWidget{
            background:#1E293B;
        }

        QPushButton{
            background:#334155;
            color:white;
            border:none;
            border-radius:10px;
            min-width:60px;
            min-height:50px;
            font-size:16px;
        }

        QPushButton:hover{
            background:#3B82F6;
        }
        """)

        layout = QHBoxLayout()

        apps = [
            "📁",
            "🌐",
            "💻",
            "⚙",
            "🤖"
        ]

        layout.addStretch()

        for app in apps:
            button = QPushButton(app)
            layout.addWidget(button)

        layout.addStretch()

        self.setLayout(layout)