'I asked Patrick Fisher about the insert negative numbers to use a try/except or if/else. Told me to use an if/else statement otherwise I did the other problems on my own.'
from tkinter import Label, Frame, Entry, Button, END
from tkinter.messagebox import showinfo
from random import randrange
class Game(Frame):
    'Number guessing app'
    def __init__(self,parent=None):
        'constructor'
        Frame.__init__(self,parent)
        self.pack()
        self.count=0
        self.gamescount=0
        self.make_widgets()
    def make_widgets(self):
        'defines Game widgets'
        
        self.lbtotal=Label(self,text='You have made 0 guesses this game. You have completed 0 games')
        self.lbtotal.grid(row=1,column=3) 

        Label(self,text='Enter your guess:').grid(row=2,column=3)

        self.guessEntry=Entry(self,width=15)
        self.guessEntry.grid(row=3,column=3)
        
        self.btn=Button(self,text='Enter',command=lambda:self.reply())
        self.btn.grid(row=4,column=3)
        
    def updateLabel(self):
        'updates the label with game info'
        self.lbtotal.config(text='You have made {} guesses this game. You have completed {} games'.format(self.count,self.gamescount))

    def new_game(self):
        secretnum=randrange(0,10)
        usernum=self.guessEntry.get()

        secretnum=str(secretnum)
        usernum=str(usernum)

        if usernum in secretnum:
            showinfo(title='',message='You got it!\nLets do it again...')
            self.gamescount+=1
        else:
            self.updateLabel()
        
    def reply(self):
        'handles button clicks'
        self.count+=1
        self.new_game()
        self.updateLabel()

Game().mainloop()

from tkinter import Tk,Scale,Label,HORIZONTAL,Entry
from tkinter.messagebox import showinfo
class MortgageCalculator(Tk):
    'Mortgage calculator GUI'
    
    def __init__(self,parent=None):
        'The constructor'
        Tk.__init__(self, parent)
        self.title('Mortgage calculator')
        self.make_widgets()

    def calculateMortgage(self):
        'Calculate monthly payment and show pop-ups'
        p=self.pEntry.get()
        r=self.rEntry.get()
        n=self.nEntry.get()
        
        try:
             p=float(p)
        except:
            showinfo(title='Monthly Payment',message='Error. Incorrect value entered for prinicpal.')
            return
        try:
            r=float(r)
            n=float(n) 
        except:
            showinfo(title='Monthly Payment',message='Error. Incorrect value for intrest.')
            return
        
        top=(p*r/1200)
        bottom=(1-((1+r/1200)**(-12*n)))
        try:
            mortgage=top/bottom
        except:
            showinfo(title='Monthly Payment',message='Error. Unable to calculate payment.')
            return
        showinfo(title='Monthly Payment',message='Your monthly payment is ${:.2f}'.format(mortgage))
        

    def make_widgets(self):
        'Create UI'
        Label(self,text='Principal').grid(row=1,column=0)

        Label(self,text='Intrest Rate').grid(row=2,column=0)

        Label(self,text='Term in Years').grid(row=3,column=0)

        self.pEntry=Entry(self,width=15)
        self.pEntry.grid(row=1,column=3)

        self.rEntry=Entry(self,width=15)
        self.rEntry.grid(row=2,column=3)

        self.nEntry=Entry(self,width=15)
        self.nEntry.grid(row=3,column=3)

        self.btn=Button(self,text='Calculate Payment',command=lambda:self.calculateMortgage())
        self.btn.grid(row=4,column=3)
        
MortgageCalculator().mainloop()

class PositivePriorityQueue(object):
    'Positive Priority queue class'

    def __init__(self):
        'constructor initializes empty priority queue'
        self.queue=[]

    def insert(self, item):
        'inserts item into priority queue'
        if item<0:
            raise Exception ('NegativeNumberError')
        else:
            self.queue.append(item)

    def min(self):
        'returns minimum item in positive priority queue'
        if self.queue==[]:
            return None
        return min(self.queue)

    def removeMin(self):
        'removes minimum item in positive priority queue'
        self.queue.remove(min(self.queue))
        return self.queue
    def removeMax(self):
        'removes maximum item in positive priority queue'
        self.queue.remove(max(self.queue))
        return self.queue

    def __len__(self):
        'returns size of positive priority queue'
        if len(self.queue)==[]:
            return None
        else:
            return len(self.queue)
    def isEmpty(self):
        'checks whether positive priority queue is empty'
        if self.queue==[]:
            return True
        else:
            return False
    def clear(self):
        'remove all items from the queue'
        self.queue.clear()
        
    def __iter__(self):
        'Returns an iterator'
        return iter(self.queue)
