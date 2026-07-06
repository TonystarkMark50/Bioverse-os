import sys
from PySide6.QtWidgets import QApplication
from desktop import Desktop

def main():
    app = QApplication(sys.argv)

    window = Desktop()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()