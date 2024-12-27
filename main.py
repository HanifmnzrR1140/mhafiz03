import sys
from PySide6.QtWidgets import QApplication
from controller import CalculatorApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())
