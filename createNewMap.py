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

        # These values specify that paths were written in the edit line by user were incorrect.
        self.incorrect_maps_directory = False
        self.incorrect_troops_directory = False

        # These values are necessary to find out indices of lines edit
        # Initially they are known from the ui file
        self.index_maps_line = 1
        self.index_troops_line = 3

    def configure_ui(self):
        self.setWindowIcon(QIcon(os.path.join(ICONS_IMAGES_DIR, 'mainIcon.png')))
        self.setWindowModality(Qt.ApplicationModal)

    def enable_accept_button(self):
        if self.mapsDirectoryLine.text() and self.troopsDirectoryLine.text():
            self.acceptButton.setEnabled(True)
        else:
            self.acceptButton.setEnabled(False)

    def files_manage(self):
        sender = self.sender()

        directory = QFileDialog.getExistingDirectory(self, caption="Открыть", directory="")

        if directory:
            if sender == self.mapsDirectoryButton:
                self.mapsDirectoryLine.setText(directory)
            elif sender == self.troopsDirectoryButton:
                self.troopsDirectoryLine.setText(directory)

    def accept(self):
        mapsDirectory = self.mapsDirectoryLine.text()
        troopsDirectory = self.troopsDirectoryLine.text()

        if not os.path.isdir(mapsDirectory) and not self.incorrect_maps_directory:
            self.error_maps_lbl = QLabel("Ошибка: данной директории не существует", self)
            self.error_maps_lbl.setStyleSheet('QLabel { color : red; }')
            self.VLayout.insertWidget(self.index_maps_line + 1, self.error_maps_lbl)
            self.index_troops_line += 1
            self.incorrect_maps_directory = True
            self.acceptButton.setEnabled(False)

        if not os.path.isdir(troopsDirectory) and not self.incorrect_troops_directory:
            self.error_troops_lbl = QLabel("Ошибка: данной директории не существует", self)
            self.error_troops_lbl.setStyleSheet('QLabel { color : red; }')
            self.VLayout.insertWidget(self.index_troops_line + 1, self.error_troops_lbl)
            self.incorrect_troops_directory = True
            self.acceptButton.setEnabled(False)
