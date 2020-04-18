"""
Tests for src.main_window.main_window.py module
"""
import unittest
from PyQt5 import QtTest
from src.main_window.main_window import MainWindow
from PyQt5.QtWidgets import QDesktopWidget, QApplication


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






