import io
import unittest.mock
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow
from src.menu.new_file import NewFileDialog


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.main = QMainWindow()
        self.new_map = NewFileDialog(self.main)

    def tearDown(self):
        self.app.deleteLater()

    @unittest.mock.patch("src.menu.new_file.NewFileDialog.ICONS_IMAGES_DIR", 'incorrect')
    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_incorrect_path_icon(self, io_string):
        NewFileDialog(QMainWindow())
        self.assertEqual(io_string.getvalue(), 'Error: No such file: incorrect\\mainIcon.png\n')

    @unittest.mock.patch("src.menu.new_file.NewFileDialog.FILENAME_UI", 'incorrect')
    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_incorrect_io_file(self, io_string):
        # When you create an instance, FileNotFoundError will be raised and sys.exit will be called
        with self.assertRaises(SystemExit):
            NewFileDialog(QMainWindow())

    def test_default_flags(self):
        dialog = NewFileDialog(QMainWindow())
        self.assertFalse(dialog.incorrect_map_filename)
        self.assertFalse(dialog.incorrect_troops_directory)

    def test_setting_modality(self):
        self.assertTrue(self.new_map.isModal())
