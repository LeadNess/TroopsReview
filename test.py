# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

PROJECT_ROOT = os.path.dirname(__file__)
BACKGROUND_IMAGES_DIR = os.path.dirname(__file__) + '/data/images/background'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1039, 757)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.backImagecomboBox.addItems(os.listdir(BACKGROUND_IMAGES_DIR))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1039, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.backImageChangeButton.clicked.connect(self.changeBackgroundImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backImageChangeButton.setText(_translate("MainWindow", "Поменять"))
        self.chooseBackgroundImageLabel.setText(_translate("MainWindow", "Выберете фоновую карту"))

    def changeBackgroundImage(self):
        imagePath = "data/images/background/" + str(self.backImagecomboBox.currentText())
        self.backgroundImage.setPixmap(QtGui.QPixmap(imagePath))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

