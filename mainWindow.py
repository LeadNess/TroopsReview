# -*- coding: utf-8 -*-
import os
import sys
from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtWidgets import (QWidget, QMainWindow, QDesktopWidget, QGridLayout, QLabel, QPushButton, QComboBox,
                             QMenuBar, QMenu, QStatusBar, QAction, QApplication, QDialog, QDialogButtonBox,
                             QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt5.QtGui import QIcon
from createNewMap import CreateNewMap

PROJECT_ROOT = os.path.dirname(__file__)
BACKGROUND_IMAGES_DIR = os.path.dirname(__file__) + '/data/images/background'
ELEMENTS_IMAGES_DIR = os.path.dirname(__file__) + '/data/images/elements'
ICONS_IMAGES_DIR = os.path.dirname(__file__) + '/data/images/icons'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setup_screen_size(self):
        desktop = QDesktopWidget()
        screen_size = desktop.availableGeometry()
        center_point = screen_size.center()

        width = screen_size.width() - 100
        height = screen_size.height() - 100
        self.setGeometry(center_point.x() - width / 2, center_point.y() - height / 2, width, height)

        self.setMinimumHeight(600)
        self.setMinimumWidth(800)

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
        create_new_file = CreateNewMap(self)
        create_new_file.show()

    def open_file(self):
        pass

    def show_info(self):
        info_message = QMessageBox(parent=self)
        info_message.setWindowTitle('О программе')
        info_message.setWindowIcon(QIcon(os.path.join(ICONS_IMAGES_DIR, 'about.png')))
        info_message.setIcon(QMessageBox.Question)
        info_message.setText("""© Lpshkn, 2020""")
        info_message.setStandardButtons(QMessageBox.Ok)
        info_message.frameGeometry().moveCenter(info_message.frameGeometry().center())
        info_message.show()

    def setupUi(self):
        self.setWindowTitle('Troops Review')
        self.setWindowIcon(QIcon(os.path.join(ICONS_IMAGES_DIR, 'mainIcon.png')))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinMaxButtonsHint)
        self.setup_screen_size()

        self.setup_menu()
        self.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())
