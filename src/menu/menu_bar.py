"""
This module represents a menu bar of the main window
"""
from PyQt5.QtWidgets import QMenuBar, QAction, QMessageBox
from PyQt5.QtGui import QIcon
from os.path import join, dirname
from menu.new_file import CreateNewMap


class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)

        self.ICONS_IMAGES_DIR = join(dirname(dirname(dirname(__file__))), 'resources', 'images', 'icons')

        self.CREATE_ICON = QIcon(join(self.ICONS_IMAGES_DIR, 'create.png'))
        self.OPEN_ICON = QIcon(join(self.ICONS_IMAGES_DIR, 'open.png'))
        self.ABOUT_ICON = QIcon(join(self.ICONS_IMAGES_DIR, 'about.png'))

        self.setup_bar()

    def setup_bar(self):
        file_menu = self.addMenu('&Файл')

        create_new_file = QAction(self.CREATE_ICON, 'Создать', self)
        create_new_file.setShortcut('Ctrl+N')
        create_new_file.setStatusTip('Создать новую карту')
        create_new_file.triggered.connect(self.create_file)
        file_menu.addAction(create_new_file)

        open_file = QAction(self.OPEN_ICON, 'Открыть', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('Открыть созданную ранее карту')
        open_file.triggered.connect(self.open_file)
        file_menu.addAction(open_file)

        help_menu = self.addMenu('&Помощь')
        reference = QAction(self.ABOUT_ICON, 'О программе', self)
        reference.setStatusTip('Показать информацию о данной программе')
        reference.triggered.connect(self.show_info)
        help_menu.addAction(reference)

    def create_file(self):
        parent = self.parent()
        parent.new_file_dialog = CreateNewMap(parent)
        parent.new_file_dialog.show()

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
