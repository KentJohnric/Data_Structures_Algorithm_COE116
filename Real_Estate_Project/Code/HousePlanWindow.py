# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HousePlanWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HousePlanWindow(object):
    def setupUi(self, HousePlanWindow):
        HousePlanWindow.setObjectName("HousePlanWindow")
        HousePlanWindow.resize(1190, 638)
        HousePlanWindow.setMinimumSize(QtCore.QSize(1190, 638))
        HousePlanWindow.setMaximumSize(QtCore.QSize(1190, 638))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Pictures/Toma4025-Tea-Tea-plant-leaf.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HousePlanWindow.setWindowIcon(icon)
        HousePlanWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(HousePlanWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.HPtab = QtWidgets.QWidget()
        self.HPtab.setObjectName("HPtab")
        self.label_11 = QtWidgets.QLabel(self.HPtab)
        self.label_11.setGeometry(QtCore.QRect(220, 60, 251, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.textBrowser = QtWidgets.QTextBrowser(self.HPtab)
        self.textBrowser.setGeometry(QtCore.QRect(220, 90, 251, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.HPtab)
        self.label.setGeometry(QtCore.QRect(20, 90, 191, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/House1/House 1/1.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.HPtab)
        self.textBrowser_2.setGeometry(QtCore.QRect(220, 320, 251, 191))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.HPtab)
        self.label_3.setGeometry(QtCore.QRect(20, 320, 191, 191))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/House2/House 2/1.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_12 = QtWidgets.QLabel(self.HPtab)
        self.label_12.setGeometry(QtCore.QRect(220, 290, 251, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.HPtab)
        self.textBrowser_5.setGeometry(QtCore.QRect(900, 90, 251, 191))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_7 = QtWidgets.QLabel(self.HPtab)
        self.label_7.setGeometry(QtCore.QRect(690, 90, 201, 191))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/House3/House 3/1.jpeg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.HPtab)
        self.label_6.setGeometry(QtCore.QRect(900, 60, 251, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(self.HPtab)
        self.layoutWidget.setGeometry(QtCore.QRect(480, 120, 201, 57))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.House1Button = QtWidgets.QPushButton(self.layoutWidget)
        self.House1Button.setObjectName("House1Button")
        self.verticalLayout_3.addWidget(self.House1Button)
        self.layoutWidget1 = QtWidgets.QWidget(self.HPtab)
        self.layoutWidget1.setGeometry(QtCore.QRect(920, 290, 231, 57))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.House3Button = QtWidgets.QPushButton(self.layoutWidget1)
        self.House3Button.setObjectName("House3Button")
        self.verticalLayout_5.addWidget(self.House3Button)
        self.layoutWidget2 = QtWidgets.QWidget(self.HPtab)
        self.layoutWidget2.setGeometry(QtCore.QRect(480, 340, 201, 57))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.House2Button = QtWidgets.QPushButton(self.layoutWidget2)
        self.House2Button.setObjectName("House2Button")
        self.verticalLayout_4.addWidget(self.House2Button)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.label_11.raise_()
        self.textBrowser.raise_()
        self.label.raise_()
        self.textBrowser_2.raise_()
        self.label_3.raise_()
        self.label_12.raise_()
        self.textBrowser_5.raise_()
        self.label_7.raise_()
        self.label_6.raise_()
        self.tabWidget.addTab(self.HPtab, "")
        self.HPtab2 = QtWidgets.QWidget()
        self.HPtab2.setObjectName("HPtab2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.HPtab2)
        self.textBrowser_3.setGeometry(QtCore.QRect(100, 250, 271, 191))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_5 = QtWidgets.QLabel(self.HPtab2)
        self.label_5.setGeometry(QtCore.QRect(120, 40, 221, 181))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/Condo1/Condo1/1.jpeg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.HPtab2)
        self.textBrowser_4.setGeometry(QtCore.QRect(640, 250, 271, 191))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_13 = QtWidgets.QLabel(self.HPtab2)
        self.label_13.setGeometry(QtCore.QRect(660, 40, 221, 181))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/Condo2/Condo2/10.jpeg"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.HPtab2)
        self.label_14.setGeometry(QtCore.QRect(660, 10, 231, 20))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_30 = QtWidgets.QLabel(self.HPtab2)
        self.label_30.setGeometry(QtCore.QRect(120, 10, 221, 20))
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.layoutWidget3 = QtWidgets.QWidget(self.HPtab2)
        self.layoutWidget3.setGeometry(QtCore.QRect(378, 190, 191, 57))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.Condo1Button = QtWidgets.QPushButton(self.layoutWidget3)
        self.Condo1Button.setObjectName("Condo1Button")
        self.verticalLayout.addWidget(self.Condo1Button)
        self.layoutWidget4 = QtWidgets.QWidget(self.HPtab2)
        self.layoutWidget4.setGeometry(QtCore.QRect(928, 190, 201, 57))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.Condo2Button = QtWidgets.QPushButton(self.layoutWidget4)
        self.Condo2Button.setObjectName("Condo2Button")
        self.verticalLayout_2.addWidget(self.Condo2Button)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.textBrowser_3.raise_()
        self.label_5.raise_()
        self.textBrowser_4.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_30.raise_()
        self.tabWidget.addTab(self.HPtab2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.HouseLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.HouseLabel.setFont(font)
        self.HouseLabel.setText("")
        self.HouseLabel.setObjectName("HouseLabel")
        self.horizontalLayout.addWidget(self.HouseLabel)
        self.Logout = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logout.sizePolicy().hasHeightForWidth())
        self.Logout.setSizePolicy(sizePolicy)
        self.Logout.setMinimumSize(QtCore.QSize(24, 24))
        self.Logout.setObjectName("Logout")
        self.horizontalLayout.addWidget(self.Logout)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)
        HousePlanWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HousePlanWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HousePlanWindow)

    def retranslateUi(self, HousePlanWindow):
        _translate = QtCore.QCoreApplication.translate
        HousePlanWindow.setWindowTitle(_translate("HousePlanWindow", "House Plan"))
        self.label_11.setText(_translate("HousePlanWindow", "Price: P10,325 / $237,495"))
        self.textBrowser.setHtml(_translate("HousePlanWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; font-style:italic;\">House and Lot</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">3 bedrooms</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">110m</span><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; vertical-align:super;\">2 </span><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">Floor Area</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">132 m</span><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; vertical-align:super;\">2</span><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"> Land Size</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\"> Balcony</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\"> Maid\'s room</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\"> Swimming pool</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\"> etc.</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("HousePlanWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; font-style:italic;\">House and Lot</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">3 bedrooms</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">65m</span><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; vertical-align:super;\">2</span><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"> floor area</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">88m</span><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; vertical-align:super;\">2</span><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"> Land Size</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">Carport</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">Swimming pool</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">Tennis court</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">etc.</span></p></body></html>"))
        self.label_12.setText(_translate("HousePlanWindow", "Price: P4,922,070 / $113,208"))
        self.textBrowser_5.setHtml(_translate("HousePlanWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; font-style:italic;\">House and Lot</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">8 bedrooms</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">625 m</span><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; vertical-align:super;\">2</span><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"> Floor area</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">835 m</span><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; vertical-align:super;\">2</span><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"> Land Size</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">Pristina North Subdivision </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">Talamban, Cebu City</span></p></body></html>"))
        self.label_6.setText(_translate("HousePlanWindow", "Price: P48,000,000 / $1,104,000"))
        self.label_2.setText(_translate("HousePlanWindow", "Click here for more details"))
        self.House1Button.setText(_translate("HousePlanWindow", "Details"))
        self.label_8.setText(_translate("HousePlanWindow", "Click here for more details"))
        self.House3Button.setText(_translate("HousePlanWindow", "Details"))
        self.label_4.setText(_translate("HousePlanWindow", "Click here for more details"))
        self.House2Button.setText(_translate("HousePlanWindow", "Details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HPtab), _translate("HousePlanWindow", "House and Lot"))
        self.textBrowser_3.setHtml(_translate("HousePlanWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; font-style:italic;\">Condominium:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">3 Bedrooms</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">4 baths</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:600; font-style:italic;\">153 m</span><span style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:600; font-style:italic; vertical-align:super;\">2</span><span style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:600; font-style:italic;\"> floor area</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:10pt; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">Gym</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">Boxing Ring</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">Pilates, Aerobics, Yoga</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">etc.</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("HousePlanWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; font-style:italic;\">Condominium:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">1 bedrooms</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">1 bathrooms</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\">25 m</span><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; vertical-align:super;\">2</span><span style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"> floor area</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">Alarm System</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">Smoke detector</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">Elevators</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:italic;\">etc.</span></p></body></html>"))
        self.label_14.setText(_translate("HousePlanWindow", "Price: P1,250,190 / $28,754"))
        self.label_30.setText(_translate("HousePlanWindow", "Price: P37,053,980 / $852,242"))
        self.label_10.setText(_translate("HousePlanWindow", "Click here for more details"))
        self.Condo1Button.setText(_translate("HousePlanWindow", "Details"))
        self.label_9.setText(_translate("HousePlanWindow", "Click here for more details"))
        self.Condo2Button.setText(_translate("HousePlanWindow", "Details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HPtab2), _translate("HousePlanWindow", "Condominium"))
        self.label_17.setText(_translate("HousePlanWindow", "WELCOME!"))
        self.Logout.setText(_translate("HousePlanWindow", "Click here to Logout"))
        self.label_15.setText(_translate("HousePlanWindow", "Welcome to our main section. This section shows you all the available properties that is currently for sale. You can click on \"Details\" to know more."))

import HousePlan
import MainPics

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HousePlanWindow = QtWidgets.QMainWindow()
    ui = Ui_HousePlanWindow()
    ui.setupUi(HousePlanWindow)
    HousePlanWindow.show()
    sys.exit(app.exec_())

