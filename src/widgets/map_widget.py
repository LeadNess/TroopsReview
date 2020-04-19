"""
This module implements the working with with a map, troops' elements at the right panel
and represents the main role in this program.
"""
from PyQt5.QtWidgets import QLabel, QWidget, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from os.path import dirname, join
from os import listdir
from src.widgets.map_area import MapArea

# Define the directory of ui's files
UI_DIR = join(dirname(dirname(dirname(__file__))), 'resources', 'ui')
# Define the filename to ui file of that widget
FILENAME_UI = join(UI_DIR, 'centralWidget.ui')
# Define the form class of that ui
FORM_CLASS = uic.loadUiType(FILENAME_UI)[0]


def load_images(directory, width=None, height=None):
    """
    Function returns list of QPixmap's instances will be able to scale to width X height

    :param directory: Str. Directory where images will be searched.
    :param height: (Optional) Int. Height to which the image will be scale.
    :param width: (Optional) Int. Width to which the image will be scale.
    :return: list of QPixmap's instances.
    """

    files = listdir(directory)
    images = list(filter(lambda x: x[len(x)-3:len(x)].lower() in ['png', 'jpeg', 'jpg', 'bmp'], files))
    images = [QPixmap(join(directory, image)) for image in images]

    if width and height:
        return [image.scaled(width, height) for image in images]
    else:
        return images


class CentralWidget(QWidget, FORM_CLASS):
    """
    Class represents the main action in this program. It provides the ability to modulate fight actions at the map.
    Also it allows to drag troops' images into the map from the right panel, which it implements too.
    """
    def __init__(self, parent, map_filename, troops_directory):
        QWidget.__init__(self, parent)

        self.setupUi(self)

        self.map_filename = map_filename
        self.troops_directory = troops_directory
        self.map_area = MapArea(self)

        self.gridLayout.replaceWidget(self.mapArea, self.map_area)
        self.mapArea.deleteLater()

        self.set_troops_panel()
        self.set_map()

    def set_troops_panel(self):
        try:
            # Load images scaled to the width of the right-hand panel from selected directory
            images = load_images(self.troops_directory, self.troops_panel.minimumWidth(), self.troops_panel.minimumWidth())
        except FileNotFoundError:
            print(f"FileNotFoundError: \"{__name__}\" can't load images from \"{self.troops_directory}\"")
            return

        for image in images:
            label = QLabel(self.troops_panel)
            label.setPixmap(image)
            label.setMinimumHeight(self.troops_panel.minimumWidth())
            label.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
            self.troops_vertical_layout.addWidget(label)

    def set_map(self):
        self.map_area.set_map(self.map_filename)
        self.map_area.show()



