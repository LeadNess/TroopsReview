"""
This class represents the Dialog, which allows you to define paths to directories containing of
necessary background maps and pictures of troops. Also, this class prevents tries to
input incorrect paths of directories, but doesn't check them for emptiness, considering that
it's necessary for the user.
"""

from PyQt5.QtWidgets import QDialog, QFileDialog, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import os
from centralWidget import CentralWidget

# Define the directory of ui's files
UI_DIR = os.path.dirname(__file__) + '/ui'
# Define the filename to ui file of that Dialog
FILENAME_UI = os.path.join(UI_DIR, 'new_file.ui')
# Define the form class of that ui
FORM_CLASS = uic.loadUiType(FILENAME_UI)[0]
# Define the filename of the directory of icons
ICONS_IMAGES_DIR = os.path.dirname(__file__) + '/data/images/icons'


class CreateNewMap(QDialog, FORM_CLASS):
    """This class creates a new map with settings were defined in the dialog window."""

    def __init__(self, parent):
        QDialog.__init__(self, parent)

        # Set the configuration was defined in ui file.
        self.setupUi(self)
        # Set the icon or any settings
        self.configure_ui()

        # These values specify that paths were written in the edit line by user were incorrect.
        self.incorrect_maps_directory = False
        self.incorrect_troops_directory = False

        # These values are necessary to find out indices of lines edit
        # Initially they are known from the ui file
        self.index_maps_line = 1
        self.index_troops_line = 3

    def configure_ui(self):
        """
        Set the window's configuration.
        """
        self.setWindowIcon(QIcon(os.path.join(ICONS_IMAGES_DIR, 'mainIcon.png')))
        self.setWindowModality(Qt.ApplicationModal)

    def enable_accept_button(self):
        sender = self.sender()

        if self.incorrect_maps_directory and sender == self.mapsDirectoryLine:
            self.VLayout.removeWidget(self.error_maps_lbl)
            self.error_maps_lbl.deleteLater()
            self.incorrect_maps_directory = False
            self.index_troops_line -= 1

        if self.incorrect_troops_directory and sender == self.troopsDirectoryLine:
            self.VLayout.removeWidget(self.error_troops_lbl)
            self.error_troops_lbl.deleteLater()
            self.incorrect_troops_directory = False

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
        maps_directory = self.mapsDirectoryLine.text()
        troops_directory = self.troopsDirectoryLine.text()

        if not os.path.isdir(maps_directory) and not self.incorrect_maps_directory:
            self.error_maps_lbl = QLabel("Ошибка: данной директории не существует", self)
            self.error_maps_lbl.setStyleSheet('QLabel { color : red; }')
            self.VLayout.insertWidget(self.index_maps_line + 1, self.error_maps_lbl)
            self.index_troops_line += 1
            self.incorrect_maps_directory = True
            self.acceptButton.setEnabled(False)

        if not os.path.isdir(troops_directory) and not self.incorrect_troops_directory:
            self.error_troops_lbl = QLabel("Ошибка: данной директории не существует", self)
            self.error_troops_lbl.setStyleSheet('QLabel { color : red; }')
            self.VLayout.insertWidget(self.index_troops_line + 1, self.error_troops_lbl)
            self.incorrect_troops_directory = True
            self.acceptButton.setEnabled(False)

        if not self.incorrect_troops_directory and not self.incorrect_maps_directory:
            super().accept()
            central_widget = CentralWidget(self.parent(), maps_directory, troops_directory)
            self.parent().setCentralWidget(central_widget)
            central_widget.show()
