"""
This module represents a menu bar of the main window
"""
from PyQt5.QtWidgets import QMenuBar, QAction, QMessageBox
from PyQt5.QtGui import QIcon
from os.path import join, dirname, isfile
from menu.new_file import CreateNewMap


class MenuBar(QMenuBar):
    ICONS_IMAGES_DIR = join(dirname(dirname(dirname(__file__))), 'resources', 'images', 'icons')
    CREATE_ICON_PATH = join(ICONS_IMAGES_DIR, 'create.png')
    OPEN_ICON_PATH = join(ICONS_IMAGES_DIR, 'open.png')
    ABOUT_ICON_PATH = join(join(ICONS_IMAGES_DIR, 'about.png'))

    def __init__(self, parent):
        super().__init__(parent)

        self.CREATE_ICON = QIcon(self.CREATE_ICON_PATH)
        self.OPEN_ICON = QIcon(self.OPEN_ICON_PATH)
        self.ABOUT_ICON = QIcon(self.ABOUT_ICON_PATH)

        if not isfile(self.CREATE_ICON_PATH):
            print(f"Error: No such file: {self.CREATE_ICON_PATH}")
        if not isfile(self.OPEN_ICON_PATH):
            print(f"Error: No such file: {self.OPEN_ICON_PATH}")
        if not isfile(self.ABOUT_ICON_PATH):
            print(f"Error: No such file: {self.ABOUT_ICON_PATH}")

        self.setup_bar()

    def setup_bar(self):
        """
        This method setups menu buttons and connects them to their slots. Every slots of them is in that class.
        Also, this methods sets the status tip to every action.
        """

        # Set the "File" menu. There are actions of opening, saving or other actions to working with files
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

        # Set the "Help" menu. There actions of getting a help, information about application etc.
        help_menu = self.addMenu('&Помощь')
        reference = QAction(self.ABOUT_ICON, 'О программе', self)
        reference.setStatusTip('Показать информацию о данной программе')
        reference.triggered.connect(self.show_info)
        help_menu.addAction(reference)

    def create_file(self):
        """
        The slot, which called by action of creating new file
        """
        parent = self.parent()
        parent.new_file_dialog = CreateNewMap(parent)
        parent.new_file_dialog.show()

    def open_file(self):
        """
        The slot, which called by action of opening existed file
        """
        pass

    def show_info(self):
        """
        The slot, which called by action of getting information about that program
        """

        info_message = QMessageBox(parent=self)
        info_message.setWindowTitle('О программе')
        info_message.setWindowIcon(self.ABOUT_ICON)
        info_message.setIcon(QMessageBox.Question)
        info_message.setText("""© Lpshkn, 2020""")
        info_message.setStandardButtons(QMessageBox.Ok)
        info_message.frameGeometry().moveCenter(info_message.frameGeometry().center())
        info_message.show()
