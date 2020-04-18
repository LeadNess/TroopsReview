"""
This module implements the working with with a map, troops' elements at the right panel
and represents the main role in this program.
"""
from PyQt5.QtWidgets import QLabel, QWidget, QSizePolicy, QGraphicsScene
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from os.path import dirname, join
from os import listdir


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
        self.zoom = 1
        self.keys = set()

        self.set_troops_panel()
        self.set_map()

        self.map_area.current_scale = 1.0
        self.map_area.max_scale = 2

        self.map_area.wheelEvent = self.wheelEvent

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
        self.scene = QGraphicsScene()
        self.scene.addPixmap(QPixmap(self.map_filename))
        self.map_area.setScene(self.scene)
        self.map_area.show()

    def wheelEvent(self, event):
        if Qt.Key_Control in self.keys:
            self.map_area.min_scale_for_width = self.map_area.width() / self.scene.width()
            self.map_area.min_scale_for_height = self.map_area.height() / self.scene.height()

            scale_factor = 1.1

            if event.angleDelta().y() > 0:
                if self.map_area.current_scale * scale_factor <= self.map_area.maximum_scale:
                    self.map_area.scale(scale_factor, scale_factor)
                    self.map_area.current_scale *= scale_factor

            else:
                new_scale = self.map_area.current_scale / scale_factor

                if new_scale >= self.map_area.min_scale_for_width:
                    self.map_area.scale(1 / scale_factor, 1 / scale_factor)
                    self.map_area.current_scale /= scale_factor
                else:
                    scale = self.map_area.min_scale_for_width
                    self.map_area.scale(scale, scale)

        else:
            vertical = self.map_area.verticalScrollBar().value()
            horizontal = self.map_area.horizontalScrollBar().value()

            if event.angleDelta().y() > 0:
                vertical -= 30
                horizontal -= 30
            else:
                vertical += 30
                horizontal += 30

            if Qt.Key_Shift in self.keys:
                self.map_area.horizontalScrollBar().setValue(horizontal)
            else:
                self.map_area.verticalScrollBar().setValue(vertical)

    def keyPressEvent(self, event):
        self.keys.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys.remove(event.key())



