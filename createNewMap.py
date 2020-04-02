from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import os

UI_DIR = os.path.dirname(__file__) + '/ui'
FILENAME_UI = os.path.join(UI_DIR, 'new_file.ui')
FORM_CLASS = uic.loadUiType(FILENAME_UI)[0]
ICONS_IMAGES_DIR = os.path.dirname(__file__) + '/data/images/icons'


class CreateNewMap(QDialog, FORM_CLASS):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.configure_ui()

    def configure_ui(self):
        self.setWindowIcon(QIcon(os.path.join(ICONS_IMAGES_DIR, 'mainIcon.png')))
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(self.size())

    def enable_accept_button(self):
        if self.mapsDirectoryLine.text() and self.troopsDirectoryLine.text():
            self.acceptButton.setEnabled(True)
        else:
            self.acceptButton.setEnabled(False)

    def maps_manage(self):
        sender = self.sender()

        directory = QFileDialog.getExistingDirectory(self, caption="Открыть", directory="")

        if directory:
            if sender == self.mapsDirectoryButton:
                self.mapsDirectoryLine.setText(directory)
            elif sender == self.troopsDirectoryButton:
                self.troopsDirectoryLine.setText(directory)

    def accept(self):
        pass
