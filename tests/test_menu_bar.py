import unittest
import unittest.mock
import io
import sys
from src.menu.menu_bar import MenuBar
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow


class MenuBarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.app = QApplication([])
        self.main = QMainWindow()
        self.menubar = MenuBar(self.main)

        # Define menu buttons (they are on top ot the menu bar)
        self.file_menu = self.menubar.actions()[0].menu()
        self.help_menu = self.menubar.actions()[1].menu()

        # Define actions for the "File" menu (these actions appear then is putted the cursor in the "File" menu)
        self.new_file_button = self.file_menu.actions()[0]
        self.open_file_button = self.file_menu.actions()[1]

        # Define actions for the "Help" menu (these actions appear then is putted the cursor in the "Help" menu)
        self.about_button = self.help_menu.actions()[0]

    def tearDown(self):
        self.app.deleteLater()

    # These paths aren't exist
    @unittest.mock.patch('src.menu.menu_bar.MenuBar.ABOUT_ICON_PATH', 'wrong_about')
    @unittest.mock.patch('src.menu.menu_bar.MenuBar.OPEN_ICON_PATH', 'wrong_open')
    @unittest.mock.patch('src.menu.menu_bar.MenuBar.CREATE_ICON_PATH', 'wrong_create')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_incorrect_default_icons_filenames(self, mock_stdout):
        # The constructor will check paths and will print errors to the console. Important to compare this
        # text in the console and that error message
        menubar = MenuBar(self.main)
        self.assertEqual(mock_stdout.getvalue(), f"Error: No such file: {MenuBar.CREATE_ICON_PATH}\n"
                                                 f"Error: No such file: {MenuBar.OPEN_ICON_PATH}\n"
                                                 f"Error: No such file: {MenuBar.ABOUT_ICON_PATH}\n")

    # It's necessary to not show the dialog window
    @unittest.mock.patch('PyQt5.QtWidgets.QDialog.show', print)
    def test_pressing_button_create_file(self):
        # The dialog of creating new file doesn't exist at the moment
        with self.assertRaises(AttributeError):
            var = self.main.new_file_dialog

        # Click the button of creating new file
        self.new_file_button.trigger()
        # And now that dialog exists
        self.assertIsNotNone(self.main.new_file_dialog)

    @unittest.mock.patch('PyQt5.QtWidgets.QMessageBox.show', print)
    def test_pressing_button_information(self):
        with self.assertRaises(AttributeError):
            var = self.menubar.info_message

        self.about_button.trigger()
        self.assertIsNotNone(self.menubar.info_message)
        self.assertEqual(self.menubar.info_message.windowTitle(), 'О программе')