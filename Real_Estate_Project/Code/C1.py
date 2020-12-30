# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Condo1Ui(object):
    def setupUi(self, Condo1Ui):
        Condo1Ui.setObjectName("Condo1Ui")
        Condo1Ui.resize(950, 542)
        Condo1Ui.setMinimumSize(QtCore.QSize(950, 542))
        Condo1Ui.setMaximumSize(QtCore.QSize(950, 542))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main/Main/Toma4025-Tea-Tea-plant-leaf.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Condo1Ui.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Condo1Ui)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(9, 9, 931, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.C1Tab1 = QtWidgets.QWidget()
        self.C1Tab1.setObjectName("C1Tab1")
        self.textBrowser = QtWidgets.QTextBrowser(self.C1Tab1)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 491, 451))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox = QtWidgets.QGroupBox(self.C1Tab1)
        self.groupBox.setGeometry(QtCore.QRect(490, -10, 431, 481))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/Condo1/Condo1/1.jpeg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.widget)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.page_6)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/Condo1/Condo1/3.jpeg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.page_5)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Condo1/Condo1/2.jpeg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.gridLayout_8.addWidget(self.stackedWidget, 2, 0, 1, 1)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.C1Buy = QtWidgets.QPushButton(self.groupBox)
        self.C1Buy.setObjectName("C1Buy")
        self.horizontalLayout.addWidget(self.C1Buy)
        self.C1Cancel = QtWidgets.QPushButton(self.groupBox)
        self.C1Cancel.setObjectName("C1Cancel")
        self.horizontalLayout.addWidget(self.C1Cancel)
        self.gridLayout_8.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(3)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_8.addWidget(self.spinBox, 1, 0, 1, 1)
        self.tabWidget.addTab(self.C1Tab1, "")
        self.C1Tab2 = QtWidgets.QWidget()
        self.C1Tab2.setObjectName("C1Tab2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.C1Tab2)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_7 = QtWidgets.QLabel(self.C1Tab2)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/Condo1/Condo1/map.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_9.addWidget(self.label_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.C1Tab2, "")
        Condo1Ui.setCentralWidget(self.centralwidget)

        self.retranslateUi(Condo1Ui)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.spinBox.valueChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(Condo1Ui)

    def retranslateUi(self, Condo1Ui):
        _translate = QtCore.QCoreApplication.translate
        Condo1Ui.setWindowTitle(_translate("Condo1Ui", "Condo 1 Details"))
        self.textBrowser.setHtml(_translate("Condo1Ui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">Price: P37,053,980/$852,242</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-weight:600;\">3 Bedrooms</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-weight:600;\">4 baths</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-weight:600;\">153 m</span><span style=\" font-family:\'Sans Serif\'; font-weight:600; vertical-align:super;\">2 </span><span style=\" font-family:\'Sans Serif\'; font-weight:600;\">floor area</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">Alphaland Corporation, </span><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">the developer of Balesin Island Club, brings you Makati Place.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:12pt; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Details</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\">  </span><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">Gym</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">  Boxing Ring</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">  Pilates, Aerobics, Yoga and Dance Studios</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">  Covered Tennis Court</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">  Covered Badminton Courts</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">  Covered Basketball Court</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">  Squash Court</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">  Table Tennis Room</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">  High Definition Virtual Golf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-style:italic;\">  Spaces For Entertainment And Dining</span></p></body></html>"))
        self.label_5.setText(_translate("Condo1Ui", "See Photos"))
        self.C1Buy.setText(_translate("Condo1Ui", "BUY"))
        self.C1Cancel.setText(_translate("Condo1Ui", "CANCEL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.C1Tab1), _translate("Condo1Ui", "House Details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.C1Tab2), _translate("Condo1Ui", "Location"))

import HousePlan
import MainPics

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Condo1Ui = QtWidgets.QMainWindow()
    ui = Ui_Condo1Ui()
    ui.setupUi(Condo1Ui)
    Condo1Ui.show()
    sys.exit(app.exec_())

