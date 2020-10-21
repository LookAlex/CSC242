'I asked Patrick Fisher about how to set up the init and weirdstring class'
class NoVowelIter(object):
    def __init__(self,string):
        'constructor'
        self.string=string
        self.index=0
        
    def __next__(self):
        while True:
            if self.index>=len(self.string):
                raise StopIteration()
            if self.string[self.index] not in 'aeiouAEIOU':
                val=self.string[self.index]
                self.index+=1
                break
            else:
                self.index+=1
        return val
        
class WeirdString(str):
    def __iter__(self):
        return NoVowelIter(self)
    
#need more imports
from tkinter import Tk,Scale,Label,HORIZONTAL
class MortgageCalcSlider(Tk):

    def __init__(self,parent=None):
        Tk.__init__(self,parent)
        self.title('Mortage Calculator')
        self.make_widgets()
        
    def updateValues(self,event):
        p=self.sliderP.get()
        n=self.sliderN.get()
        r=self.sliderR.get()
        try:
            top=(p*r/1200)
            bottom=(1-((1+r/1200)**(-12*n)))
            mortgage=top/bottom
            self.lbamount.config(text='${:,.2f}'.format(mortgage))
        except Exception as e:
            self.lbamount.config(text='Unable to calculate with current values'.format(e))
    def make_widgets(self):
        Label(self,text='Mortgage Calculator Slider').grid(row=0,column=1)
        
        Label(self,text='Principal:').grid(row=1,column=0)
        self.sliderP=Scale(self,from_=0,to=1000000,orient=HORIZONTAL,command=self.updateValues)
        self.sliderP.grid(row=1,column=1)
        
        Label(self,text='Years:').grid(row=2,column=0)
        self.sliderN=Scale(self,from_=0,to=30,orient=HORIZONTAL,command=self.updateValues)
        self.sliderN.grid(row=2,column=1)
        
        Label(self,text='Intrest:').grid(row=3,column=0)
        self.sliderR=Scale(self,from_=0,to=10,orient=HORIZONTAL,command=self.updateValues)
        self.sliderR.grid(row=3,column=1)
        
        
        self.lbamount=Label(self,text='')
        self.lbamount.grid(row=4,column=1)
    

#MortgageCalcSlider().mainloop()


#Simplified BIM Calculation: BMI = (Weight in Pounds / (Height in inches x Height in inches)) x 703
from tkinter import Tk,Scale,Label,HORIZONTAL,Button,Entry
from tkinter.messagebox import showinfo
class BMIGUI(Tk):
    def __init__(self,parent=None):
        'constructor'
        Tk.__init__(self,parent)
        self.title('BMI Calculator')
        self.make_widgets()
        

    def getBMIDescription(self,value):
        if value<18.5:
            return 'Underweight'
        elif value==18.5 and value<25:
            return'Normal Weight'
        elif value==25 and value<30:
            return 'Overweight'
        else:
            return 'Obese'
    def calculateBMI(self):
        hf=self.heightfeet.get()
        hi=self.heightinches.get()
        weight=self.slider.get()
        try:
            hf=float(hf)
        except ValueError:
            showinfo(title='BMI Calculation', message='Error. Incorrect value entered for height(feet).')
            return
        try:
            hi=float(hi)
        except ValueError:
            showinfo(title='BMI Calculation',message='Error. Incorrect value entered for height(inches).')
            return
        heightinches=(hf*12)+hi
        bmi=(weight/(heightinches*heightinches))*703
        self.lbupdater.config(text='{:.2f} {{}}'.format(bmi,self.getBMIDescription(bmi)))

        
    def make_widgets(self):
        Label(self,text='Body Mass Index Calculator').grid(row=0,column=0)
        
        Label(self,text='Your Height:').grid(row=1,column=0)
        
        Label(self,text='Your Weight:').grid(row=2,column=0)
        
        Label(self,text='BMI:').grid(row=5,column=0)
        
        Label(self,text='Pounds').grid(row=2,column=2)
        
        Label(self,text='Feet').grid(row=1,column=2)
        
        Label(self,text='Inches').grid(row=1,column=4)
        
        self.lbupdater=Label(self)
        self.lbupdater.grid(row=5,column=1)
        
        self.calcBTN=Button(self,text='Calculate BMI', command=lambda:self.calculateBMI())
        self.calcBTN.grid(row=4,column=1)
        
        self.slider=Scale(self,from_=0,to=500,orient=HORIZONTAL,resolution=10)
        self.slider.grid(row=2,column=1)
        
        self.heightfeet=Entry(self,width=5)
        self.heightfeet.grid(row=1,column=1)
        
        self.heightinches=Entry(self,width=5)
        self.heightinches.grid(row=1,column=3)
        
    
#BMIGUI().mainloop()
