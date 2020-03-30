# -*- coding: utf-8 -*-
import os
import sys
from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtWidgets import (QWidget, QMainWindow, QDesktopWidget, QGridLayout, QLabel, QPushButton, QComboBox,
                             QMenuBar, QMenu, QStatusBar, QAction, QApplication, QDialog, QDialogButtonBox,
                             QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QIcon

PROJECT_ROOT = os.path.dirname(__file__)
BACKGROUND_IMAGES_DIR = os.path.dirname(__file__) + '/data/images/background'
ELEMENTS_IMAGES_DIR = os.path.dirname(__file__) + '/data/images/elements'
ICONS_IMAGES_DIR = os.path.dirname(__file__) + '/data/images/icons'


class AboutInformation(QDialog):
    def __init__(self):
        super().__init__()

        self.resize(500, 500)

        self.setWindowTitle('О программе')
        self.setWindowIcon(QIcon(os.path.join(ICONS_IMAGES_DIR, 'about.png')))
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        self.button_box.accepted.connect(self.accept)

        self.label = QLabel("""
                            © Lpshkn, 2020""")

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.layout = QVBoxLayout()
        #self.layout.addWidget(self.button_box)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setup_screen_size(self):
        screen_size = QDesktopWidget().screenGeometry()
        self.resize(screen_size.width() - 200, screen_size.height() - 100)

    def setup_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&Файл')

        create_new_file = QAction(QIcon(os.path.join(ICONS_IMAGES_DIR, 'create.png')), 'Создать', self)
        create_new_file.setShortcut('Ctrl+N')
        create_new_file.setStatusTip('Создать новую карту')
        create_new_file.triggered.connect(self.create_file)
        file_menu.addAction(create_new_file)

        open_file = QAction(QIcon(os.path.join(ICONS_IMAGES_DIR, 'open.png')), 'Открыть', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('Открыть созданную ранее карту')
        open_file.triggered.connect(self.open_file)
        file_menu.addAction(open_file)

        help_menu = menubar.addMenu('&Помощь')
        reference = QAction(QIcon(os.path.join(ICONS_IMAGES_DIR, 'about.png')), 'О программе', self)
        reference.setStatusTip('Показать информацию о данной программе')
        reference.triggered.connect(self.show_info)
        help_menu.addAction(reference)

        self.statusBar()

    def create_file(self):
        pass

    def open_file(self):
        pass

    def show_info(self):
        self.information = AboutInformation()
        self.information.show()

    def setupUi(self):
        self.setup_screen_size()

        self.setup_menu()
        self.show()

    def changeBackgroundImage(self):
        imagePath = "data/images/background/" + str(self.backImagecomboBox.currentText())
        self.backgroundImage.setPixmap(QtGui.QPixmap(imagePath))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())
