# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os


PROJECT_ROOT = os.path.dirname(__file__)
BACKGROUND_IMAGES_DIR = os.path.dirname(__file__) + '/data/images/background'


class Ui_addBackgroundImageLabel(object):
    def setupUi(self, addBackgroundImageLabel):
        addBackgroundImageLabel.setObjectName("addBackgroundImageLabel")
        addBackgroundImageLabel.resize(1035, 757)
        self.centralwidget = QtWidgets.QWidget(addBackgroundImageLabel)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.backgroundImage = QtWidgets.QLabel(self.centralwidget)
        self.backgroundImage.setGeometry(QtCore.QRect(10, 70, 781, 631))
        self.backgroundImage.setStyleSheet(".brd {\n"
"    border: 4px double black; /* Параметры границы */\n"
"    background: #fc3; /* Цвет фона */\n"
"    padding: 10px; /* Поля вокруг текста */\n"
"}\n"
"  ")
        self.backgroundImage.setText("")
        self.backgroundImage.setPixmap(QtGui.QPixmap("data/images/background/example.jpg"))
        self.backgroundImage.setScaledContents(True)
        self.backgroundImage.setObjectName("backgroundImage")
        self.backImageChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.backImageChangeButton.setGeometry(QtCore.QRect(820, 130, 181, 25))
        self.backImageChangeButton.setObjectName("backImageChangeButton")
        self.chooseBackgroundImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseBackgroundImageLabel.setGeometry(QtCore.QRect(820, 70, 191, 17))
        self.chooseBackgroundImageLabel.setObjectName("chooseBackgroundImageLabel")
        self.backImagecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.backImagecomboBox.setGeometry(QtCore.QRect(820, 100, 181, 25))
        self.backImagecomboBox.setObjectName("backImagecomboBox")
        addBackgroundImageLabel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(addBackgroundImageLabel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        addBackgroundImageLabel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(addBackgroundImageLabel)
        self.statusbar.setObjectName("statusbar")
        addBackgroundImageLabel.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(addBackgroundImageLabel)
        self.action.setObjectName("action")
        self.menu.addSeparator()
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(addBackgroundImageLabel)
        QtCore.QMetaObject.connectSlotsByName(addBackgroundImageLabel)

        self.backImageChangeButton.clicked.connect(self.changeBackgroundImage)

    def changeBackgroundImage(self):
        imagePath = "data/images/background/" + str(self.backImagecomboBox.currentText())
        self.backgroundImage.setPixmap(QtGui.QPixmap(imagePath))

    def retranslateUi(self, addBackgroundImageLabel):
        _translate = QtCore.QCoreApplication.translate
        addBackgroundImageLabel.setWindowTitle(_translate("addBackgroundImageLabel", "MainWindow"))
        self.backImageChangeButton.setText(_translate("addBackgroundImageLabel", "Поменять"))
        self.chooseBackgroundImageLabel.setText(_translate("addBackgroundImageLabel", "Выберете фоновую карту"))
        self.menu.setTitle(_translate("addBackgroundImageLabel", "Файлы"))
        self.action.setText(_translate("addBackgroundImageLabel", "Добавить фоновую карту"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addBackgroundImageLabel = QtWidgets.QMainWindow()
    ui = Ui_addBackgroundImageLabel()
    ui.setupUi(addBackgroundImageLabel)
    addBackgroundImageLabel.show()
    sys.exit(app.exec_())

