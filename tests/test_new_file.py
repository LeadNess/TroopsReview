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



