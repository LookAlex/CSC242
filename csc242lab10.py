import os

def nestingCount(pathname):
    largest=0
    for item in os.listdir(pathname):
        n = os.path.join(pathname, item)
        if os.path.isdir(n):
            depth = nestingCount(n)
            if depth > largest:
                largest = depth
    return 1+largest

from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

class TitleParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.lst=''
        self.foundTag=False
        
    def handle_starttag(self, tag, attrs):
        if tag=='title':
            self.foundTag=True

    def handle_endtag(self, tag):
        if tag=='title':
            self.foundTag=False

    def handle_data(self, data):
        if self.foundTag==True:
            self.lst+=data
            
    def getTitle(self):
        return self.lst

from random import randrange
class Magic8Ball(object):

    def __init__(self, q=[]):
        'the constructor'
        if len(q)==0:
            q.append('It is certain')
            q.append('It is decidedly so')
            q.append('Without a doubt')
            q.append('Yes definitely')
            q.append('You may rely on it')
            q.append('As I see it, yes')
            q.append('Most likely')
            q.append('Outlook good')
            q.append('Yes')
            q.append('Signs point to yes')
            q.append('Reply hazy try again')
            q.append('Ask again later')
            q.append('Better not tell you now')
            q.append('Cannot predict now')
            q.append('Concentrate and ask again')
            q.append("Don't count on it")
            q.append('My reply is no')
            q.append('My sources say no')
            q.append('Outlook not so good')
            q.append('Very doubtful')
        self.q = q
        self.current=randrange(0,len(self.q))

    def shake(self):
        'get the next answer'
        self.current=randrange(0,len(self.q))

    def get(self):
        'get the current answer'
        return self.q[self.current]

    def numAnswers(self):
        'get the number of answers in the ball'
        return len(self.q)

    def __iter__(self):
        'get the iterator'
        return iter(self.q)

    def __str__(self):
        'string representation'
        return 'I am a Magic 8 Ball with {} answers'.format(len(self.q))

from tkinter import Button, Entry, Label,Tk,TOP,LEFT,RIGHT,END
from tkinter.messagebox import showinfo


class BizzaroGUI(Tk):
    'Number guessing app'
    def __init__(self,parent=None):
        'constructor'
        Tk.__init__(self, parent)
        self.title('Bizzaro GUI')
        self.make_widgets()

    def getTitle(self):
        url=self.EntryURL.get()
        content=urlopen(url).read().decode()
        parser=TitleParser()
        parser.feed(content)
        title=parser.getTitle()
        
        showinfo(title='The answer',message='{}'.format(title))

    def getFolderDepth(self):
        filename=self.EntryFolder.get()
        folder=nestingCount(filename)
        showinfo(title='The answer',message='{}'.format(folder))

    def getAnswer(self):
        question=self.EntryQuestion.get()
        m=Magic8Ball()
        m.shake()
        answer=m.get()
        showinfo(title='The answer',message='The answer to your question {} is {}'.format(question,answer))

    def make_widgets(self):
        Label(self,text='Enter URL:').grid(row=0,column=0) 
        Label(self,text='Enter Folder:').grid(row=1,column=0)
        Label(self,text='Ask Question:').grid(row=2,column=0)

        self.EntryURL=Entry(self, text='')
        self.EntryURL.grid(row=0,column=3)

        self.EntryFolder=Entry(self,text='')
        self.EntryFolder.grid(row=1,column=3)

        self.EntryQuestion=Entry(self,text='')
        self.EntryQuestion.grid(row=2,column=3)

        Button(self,text='Get Title',command=lambda:self.getTitle()).grid(row=0,column=5)
        Button(self,text='Get Depth Count',command=lambda:self.getFolderDepth()).grid(row=1,column=5)
        Button(self,text='Get Magic Answer',command=lambda:self.getAnswer()).grid(row=2,column=5)
        

BizzaroGUI().mainloop()
