class BankAccount(object):
    def __init__(self,balance=0):
        self.balance=balance
    def withdraw(self,amount):
        if self.balance<=0:
            return False
        try:
            self.balance-=amount
            return True
        except:
            return False
    def deposit(self,amount):
        try:
            self.balance+=amount
            return True
        except:
            return False
    def getbalance(self):
        return self.balance
    
from tkinter import Tk,Entry,Label,Button,END
from tkinter.messagebox import showinfo
class ATM(Tk):
    def __init__(self,account=BankAccount(),parent=None):
        Tk.__init__(self,parent)
        self.title('ATM')
        self.make_widgets()
        self.account=account
        self.updateBalance()
    def updateBalance(self):
        self.bAmountLb1.config(text=self.account.getbalance())
    def withdraw(self):
        try:
            amount=float(self.withdraw.get())
            
            if self.account.withdraw(amount):
                showinfo(title='Transaction',message='Sucessful withdraw')
            self.withdraw.delete(0,END)
            self.updateBalance()
        except:
            showinfo(title='Transaction',message='Amount entered is not a number')   
    def deposit(self):
        try:
            amount=float(self.aEntry.get())
            
            if self.account.deposit(amount):
                showinfo(title='Transaction',message='Sucessful deposit')
            self.aEntry.delete(0,END)
            self.updateBalance()
        except:
            showinfo(title='Transaction',message='Amount entered is not a number')
            
    def make_widgets(self):
        self.bLB1=Label(self,text='Balance: ')
        self.bLB1.grid(row=1,column=1)
                         
        self.aLB1=Label(self,text='Amount:')
        self.aLB1.grid(row=2,column=1)
                         
        self.bAmountLb1=Label(self)
        self.bAmountLb1.grid(row=1,column=7)
                         
        self.withdraw=Button(self,text='Withdraw',command=lambda:self.withdraw())
        self.withdraw.grid(row=3,column=1)
        
        self.dBtn=Button(self,text='Deposit',command=lambda:self.deposit())
        self.dBtn.grid(row=3,column=7)
        
        self.aEntry=Entry(self,width=5)
        self.aEntry.grid(row=2,column=7)
ATM().mainloop
    
