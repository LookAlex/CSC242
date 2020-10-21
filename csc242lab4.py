from tkinter import Label,Tk
class Sign(Tk):
    def __init__(self,lines=['default'],parent=None):
        Tk.__init__(self,parent)
        self.title('Warning')
        self.make_widgets(lines)
        
    def make_widgets(self,lines):
        if lines==['default']:
            self.widget1=Label(self,text='GREAT DEAL!')
            self.widget2=Label(self,text='Android 1.0 Phones for $10!')
            self.widget3=Label(self,text='Security vulnerabilities included!')
            self.widget1.pack()
            self.widget2.pack()
            self.widget3.pack()
        else:
            self.make_widgets(self,[1])
            self.make_widgets(self,[2])
            self.make_widgets(self,[3])
        pass

Sign().mainloop()

