"""
This module represents the class to work with the main window. There are methods to setup geometry, setup
menu bar, widgets e.t.c.
"""
from os.path import dirname, join
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QAction, QMessageBox)
from PyQt5.QtGui import QIcon
from menu.new_file import CreateNewMap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Define the directory of ui's files
        self.ICONS_IMAGES_DIR = join(dirname(dirname(dirname(__file__))), 'resources', 'images', 'icons')
        self.setup_ui()

    def setup_geometry(self):
        """
        Setup geometry of the main window. It determines screen dimensions and a central point, then uses it to
        setup particular geometry.
        """

        # Determine screen dimensions and central point
        desktop = QDesktopWidget()
        screen_size = desktop.availableGeometry()
        center_point = screen_size.center()

        # Determine dimensions and subtract some pixels in order to the window will not out of bounds
        width = screen_size.width() - 100
        height = screen_size.height() - 100
        self.setGeometry(center_point.x() - width / 2, center_point.y() - height / 2, width, height)

        # Setup minimal dimensions
        self.setMinimumHeight(600)
        self.setMinimumWidth(800)

    def setup_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&Файл')

        create_new_file = QAction(QIcon(join(self.ICONS_IMAGES_DIR, 'create.png')), 'Создать', self)
        create_new_file.setShortcut('Ctrl+N')
        create_new_file.setStatusTip('Создать новую карту')
        create_new_file.triggered.connect(self.create_file)
        file_menu.addAction(create_new_file)

        open_file = QAction(QIcon(join(self.ICONS_IMAGES_DIR, 'open.png')), 'Открыть', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('Открыть созданную ранее карту')
        open_file.triggered.connect(self.open_file)
        file_menu.addAction(open_file)

        help_menu = menubar.addMenu('&Помощь')
        reference = QAction(QIcon(join(self.ICONS_IMAGES_DIR, 'about.png')), 'О программе', self)
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
        info_message.setWindowIcon(QIcon(join(self.ICONS_IMAGES_DIR, 'about.png')))
        info_message.setIcon(QMessageBox.Question)
        info_message.setText("""© Lpshkn, 2020""")
        info_message.setStandardButtons(QMessageBox.Ok)
        info_message.frameGeometry().moveCenter(info_message.frameGeometry().center())
        info_message.show()

    def setup_title_settings(self):
        self.setWindowTitle('Troops review')
        self.setWindowIcon(QIcon(join(self.ICONS_IMAGES_DIR, 'mainIcon.png')))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinMaxButtonsHint)

    def setup_ui(self):
        self.setup_geometry()
        self.setup_title_settings()
        self.setup_menu()

        self.showMaximized()
