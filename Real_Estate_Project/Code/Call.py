
from PyQt5 import QtCore, QtGui, QtWidgets
from Admin import Ui_AdminWindow
from C1 import Ui_Condo1Ui
from C2 import Ui_Condo2Ui
from H1 import Ui_House1Ui
from H2 import Ui_House2Ui
from H3 import Ui_House3Ui
from HousePlanWindow import Ui_HousePlanWindow
from Login import Ui_LoginForm
from RealEstate import Ui_WelcomeForm
from SignUp import Ui_SignUpWindow
from UserData import Data
from List import Ui_ShowData
from LoanCalc import  Ui_LoanCalcUi
from LoanPlan import LoanCalculator
class RealEstate:
    # ------------setup Ui--------------------#

    def __init__(self):


        self.WelcomeWindow = QtWidgets.QMainWindow()
        self.WelUi = Ui_WelcomeForm()
        self.WelUi.setupUi(self.WelcomeWindow)

        self.ListWindow = QtWidgets.QMainWindow()
        self.ListUi = Ui_ShowData()
        self.ListUi.setupUi(self.ListWindow)
        self.ListWindow.setCentralWidget(self.ListUi.listWidget)


        self.LoginWindow = QtWidgets.QMainWindow()
        self.LogUi = Ui_LoginForm()
        self.LogUi.setupUi(self.LoginWindow)

        self.SignWindow = QtWidgets.QMainWindow()
        self.SignUi = Ui_SignUpWindow()
        self.SignUi.setupUi(self.SignWindow)

        self.AdminWindow = QtWidgets.QMainWindow()
        self.Adui = Ui_AdminWindow()
        self.Adui.setupUi(self.AdminWindow)

        self.HouseWindow = QtWidgets.QMainWindow()
        self.HouseUi = Ui_HousePlanWindow()
        self.HouseUi.setupUi(self.HouseWindow)

        self.C1window = QtWidgets.QMainWindow()
        self.C1ui = Ui_Condo1Ui()
        self.C1ui.setupUi(self.C1window)

        self.C2window = QtWidgets.QMainWindow()
        self.C2ui =Ui_Condo2Ui()
        self.C2ui.setupUi(self.C2window)

        self.H1window = QtWidgets.QMainWindow()
        self.H1ui = Ui_House1Ui()
        self.H1ui.setupUi(self.H1window)

        self.H2window = QtWidgets.QMainWindow()
        self.H2ui = Ui_House2Ui()
        self.H2ui.setupUi(self.H2window)

        self.H3window = QtWidgets.QMainWindow()
        self.H3ui = Ui_House3Ui()
        self.H3ui.setupUi(self.H3window)

        self.LoanWindow = QtWidgets.QMainWindow()
        self.Loanui = Ui_LoanCalcUi()
        self.Loanui.setupUi(self.LoanWindow)

    #----------------------Functions-----------------

    #-----Signup functions
    def SignUpShow(self):
        self.SignWindow.show()
        self.clearSign()
        self.SignUi.SignUpLabel.clear()
        self.restrictInvalidChar()
        self.WelcomeWindow.setVisible(False)
        self.SignUi.SPB_cancel.clicked.connect(lambda: self.SingUpcancel())
        self.SignUi.SPB_Signup.clicked.connect(lambda: self.signup())

    def clearSign(self):
        self.SignUi.SLE_Fullname.clear()
        self.SignUi.SLE_Phone.clear()
        self.SignUi.SLE_Email.clear()
        self.SignUi.SLE_Username.clear()
        self.SignUi.SLE_Password.clear()


    def restrictInvalidChar(self):
        self.intobj = QtCore.QRegExp("[0-9-+]+")
        self.strobj = QtCore.QRegExp("[a-z-A-Z-0-9-@-.-_]+")

        self.intvalidate = QtGui.QRegExpValidator(self.intobj, self.SignUi.SLE_Phone)
        self.strvalidate = QtGui.QRegExpValidator(self.strobj, self.SignUi.SLE_Email)

        self.SignUi.SLE_Phone.setValidator(self.intvalidate)
        self.SignUi.SLE_Email.setValidator(self.strvalidate)

    def SingUpcancel(self):
        self.SignWindow.close()
        self.WelcomeWindow.setVisible(True)

    def signup(self):


        if self.SignUi.SLE_Fullname.text() == "" or self.SignUi.SLE_Email.text() == "" or self.SignUi.SLE_Phone == "" or self.SignUi.SLE_Username == "" or self.SignUi.SLE_Password == "":
            self.SignUi.SignUpLabel.clear()
            self.SignUi.SignUpLabel.setStyleSheet("color:rgb(255, 0, 0)")
            self.SignUi.SignUpLabel.setText("PLEASE FILL OUT THE FORM COMPLETELY!")
        else:
            self.SignUi.SignUpLabel.clear()
            tempfullname = " ".join(self.SignUi.SLE_Fullname.text().split())
            tempusername = " ".join(self.SignUi.SLE_Username.text().split())
            temppassword = self.SignUi.SLE_Password.text().strip()
            SignObj = Data()
            checkUsername = SignObj.checkUsername(tempusername)

            if checkUsername == True:
                self.SignUi.SignUpLabel.setStyleSheet("color:rgb(255, 0, 0)")
                self.SignUi.SignUpLabel.setText("USERNAME IS ALREADY TAKEN!")
            else:
                SignObj.setFullname(tempfullname)
                SignObj.setPhoneContact(self.SignUi.SLE_Phone.text())
                SignObj.setEmail(self.SignUi.SLE_Email.text())
                SignObj.setUsername(tempusername)
                SignObj.setPassword(temppassword)
                SignObj.Register()
                self.clearSign()
                self.SignUi.SignUpLabel.setStyleSheet("color:rgb(0, 255, 0)")
                self.SignUi.SignUpLabel.setText("ACCOUNT REGISTERED!")


    #-----End of signup functions


    #---Login functions
    def LoginShow(self):
        self.LogUi.LineEditUsername.clear()
        self.LogUi.LineEditPassword.clear()
        self.LoginWindow.show()
        self.LogUi.LoginLabel.clear()
        self.WelcomeWindow.setVisible(False)
        self.LogUi.ButtonCancelLogin.clicked.connect(lambda: self.LoginCancel())
        self.LogUi.ButtonLogin.clicked.connect(lambda:self.Login())

    def LoginCancel(self):
        self.LoginWindow.close()
        self.WelcomeWindow.setVisible(True)

    def Login(self):

        LogObj = Data()
        Check = LogObj.checkLogin(self.LogUi.LineEditUsername.text(),self.LogUi.LineEditPassword.text())

        if Check == True:
            self.name = LogObj.getFullname()
            if self.name == "admin":
                self.LoginWindow.close()
                self.ShowAdmin()
            else:
                self.LoginWindow.close()
                self.HouseWindowshow()

        else:
            self.LogUi.LineEditUsername.clear()
            self.LogUi.LineEditPassword.clear()
            self.LogUi.LoginLabel.setText("USERNAME OR PASSWORD IS INCORRECT!")

    #----End of login functions

    #----admin functions

    def ShowAdmin(self):
        self.clearAdmin()
        self.Adui.Admin_LEusername.clear()
        self.Adui.Delshow.setChecked(False)
        self.Adui.Rshow.setChecked(False)
        self.AdminWindow.show()
        self.Adui.Aenter.clicked.connect(lambda :self.getOrDel())
        self.Adui.ShowList.clicked.connect(lambda : self.lister())
        self.Adui.Logout.clicked.connect(lambda : self.logout())

    def logout(self):
        self.AdminWindow.close()
        self.WelcomeWindow.show()

    def lister(self):
        self.ListUi.listWidget.clear()
        self.ListWindow.show()
        templist = []
        listobj = Data()
        templist = listobj.items()
        self.ListUi.listWidget.addItems(templist)

    def getOrDel(self):

        self.clearAdmin()
        Adobj = Data()

        if self.Adui.Admin_LEusername.text() == "admin" and self.Adui.Delshow.isChecked():
            self.Adui.AdminDNE.setText("DELETION OF ADMIN IS NOT ALLOWED.")
        elif self.Adui.Admin_LEusername.text() == "admin" and self.Adui.Rshow.isChecked():
            self.Adui.AdminDNE.setText("You are the admin!")
        else:
            tempcheck= Adobj.checkUsers(self.Adui.Admin_LEusername.text())

            if tempcheck == True and self.Adui.Rshow.isChecked():
                self.Adui.ALfullname.setText(Adobj.getFullname())
                self.Adui.ALcontact.setText(Adobj.getPhoneContact())
                self.Adui.ALemail.setText(Adobj.getEmail())
                self.Adui.ALuser.setText(Adobj.getUsername())
                self.Adui.ALpassw.setText(Adobj.getPassword())
                self.Adui.Rshow.setChecked(False)

            elif tempcheck == True and self.Adui.Delshow.isChecked():
                Adobj.Deluser(self.Adui.Admin_LEusername.text())
                self.Adui.Delshow.setChecked(False)
                self.Adui.AdminDNE.setText("Account Deleted.")

            elif tempcheck == False:
                self.Adui.AdminDNE.setText("NO USER FOUND!")

    def clearAdmin(self):
        self.Adui.ALfullname.clear()
        self.Adui.ALcontact.clear()
        self.Adui.ALemail.clear()
        self.Adui.ALuser.clear()
        self.Adui.ALpassw.clear()
        self.Adui.AdminDNE.clear()







    #---HouseWindow
    def HouseWindowshow(self):
        self.HouseWindow.show()
        self.HouseUi.HouseLabel.setText(self.name)
        self.HouseUi.House1Button.clicked.connect(lambda: self.House1Show())
        self.HouseUi.House2Button.clicked.connect(lambda: self.House2Show())
        self.HouseUi.House3Button.clicked.connect(lambda: self.House3Show())
        self.HouseUi.Condo1Button.clicked.connect(lambda: self.Condo1Show())
        self.HouseUi.Condo2Button.clicked.connect(lambda: self.Condo2show())
        self.H1ui.H1Cancel.clicked.connect(lambda:self.closeH1())
        self.H2ui.H2Cancel.clicked.connect(lambda: self.closeH2())
        self.H3ui.H3Cancel.clicked.connect(lambda: self.closeH3())
        self.C1ui.C1Cancel.clicked.connect(lambda: self.closeC1())
        self.C2ui.C2Cancel.clicked.connect(lambda: self.closeC2())
        self.HouseUi.Logout.clicked.connect(lambda: self.HouseLogout())

        self.H1ui.H1Buy.clicked.connect(lambda: self.showH1calc())
        self.H2ui.H2Buy.clicked.connect(lambda: self.showH2calc())
        self.H3ui.H3Buy.clicked.connect(lambda: self.showH3calc())
        self.C1ui.C1Buy.clicked.connect(lambda: self.showC1calc())
        self.C2ui.C2Buy.clicked.connect(lambda: self.showC2calc())

    def showH1calc(self):
        self.LoanWindow.show()
        self.Loanui.label_2.setText("10,326,860")
        self.Loanui.CalculateBTN.clicked.connect(lambda: self.H1calc())
        self.Loanui.CancelBTN.clicked.connect(lambda: self.CloseCalc())

    def CloseCalc(self):
        self.LoanWindow.close()


    def showH2calc(self):
        self.LoanWindow.show()
        self.Loanui.label_2.setText("4,922,070")
        self.Loanui.CalculateBTN.clicked.connect(lambda: self.H2calc())
        self.Loanui.CancelBTN.clicked.connect(lambda: self.CloseCalc())
    def showH3calc(self):
        self.LoanWindow.show()
        self.Loanui.label_2.setText("48,000,000")
        self.Loanui.CalculateBTN.clicked.connect(lambda: self.H3calc())
        self.Loanui.CancelBTN.clicked.connect(lambda: self.CloseCalc())
    def showC1calc(self):
        self.LoanWindow.show()
        self.Loanui.label_2.setText("37,053,980")
        self.Loanui.CalculateBTN.clicked.connect(lambda: self.C1calc())
        self.Loanui.CancelBTN.clicked.connect(lambda: self.CloseCalc())
    def showC2calc(self):
        self.LoanWindow.show()
        self.Loanui.label_2.setText("1,250,190")
        self.Loanui.CalculateBTN.clicked.connect(lambda: self.C2calc())
        self.Loanui.CancelBTN.clicked.connect(lambda: self.CloseCalc())

    def H1calc(self):
        hobj = LoanCalculator()
        hobj.setDownPayment(float(self.Loanui.DownPayment.text()))
        hobj.setPrice(10326860)
        hobj.setYear(self.Loanui.spinBox.value())
        hobj.LoanCalc1()
        self.Loanui.LoanAmount.setText("{0:.2f}".format(round(hobj.getLoanAmount(),2)))
        self.Loanui.MonthlyPayment.setText("{0:.2f}".format(round(hobj.getMonthlyPayment(),2)))
        self.Loanui.Interest.setText("{0:.2f}".format(round(hobj.getInterest(),2)))

    def H2calc(self):
        hobj = LoanCalculator()
        hobj.setDownPayment(float(self.Loanui.DownPayment.text()))
        hobj.setPrice(4922070)
        hobj.setYear(self.Loanui.spinBox.value())
        hobj.LoanCalc1()
        self.Loanui.LoanAmount.setText("{0:.2f}".format(round(hobj.getLoanAmount(), 2)))
        self.Loanui.MonthlyPayment.setText("{0:.2f}".format(round(hobj.getMonthlyPayment(), 2)))
        self.Loanui.Interest.setText("{0:.2f}".format(round(hobj.getInterest(), 2)))

    def H3calc(self):
        hobj = LoanCalculator()
        hobj.setDownPayment(float(self.Loanui.DownPayment.text()))
        hobj.setPrice(48000000)
        hobj.setYear(self.Loanui.spinBox.value())
        hobj.LoanCalc1()
        self.Loanui.LoanAmount.setText("{0:.2f}".format(round(hobj.getLoanAmount(), 2)))
        self.Loanui.MonthlyPayment.setText("{0:.2f}".format(round(hobj.getMonthlyPayment(), 2)))
        self.Loanui.Interest.setText("{0:.2f}".format(round(hobj.getInterest(), 2)))

    def C1calc(self):
        cobj = LoanCalculator()
        cobj.setDownPayment(float(self.Loanui.DownPayment.text()))
        cobj.setPrice(37053980)
        cobj.setYear(self.Loanui.spinBox.value())
        cobj.LoanCalc1()
        self.Loanui.LoanAmount.setText("{0:.2f}".format(round(cobj.getLoanAmount(), 2)))
        self.Loanui.MonthlyPayment.setText("{0:.2f}".format(round(cobj.getMonthlyPayment(), 2)))
        self.Loanui.Interest.setText("{0:.2f}".format(round(cobj.getInterest(), 2)))

    def C2calc(self):
        cobj = LoanCalculator()
        cobj.setDownPayment(float(self.Loanui.DownPayment.text()))
        cobj.setPrice(1250190)
        cobj.setYear(self.Loanui.spinBox.value())
        cobj.LoanCalc1()
        self.Loanui.LoanAmount.setText("{0:.2f}".format(round(cobj.getLoanAmount(), 2)))
        self.Loanui.MonthlyPayment.setText("{0:.2f}".format(round(cobj.getMonthlyPayment(), 2)))
        self.Loanui.Interest.setText("{0:.2f}".format(round(cobj.getInterest(), 2)))

    def HouseLogout(self):
        self.HouseWindow.close()
        self.WelcomeWindow.show()

    def House1Show(self):
        self.HouseWindow.setVisible(False)
        self.H1window.show()

    def House2Show(self):
        self.HouseWindow.setVisible(False)
        self.H2window.show()

    def House3Show(self):
        self.HouseWindow.setVisible(False)
        self.H3window.show()

    def Condo1Show(self):
        self.HouseWindow.setVisible(False)
        self.C1window.show()

    def Condo2show(self):
        self.HouseWindow.setVisible(False)
        self.C2window.show()

    def closeH1(self):
        self.HouseWindow.setVisible(True)
        self.H1window.close()
    def closeH2(self):
        self.HouseWindow.setVisible(True)
        self.H2window.close()
    def closeH3(self):
        self.HouseWindow.setVisible(True)
        self.H3window.close()
    def closeC1(self):
        self.HouseWindow.setVisible(True)
        self.C1window.close()
    def closeC2(self):
        self.HouseWindow.setVisible(True)
        self.C2window.close()
        my = QtGui.QCloseEvent()

    #--End of HouseWindow Functions





    #------------------Start events------------------
    def welcomeWindow(self):
        self.WelcomeWindow.show()
        self.WelUi.ButtonRegisterWelcome.clicked.connect(lambda:self.SignUpShow())
        self.WelUi.ButtonLoginWelcome.clicked.connect(lambda:self.LoginShow())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = RealEstate()
    ui.welcomeWindow()
    sys.exit(app.exec_())