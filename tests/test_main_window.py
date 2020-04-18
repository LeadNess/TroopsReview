"""
Tests for src.main_window.main_window.py module
"""
import unittest
from os.path import isfile
from src.main_window.main_window import MainWindow
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow


class MainWindowTest(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.main_window = MainWindow()
        self.desktop = QDesktopWidget().availableGeometry()

    def tearDown(self):
        self.app.deleteLater()

    def test_width_height(self):
        self.assertEqual(self.main_window.width(), self.desktop.width() - 100)
        self.assertEqual(self.main_window.height(), self.desktop.height() - 100)

    def test_minimum_width_height(self):
        self.assertEqual(self.main_window.minimumWidth(), 800)
        self.assertEqual(self.main_window.minimumHeight(), 600)

    def test_center_point(self):
        x = self.main_window.geometry().center().x()
        y = self.main_window.geometry().center().y()

        x_desktop = self.desktop.center().x()
        y_desktop = self.desktop.center().y()

        # The main window's center point is set like the half of width or height of desktop
        # Therefore, variation between them must be less 1
        self.assertTrue(abs(x - x_desktop) <= 1)
        self.assertTrue(abs(y - y_desktop) <= 1)

    def test_setting_menubar(self):
        # Test that menubar was set. If it's new QMainWindow, then its menu bar must be None
        self.assertIsNotNone(self.main_window.menuWidget())
        self.assertIsNone(QMainWindow().menuWidget())

    def test_setting_title_parameters(self):
        self.assertEqual(self.main_window.windowTitle(), 'Troops review')
        # Check default icon path is a file
        self.assertTrue(isfile(self.main_window.ICON_PATH))

    def test_setting_central_widget(self):
        # The central widget isn't set at the moment
        self.assertIsNone(self.main_window.centralWidget())
        self.main_window.setup_central_widget('first', 'second')
        # But now it's set
        self.assertIsNotNone(self.main_window.centralWidget())