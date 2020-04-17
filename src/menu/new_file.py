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
from os.path import dirname, join, isfile, isdir


class CreateNewMap(QDialog):
    """This class creates a new map with settings were defined in the dialog window."""

    def __init__(self, parent):
        QDialog.__init__(self, parent)
        # Define the filename to ui file of that Dialog
        self.FILENAME_UI = join(dirname(dirname(dirname(__file__))), 'resources', 'ui', 'new_file.ui')

        # Load .ui file and initialize it
        try:
            uic.loadUi(self.FILENAME_UI, self)
        except FileNotFoundError as e:
            print(e)
            exit(-1)

        self.ICONS_IMAGES_DIR = join(dirname(dirname(dirname(__file__))), 'resources', 'images', 'icons')

        # Setup main icon to the left corner of the window
        PATH = join(self.ICONS_IMAGES_DIR, 'mainIcn.png')
        if not isfile(PATH):
            print(f"Error: No such file: {PATH}")
        self.MAIN_ICON = QIcon(PATH)

        # Set the icon or any settings
        self.configure_ui()

        # These values specify that paths were written in the edit line by user were incorrect.
        self.incorrect_map_filename = False
        self.incorrect_troops_directory = False

        # These values are necessary to find out indices of lines edit
        # Initially they are known from the ui file
        self.index_maps_line = 1
        self.index_troops_line = 3

    def configure_ui(self):
        """
        Set the window's configuration.
        """
        self.setWindowIcon(self.MAIN_ICON)
        self.setWindowModality(Qt.ApplicationModal)

    def correct_wrong_path(self):
        """
        This function provides correcting wrong paths to files and directories. It's a slot which called when
        both of edit lines is changing. If one of the paths is incorrect, then the error will be removed.
        """
        sender = self.sender()

        # This block provides removing an error under the edit line of the map's filename
        if sender == self.mapsDirectoryLine and self.incorrect_map_filename:
            self.VLayout.removeWidget(self.error_maps_lbl)
            self.error_maps_lbl.deleteLater()
            self.incorrect_map_filename = False
            self.index_troops_line -= 1

        # This block provides removing an error under the edit line of the troops' directory name
        elif sender == self.troopsDirectoryLine and self.incorrect_troops_directory:
            self.VLayout.removeWidget(self.error_troops_lbl)
            self.error_troops_lbl.deleteLater()
            self.incorrect_troops_directory = False

    def enable_accept_button(self):
        """
        This module enables or disables the accept button for this dialog window depending on whether
        there is text in the edit lines.
        """
        if self.mapsDirectoryLine.text() and self.troopsDirectoryLine.text():
            self.acceptButton.setEnabled(True)
        else:
            self.acceptButton.setEnabled(False)

    def files_manage(self):
        """
        It's a slot which is called when the setting button is pressed
        This method opens the file manager and if a directory or a file is chosen, it fills edit lines
        """
        sender = self.sender()

        if sender == self.mapsDirectoryButton:
            path_to_map, _ = QFileDialog.getOpenFileName(self,
                                                         caption="Открыть",
                                                         directory="/",
                                                         filter="Image files (*.jpg *.JPG *.png *.jpeg *.bmp")

            if path_to_map:
                self.mapsDirectoryLine.setText(path_to_map)

        elif sender == self.troopsDirectoryButton:
            directory = QFileDialog.getExistingDirectory(self,
                                                         caption="Открыть",
                                                         directory="/")

            if directory:
                self.troopsDirectoryLine.setText(directory)

    def accept(self):
        """
        It's slot which is called when the accept button is pressed, if it's enabled
        This method checks that a specified directory or a file is correct and calls the method of creating
        central widget in the parent widget. Else this method prints an error about that trouble under the edit line
        and sets particular flags, specifying that error was occurred.
        """

        map_filename = self.mapsDirectoryLine.text()
        troops_directory = self.troopsDirectoryLine.text()

        if not isfile(map_filename) and not self.incorrect_map_filename:
            self.error_maps_lbl = QLabel("Ошибка: данного файла не существует", self)
            self.error_maps_lbl.setStyleSheet('QLabel { color : red; }')
            self.VLayout.insertWidget(self.index_maps_line + 1, self.error_maps_lbl)
            self.index_troops_line += 1
            self.incorrect_map_filename = True
            self.acceptButton.setEnabled(False)

        if not isdir(troops_directory) and not self.incorrect_troops_directory:
            self.error_troops_lbl = QLabel("Ошибка: данной директории не существует", self)
            self.error_troops_lbl.setStyleSheet('QLabel { color : red; }')
            self.VLayout.insertWidget(self.index_troops_line + 1, self.error_troops_lbl)
            self.incorrect_troops_directory = True
            self.acceptButton.setEnabled(False)

        if not self.incorrect_troops_directory and not self.incorrect_map_filename:
            super().accept()
            self.parent().setup_central_widget(map_filename, troops_directory)
