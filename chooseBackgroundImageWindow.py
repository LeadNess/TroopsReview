# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseBackgroundImageWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os


PROJECT_ROOT = os.path.dirname(__file__)
BACKGROUND_IMAGES_DIR = os.path.dirname(__file__) + '/data/images/background'


class Ui_chooseBackgroundImageWindow(object):
    def setupUi(self, chooseBackgroundImageWindow):
        chooseBackgroundImageWindow.setObjectName("chooseBackgroundImageWindow")
        chooseBackgroundImageWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(chooseBackgroundImageWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)
        chooseBackgroundImageWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(chooseBackgroundImageWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        chooseBackgroundImageWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(chooseBackgroundImageWindow)
        self.statusbar.setObjectName("statusbar")
        chooseBackgroundImageWindow.setStatusBar(self.statusbar)

        self.retranslateUi(chooseBackgroundImageWindow)
        QtCore.QMetaObject.connectSlotsByName(chooseBackgroundImageWindow)
        self.populate()

    def populate(self):
        path = PROJECT_ROOT
        model = QtWidgets.QFileSystemModel()
        model.setRootPath(QtCore.QDir.rootPath())
        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(path))

    def retranslateUi(self, chooseBackgroundImageWindow):
        _translate = QtCore.QCoreApplication.translate
        chooseBackgroundImageWindow.setWindowTitle(_translate("chooseBackgroundImageWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(1, _translate("chooseBackgroundImageWindow", "Файлы"))
        self.treeWidget.headerItem().setText(2, _translate("chooseBackgroundImageWindow", "Время изменения"))
        self.treeWidget.headerItem().setText(3, _translate("chooseBackgroundImageWindow", "Размер"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    chooseBackgroundImageWindow = QtWidgets.QMainWindow()
    ui = Ui_chooseBackgroundImageWindow()
    ui.setupUi(chooseBackgroundImageWindow)
    chooseBackgroundImageWindow.show()
    sys.exit(app.exec_())

