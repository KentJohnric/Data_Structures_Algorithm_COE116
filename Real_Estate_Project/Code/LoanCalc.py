# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoanCalc.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoanCalcUi(object):
    def setupUi(self, LoanCalcUi):
        LoanCalcUi.setObjectName("LoanCalcUi")
        LoanCalcUi.resize(348, 286)
        self.centralwidget = QtWidgets.QWidget(LoanCalcUi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 41, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 151, 31))
        self.label_3.setObjectName("label_3")
        self.DownPayment = QtWidgets.QLineEdit(self.centralwidget)
        self.DownPayment.setGeometry(QtCore.QRect(160, 70, 121, 22))
        self.DownPayment.setObjectName("DownPayment")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(140, 100, 47, 23))
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 100, 81, 21))
        self.label_4.setObjectName("label_4")
        self.CalculateBTN = QtWidgets.QPushButton(self.centralwidget)
        self.CalculateBTN.setGeometry(QtCore.QRect(200, 100, 80, 22))
        self.CalculateBTN.setObjectName("CalculateBTN")
        self.CancelBTN = QtWidgets.QPushButton(self.centralwidget)
        self.CancelBTN.setGeometry(QtCore.QRect(260, 0, 80, 22))
        self.CancelBTN.setObjectName("CancelBTN")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 131, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 131, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 210, 131, 31))
        self.label_7.setObjectName("label_7")
        self.LoanAmount = QtWidgets.QLabel(self.centralwidget)
        self.LoanAmount.setGeometry(QtCore.QRect(150, 150, 550, 31))
        self.LoanAmount.setText("")
        self.LoanAmount.setObjectName("LoanAmount")
        self.Interest = QtWidgets.QLabel(self.centralwidget)
        self.Interest.setGeometry(QtCore.QRect(150, 210, 550, 31))
        self.Interest.setText("")
        self.Interest.setObjectName("Interest")
        self.MonthlyPayment = QtWidgets.QLabel(self.centralwidget)
        self.MonthlyPayment.setGeometry(QtCore.QRect(150, 180, 550, 31))
        self.MonthlyPayment.setText("")
        self.MonthlyPayment.setObjectName("MonthlyPayment")
        LoanCalcUi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoanCalcUi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 22))
        self.menubar.setObjectName("menubar")
        LoanCalcUi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoanCalcUi)
        self.statusbar.setObjectName("statusbar")
        LoanCalcUi.setStatusBar(self.statusbar)

        self.retranslateUi(LoanCalcUi)
        QtCore.QMetaObject.connectSlotsByName(LoanCalcUi)

    def retranslateUi(self, LoanCalcUi):
        _translate = QtCore.QCoreApplication.translate
        LoanCalcUi.setWindowTitle(_translate("LoanCalcUi", "Loan Planner"))
        self.label.setText(_translate("LoanCalcUi", "Price:"))
        self.label_3.setText(_translate("LoanCalcUi", "Enter Downpayment:"))
        self.label_4.setText(_translate("LoanCalcUi", "Years to Pay:"))
        self.CalculateBTN.setText(_translate("LoanCalcUi", "CALCULATE"))
        self.CancelBTN.setText(_translate("LoanCalcUi", "CANCEL"))
        self.label_5.setText(_translate("LoanCalcUi", "LOAN AMOUNT:"))
        self.label_6.setText(_translate("LoanCalcUi", "MONTHLY PAYMENT:"))
        self.label_7.setText(_translate("LoanCalcUi", "INTEREST:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoanCalcUi = QtWidgets.QMainWindow()
    ui = Ui_LoanCalcUi()
    ui.setupUi(LoanCalcUi)
    LoanCalcUi.show()
    sys.exit(app.exec_())

