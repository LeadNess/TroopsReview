"""
This module represents the map that is instance of QGraphicsView. There are methods to work with it in here.
"""

from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MapArea(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)

        self.zoom = 1
        self.current_scale = 1.0
        self.maximum_scale = 2

        self.scene = QGraphicsScene()
        self.keys = set()

    def set_map(self, filename: str):
        self.scene.addPixmap(QPixmap(filename))
        self.setScene(self.scene)

    def wheelEvent(self, event):
        if Qt.Key_Control in self.keys:
            self.min_scale_for_width = self.width() / self.scene.width()
            self.min_scale_for_height = self.height() / self.scene.height()

            scale_factor = 1.1

            if event.angleDelta().y() > 0:
                if self.current_scale * scale_factor <= self.maximum_scale:
                    self.scale(scale_factor, scale_factor)
                    self.current_scale *= scale_factor

            else:
                new_scale = self.current_scale / scale_factor

                if new_scale >= self.min_scale_for_width:
                    self.scale(1 / scale_factor, 1 / scale_factor)
                    self.current_scale /= scale_factor
                else:
                    scale = self.current_scale / self.min_scale_for_width
                    self.scale(1 / scale, 1 / scale)
                    self.current_scale /= scale
        else:
            vertical = self.verticalScrollBar().value()
            horizontal = self.horizontalScrollBar().value()

            if event.angleDelta().y() > 0:
                vertical -= 75
                horizontal -= 75
            else:
                vertical += 75
                horizontal += 75

            if Qt.Key_Shift in self.keys:
                self.horizontalScrollBar().setValue(horizontal)
            else:
                self.verticalScrollBar().setValue(vertical)

    def keyPressEvent(self, event):
        self.keys.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys.remove(event.key())
