import sys
from PyQt5.QtWidgets import QApplication
from main_window.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())
