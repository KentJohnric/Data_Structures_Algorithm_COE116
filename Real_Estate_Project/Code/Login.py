# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(529, 313)
        LoginForm.setMinimumSize(QtCore.QSize(529, 313))
        LoginForm.setMaximumSize(QtCore.QSize(529, 313))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main/Main/Toma4025-Tea-Tea-plant-leaf.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginForm.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(LoginForm)
        self.label.setGeometry(QtCore.QRect(-50, 40, 271, 201))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Main/Main/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(LoginForm)
        self.frame.setGeometry(QtCore.QRect(140, 40, 351, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 71, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LabelUsername = QtWidgets.QLabel(self.layoutWidget)
        self.LabelUsername.setObjectName("LabelUsername")
        self.verticalLayout.addWidget(self.LabelUsername)
        self.LabelPassword = QtWidgets.QLabel(self.layoutWidget)
        self.LabelPassword.setObjectName("LabelPassword")
        self.verticalLayout.addWidget(self.LabelPassword)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 160, 231, 34))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ButtonLogin = QtWidgets.QPushButton(self.layoutWidget1)
        self.ButtonLogin.setObjectName("ButtonLogin")
        self.horizontalLayout.addWidget(self.ButtonLogin)
        self.ButtonCancelLogin = QtWidgets.QPushButton(self.layoutWidget1)
        self.ButtonCancelLogin.setObjectName("ButtonCancelLogin")
        self.horizontalLayout.addWidget(self.ButtonCancelLogin)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(100, 50, 231, 101))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LineEditUsername = QtWidgets.QLineEdit(self.layoutWidget2)
        self.LineEditUsername.setObjectName("LineEditUsername")
        self.verticalLayout_2.addWidget(self.LineEditUsername)
        self.LineEditPassword = QtWidgets.QLineEdit(self.layoutWidget2)
        self.LineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LineEditPassword.setObjectName("LineEditPassword")
        self.verticalLayout_2.addWidget(self.LineEditPassword)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(LoginForm)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 51, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Main/Main/MapuaLogo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.LoginLabel = QtWidgets.QLabel(LoginForm)
        self.LoginLabel.setGeometry(QtCore.QRect(200, 260, 261, 41))
        self.LoginLabel.setStyleSheet("color:rgb(255, 0, 0)")
        self.LoginLabel.setText("")
        self.LoginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LoginLabel.setObjectName("LoginLabel")

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Login"))
        self.LabelUsername.setText(_translate("LoginForm", "Username:"))
        self.LabelPassword.setText(_translate("LoginForm", "Password:"))
        self.ButtonLogin.setText(_translate("LoginForm", "Login"))
        self.ButtonCancelLogin.setText(_translate("LoginForm", "Cancel"))
        self.label_2.setText(_translate("LoginForm", "Login"))

import MainPics

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec_())

