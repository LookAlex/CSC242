#I asked Patrick Fisher about the Parser problem #4 we had the same code besides one line in handle data where he set the occurance to false. 

from tkinter import Button, Entry, Label,Tk
from tkinter.messagebox import showinfo

import random

class ShellGame(object):
    def __init__(self,shellCount=3,winningPiece='X', losingPiece=''):
        'constructor'
        self.shell=shellCount
        self.win=winningPiece
        self.lose=losingPiece
        self.board=[]

                   
    def resetShells(self):
        self.board[random.randrange(0,self.shell)]=self.win
        for i in self.board:
            i=self.lose
            self.board.append(i)
        return self.board
        
    
    def checkWin(self,index):
        if self.win==index:
            return True
        elif index<=0 or index>len(self.shell):
            return False

    def getBoard(self):
        return self.board
        
class ShellGameGUI(Tk):
    'Shell Game GUI'
    def __init__(self,game=ShellGame(),parent=None):
        'constructor'
        Tk.__init__(self,parent)
        self.title('Shell Game')
        self.make_widgets()
        game=ShellGame()

    def first(self):
        if self.label1==True:
            self.label1.config(text='{}'.format(self.win))
            showinfo(title='Shell Game',message='You got it!')
        else:
            showinfo(title='Shell Game', message='Sorry. Wrong Guess')
            self.label1.config(text='{}'.format(game.getlose))
    def second(self):
        if self.label2==True:
            self.label2.config(text='{}'.format(self.win))
            showinfo(title='Shell Game',message='You got it!')
        else:
            showinfo(title='Shell Game', message='Sorry. Wrong Guess')
            self.label2.config(text='{}'.format(game.getlose))
    def third(self):
        if self.label3==True:
            self.label3.config(text='{}'.format(self.win))
            showinfo(title='Shell Game',message='You got it!')
        else:
            showinfo(title='Shell Game',message='Sorry. Wrong Guess')
            self.label3.config(text='{}'.format(game.getlose))
            
    def newgame(self):
        s=ShellGame()
        s.resetShells()
        
    def make_widgets(self):
        Label(self,text='Shell Game').grid(row=0,column=1)
        Button(self,text='Look Under First Shell', command=lambda:self.first()).grid(row=1,column=1)
        Button(self,text='Look Under Second Shell', command=lambda:self.second()).grid(row=1,column=3)
        Button(self,text='Look Under Third Shell', command=lambda:self.third()).grid(row=1,column=5)

        self.label1=Label(self,text='')
        self.label1.grid(row=3,column=1)
        
        self.label2=Label(self,text='')
        self.label2.grid(row=3,column=3)
        
        self.label3=Label(self,text='')
        self.label3.grid(row=3,column=5)
        
        Button(self,text='New Game',command=lambda:self.newgame()).grid(row=5,column=1)
        
        
#ShellGameGUI().mainloop()

def fileNameCount(folder,name):#done
    'recursively runs through files and will add 1 to count if found'
    count=0
    for item in os.listdir(folder):
        n=os.path.join(folder,item)
        if os.path.isdir(n):
            count+=fileNameCount(n,name)
        else:
            if name==item:
                count+=1
    return count

import os
def frequency(folder):
    'a dictionary that totals the counts if specific words are found'
    dictionary={}
    for item in os.listdir(folder):
        itemPath=os.path.join(folder,item)
        if os.path.isdir(n):
            words=findall(pattern,folder)
        for i in words:
            if i in dictionary:
                dictionary[i]+=1
            else:
                dictionary[i]=1
    return dictionary
    
#PAGES TO TEST PARSER WITH
#https://www.cdm.depaul.edu/academics/Pages/Current/Requirements-BS-In-Computer-Science-Software-Development.aspx
#https://www.cdm.depaul.edu/academics/Pages/Current/Requirements-BS-In-Computer-Science-Game-Systems.aspx

#done
from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

def testParser(url):
    content = urlopen(url).read().decode()
    parser = CourseParser()
    parser.feed(content)
    return parser.getData()

class CourseParser(HTMLParser):
    def __init__(self):
        'Takes an empty list and will run through a link and find all the information under the class and CDMExtendedCourseInfo tags and appends to the list the informaiton'
        HTMLParser.__init__(self)
        self.lst=[]
        self.classes=False
        
    def handle_starttag(self,tag,attrs):
        if ('class','CDMExtendedCourseInfo') in attrs:
            self.classes=True
            
    def handle_data(self,data):
        if self.classes==True:
            self.lst.append(data)
        self.classes=False
        
    def getData(self):
        return self.lst

