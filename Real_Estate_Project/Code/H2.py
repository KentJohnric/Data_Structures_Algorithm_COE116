# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_House2Ui(object):
    def setupUi(self, House2Ui):
        House2Ui.setObjectName("House2Ui")
        House2Ui.resize(950, 542)
        House2Ui.setMinimumSize(QtCore.QSize(950, 542))
        House2Ui.setMaximumSize(QtCore.QSize(950, 542))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main/Main/Toma4025-Tea-Tea-plant-leaf.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        House2Ui.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(House2Ui)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(9, 9, 931, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.H2Tab1 = QtWidgets.QWidget()
        self.H2Tab1.setObjectName("H2Tab1")
        self.textBrowser = QtWidgets.QTextBrowser(self.H2Tab1)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 491, 451))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox = QtWidgets.QGroupBox(self.H2Tab1)
        self.groupBox.setGeometry(QtCore.QRect(500, -10, 421, 491))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.stackedWidget.addWidget(self.page_7)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_8 = QtWidgets.QLabel(self.page_5)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/House2/House 2/1.jpeg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout = QtWidgets.QGridLayout(self.page)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/House2/House 2/7.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/House2/House 2/2.jpeg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_6 = QtWidgets.QLabel(self.page_6)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/House2/House 2/4.jpeg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/House2/House 2/3.jpeg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/House2/House 2/5.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_8.addWidget(self.stackedWidget, 2, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(6)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_8.addWidget(self.spinBox, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.H2Buy = QtWidgets.QPushButton(self.groupBox)
        self.H2Buy.setObjectName("H2Buy")
        self.horizontalLayout.addWidget(self.H2Buy)
        self.H2Cancel = QtWidgets.QPushButton(self.groupBox)
        self.H2Cancel.setObjectName("H2Cancel")
        self.horizontalLayout.addWidget(self.H2Cancel)
        self.gridLayout_8.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.tabWidget.addTab(self.H2Tab1, "")
        self.H2Tab2 = QtWidgets.QWidget()
        self.H2Tab2.setObjectName("H2Tab2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.H2Tab2)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_7 = QtWidgets.QLabel(self.H2Tab2)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/House2/House 2/map3.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_9.addWidget(self.label_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.H2Tab2, "")
        House2Ui.setCentralWidget(self.centralwidget)

        self.retranslateUi(House2Ui)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.spinBox.valueChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(House2Ui)

    def retranslateUi(self, House2Ui):
        _translate = QtCore.QCoreApplication.translate
        House2Ui.setWindowTitle(_translate("House2Ui", "House 2 Details"))
        self.textBrowser.setHtml(_translate("House2Ui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">Price: P4,922,070/$113,208</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-weight:600;\">3 bedrooms</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-weight:600;\">65m</span><span style=\" font-family:\'Sans Serif\'; font-weight:600; vertical-align:super;\">2</span><span style=\" font-family:\'Sans Serif\'; font-weight:600;\"> floor area</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-weight:600;\">88m</span><span style=\" font-family:\'Sans Serif\'; font-weight:600; vertical-align:super;\">2</span><span style=\" font-family:\'Sans Serif\'; font-weight:600;\"> Land Size</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-weight:600;\">Bellissima Valenza</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">Situated in Santa Rosa City </span><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">- one of the Philippines\' fastest growing cities - surrounded by premium shopping centers and renowned educational institutions, lies Valenza!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; text-decoration: underline;\">Details</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\">  </span><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">  Carport</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">    Swimming pool</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">    Tennis court</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">    Courtyard</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">    Jogging path</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">    Sports facilities</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">    Basketball court</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">    Parks</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">    24-hour security</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">    Clubhouse</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">    Playground</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">    Badminton court</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">    Function area</span></p></body></html>"))
        self.label_5.setText(_translate("House2Ui", "See Photos"))
        self.H2Buy.setText(_translate("House2Ui", "BUY"))
        self.H2Cancel.setText(_translate("House2Ui", "CANCEL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.H2Tab1), _translate("House2Ui", "House Details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.H2Tab2), _translate("House2Ui", "Location"))

import HousePlan
import MainPics

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    House2Ui = QtWidgets.QMainWindow()
    ui = Ui_House2Ui()
    ui.setupUi(House2Ui)
    House2Ui.show()
    sys.exit(app.exec_())

