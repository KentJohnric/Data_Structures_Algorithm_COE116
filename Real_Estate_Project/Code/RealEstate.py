# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RealEstate.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WelcomeForm(object):
    def setupUi(self, WelcomeForm):
        WelcomeForm.setObjectName("WelcomeForm")
        WelcomeForm.resize(450, 450)
        WelcomeForm.setMinimumSize(QtCore.QSize(450, 450))
        WelcomeForm.setMaximumSize(QtCore.QSize(450, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Images/Toma4025-Tea-Tea-plant-leaf.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WelcomeForm.setWindowIcon(icon)
        WelcomeForm.setWindowOpacity(1.0)
        self.label = QtWidgets.QLabel(WelcomeForm)
        self.label.setGeometry(QtCore.QRect(140, 0, 171, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Main/Main/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(WelcomeForm)
        self.frame.setGeometry(QtCore.QRect(10, 350, 431, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(230, 20, 61, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/Main/Main/MapuaLogo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 40, 201, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Main/Main/Lamundi.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(320, 10, 101, 71))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Main/Main/Sponsor.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(WelcomeForm)
        self.frame_2.setGeometry(QtCore.QRect(10, 110, 431, 211))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.WelcomeLabel = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomeLabel.setFont(font)
        self.WelcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeLabel.setObjectName("WelcomeLabel")
        self.gridLayout.addWidget(self.WelcomeLabel, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setStyleSheet("background-color: rgb(249, 249, 249)")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ButtonLoginWelcome = QtWidgets.QPushButton(self.frame_2)
        self.ButtonLoginWelcome.setObjectName("ButtonLoginWelcome")
        self.horizontalLayout.addWidget(self.ButtonLoginWelcome)
        self.ButtonRegisterWelcome = QtWidgets.QPushButton(self.frame_2)
        self.ButtonRegisterWelcome.setObjectName("ButtonRegisterWelcome")
        self.horizontalLayout.addWidget(self.ButtonRegisterWelcome)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(WelcomeForm)
        QtCore.QMetaObject.connectSlotsByName(WelcomeForm)

    def retranslateUi(self, WelcomeForm):
        _translate = QtCore.QCoreApplication.translate
        WelcomeForm.setWindowTitle(_translate("WelcomeForm", "Welcome!"))
        self.label_2.setText(_translate("WelcomeForm", "In Partnership with"))
        self.WelcomeLabel.setText(_translate("WelcomeForm", "Finding your new home? Let\'s make it easy!"))
        self.textBrowser.setHtml(_translate("WelcomeForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF UI Display, serif\'; font-size:12pt; font-weight:600; vertical-align:sub;\">You can find and buy houses or properties without leaving your place. Simply, sit and relax, and find the properties that matches your style! Just Log in to your account and you can simply do what you want with our user-friendly environment. Enjoy!</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SF UI Display, serif\'; font-style:italic; vertical-align:sub;\">Not registered yet? Click the Sign up button below.</span></p></body></html>"))
        self.ButtonLoginWelcome.setText(_translate("WelcomeForm", "Login"))
        self.ButtonRegisterWelcome.setText(_translate("WelcomeForm", "Sign up"))

import MainPics

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomeForm = QtWidgets.QWidget()
    ui = Ui_WelcomeForm()
    ui.setupUi(WelcomeForm)
    WelcomeForm.show()
    sys.exit(app.exec_())

