



class LoanCalculator:
    
#------------------setters-------------------#
    def setDownPayment(self,downpayment):
        self.downpayment = downpayment

    def setLoanAmount(self,loanamount):
        self.loanamount = loanamount

    def setPrice(self,price):
        self.price = price

    def setMonthlyPayment(self,monthlypayment):
        self.monthlypayment = monthlypayment

    def setYear(self,year):
        self.year = year

    def setInterest(self,interest):
        self.interest = interest
        
#--------------getters----------------------#

    def getDownPayment(self):
        return self.downpayment
    def getYear(self):
        return self.price
    def getLoanAmount(self):
        return self.loanamount
    def getMonthlyPayment(self):
        return self.monthlypayment
    def getInterest(self):
        return self.interest
    
#___________________-Function-___________________#

    def LoanCalc1(self):
        
        self.loanamount = self.price - self.downpayment
        self.monthlypayment = self.loanamount / (self.year * 12)
        self.interest = self.loanamount * (0.01) * (self.year)
        

        
