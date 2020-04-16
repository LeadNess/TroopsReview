"""
This module represents the class to work with the main window. There are methods to setup geometry, setup
menu bar, widgets e.t.c.
"""
from os.path import dirname, join
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QAction, QMessageBox)
from PyQt5.QtGui import QIcon
from menu import menu_bar
from widgets.map_widget import CentralWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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
        menubar = menu_bar.MenuBar(self)
        self.setMenuBar(menubar)
        self.statusBar()

    def setup_title_settings(self):
        self.setWindowTitle('Troops review')
        self.setWindowIcon(QIcon(join(self.ICONS_IMAGES_DIR, 'mainIcon.png')))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinMaxButtonsHint)

    def setup_ui(self):
        self.setup_geometry()
        self.setup_title_settings()
        self.setup_menu()

        self.showMaximized()

    def setup_central_widget(self, map_filename: str, troops_directory: str):
        central_widget = CentralWidget(self, map_filename, troops_directory)
        self.setCentralWidget(central_widget)
        central_widget.show()

