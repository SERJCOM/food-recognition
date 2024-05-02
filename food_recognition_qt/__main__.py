from widget import Widget
import sys
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
