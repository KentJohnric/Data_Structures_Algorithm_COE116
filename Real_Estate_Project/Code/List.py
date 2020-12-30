# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'List.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ShowData(object):

    def setupUi(self, ShowData):

        ShowData.setObjectName("ShowData")
        ShowData.resize(650, 440)
        ShowData.setMinimumSize(QtCore.QSize(650, 440))
        ShowData.setMaximumSize(QtCore.QSize(650, 440))
        self.gridLayout_2 = QtWidgets.QGridLayout(ShowData)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(ShowData)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(ShowData)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(ShowData)
        QtCore.QMetaObject.connectSlotsByName(ShowData)

    def retranslateUi(self, ShowData):
        _translate = QtCore.QCoreApplication.translate
        ShowData.setWindowTitle(_translate("ShowData", "Show Data"))
        self.label.setText(_translate("ShowData", "Fullname, Phone number, Email, Username and Password are separated by \" -- \"."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShowData = QtWidgets.QWidget()
    ui = Ui_ShowData()
    ui.setupUi(ShowData)
    ShowData.show()
    sys.exit(app.exec_())

