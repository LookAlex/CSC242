#I asked Patrick Fisher how to format the configures other wise worked alone
def recNestedListSum(lst):
    if lst==[]:
        return 0
    if type(lst[0])==float or type(lst[0])==int:
        return recNestedListSum(lst[0])+recNestedListSum(lst[1:])
    if type(lst[0])==list:
        return recNestedListSum(lst[0])+recNestedListSum(lst[1:])
    else:
        return recNestedListSum(lst[1:])
    
def recWordCount(lst,word):
    'returns a count of how many times a word is found in the strings in a list. Case should be ignored'
    if len(lst)==0:
        return 0
    if type(lst[0])==str:
        count=0
        lword=word.lower()
        wordinstring=lst[0].split()
        if len(wordinstring)>1:
            count=count+recWordCount(lst[1:],word)
        else:
            if lword==wordinstring[0].lower():
                count+=1
        return count+recWordCount(lst[1:],word)

    elif type(lst[0])==list:
        return recWordCount(lst[0],word)+recWordCount(lst[1:],word)
    else:
        return recWordCount(lst[1:],word)
    
import os

def dirPrint(pathname, indent):
    '''recursively scans all files contained, directly or
       indirectly, in the folder pathname'''
    for item in os.listdir(pathname):  
        n = os.path.join(pathname,item)
        if os.path.isdir(n):
            print(' '*indent+n)
            dirPrint(n,indent+2)
        else:
            print(' '*indent+n)

import os

def fileCount(pathname, fileName):
    count=0
    for item in os.listdir(pathname):
        n=os.path.join(pathname,item)
        if os.path.isdir(n):
            count+=fileCount(n,fileName)
        else:
            if fileName==item:
                count+=1
    return count

from tkinter import Button,Entry,Label,Tk,TOP,LEFT,RIGHT,END,filedialog
from tkinter.messagebox import showinfo

class FileCountExplorer(Tk):

    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('File Count Explorer')
        self.make_widgets()

    def getPath(self):       
        path = filedialog.askdirectory(parent=self,initialdir="/",title='Please select a directory')
        self.dirPath.delete(0,END)
        self.dirPath.insert()  
    def getCount(self):
        
        filename=self.fEntry.get()
        path=self.pEntry.get()
        
        if path=='':
            showinfo(title='Error',message='You must select a folder path.')
        if filename=='':
            showinfo(title='Error',message='You must enter a filename.')
        else:
            path = self.dirpath.get()
            filename=self.filenEntry.get()
            count=self.fileCount(path,filename)
            showinfo(title='Total Files Found', message='{}'.format(count))

    def fileCount(self,pathname, fileName):
        count=0
        for item in os.listdir(pathname):
            n=os.path.join(pathname,item)
            if os.path.isdir(n):
                count+=self.fileCount(n,fileName)
            else:
                if fileName==item:
                    count+=1
        return count

    def make_widgets(self):
        Label(self,text='Enter a file name:').grid(row=1,column=0)
        Label(self,text='Select path:').grid(row=2,column=0)

        self.fEntry=Entry(self,width=40)
        self.fEntry.grid(row=1,column=3)

        self.pEntry=Entry(self,width=40)
        self.pEntry.grid(row=2,column=3)

        self.pbtn=Button(self,text='Get Path',command=lambda:self.getPath())
        self.pbtn.grid(row=2,column=5)

        self.cbtn=Button(self,text='Get Count',command=lambda:self.getCount())
        self.cbtn.grid(row=3,column=5)
        
    
#FileCountExplorer().mainloop()

class Automobile(object):
    'Automobile class. Only way to initialize values is through the constructor'
    def __init__(self,make='Unknown', model='Unknown',year='1900',color='Unknown'):
        'Constructor'
        self.make=make
        self.color=color
        self.year=year
        self.model=model

    def getMake(self):
        'Get the Make of the Car'
        return self.make

    def getColor(self):
        'Get the color of the car'
        return self.color

    def getYear(self):
        'Get the year of the car'
        return self.year

    def getModel(self):
        'get the model of the car'
        return self.model

    def __str__(self):
        'get the string representation of the automobile'
        return 'A {}, {}, {} model year {}'.format(self.color,self.make,self.model,self.year)

class AutomobileInventoryManager(object):
    'Class to manage adding / removing inventory from the inventory file'
    #use your version from assignment 7.
    # you can use the solution I showed in class
    def __init__(self, filename='inventory.txt'):
        'Initialize the Inventory Manager'
        self.filename=filename
        self.lst=[]
    
    def loadInventory(self):
        'load cars from the inventory file'
        try:
            self.lst.clear()
            infile=open(self.filename,'r')
            contents=infile.readlines()
            infile.close()
            for line in contents:
                details=line.strip().split(',')
                self.lst.append(Automobile(details[0],details[1],details[2],details[3]))
            return True
        except:
            self.lst.clear()
            return False

    def saveInventory(self):
        'save the inventory to the file and overwrite the old data.'
        try:
            outfile=open(self.filename,'w')
            for items in self.lst:
                outfile.write('{},{},{},{}\n'.format(itemsgetMake(),items.getModel(),items.getYear(),items.getColor()))
            outfile.close()
            return True
        except:
            return False

    def addInventory(self,auto):
        'add a new auto to inventory'
        self.lst.append(auto)

    def removeInventory(self,index):
        'remove inventory from the internal collection'
        if index>=0 and index<len(self.lst):
            self.lst.pop(index)
        try:
            self.lst.pop(index)
            return True
        except:
            return False

    def __len__(self):
        'get the count of cars in inventory'
        return len(self.lst)

    def __contains__(self, make):
        'true to if a make of car in inventory'
        for i in self.lst:
            if i.getMake() == make:
                return True
        return False
            

    def __getitem__(self,index):
        'get an automobile from inventory'
        if index>=0 and index<len(self.lst):
            return self.lst[index]
        else:
            return None

    def __iter__(self):
        'get an iterator to loop through the automobile objects'
        return iter(self.lst)

    def __str__(self):
        'string represention of the inventory'
        return ('There are '+str(len(self.lst))+' automobiles in inventory')

from tkinter import Label, Tk, Entry, Button, END
from tkinter.messagebox import showinfo

class AIMGUI(Tk):
    'Inventory Manager GUI'
    
    def __init__(self,im,parent=None):
        'constructor'
        Tk.__init__(self, parent)
        self.title('Dewey, Cheatem & Howe Motors Inventory')
        self.im=AutomobileInventoryManager()
        self.current=1
        self.make_widgets()
        self.updateUI()
        

    def updateUI(self):
        'updates modt UI elements after interaction with the GUI'
        self.labelcar.configure(text='Viewing automobile {} of {}'.format(self.current,self.current))
        self.labeldetail.configure(text='A {},{},{}, model year {}'.format(getMake(),getModel(),getYear(),getColor()))
        
    def previous(self):
        'View the previous car in inventory'
        if self.current <0:
            showinfo(title='Inventory',message='You are at the beginning of the list')
        else:
            self.current-=1
            self.updateUI()
            

    def next(self):
        'view the next car in inventory'
        if self.current>len(self.im):
            showinfo(title='Inventory',message='You are at the end of the list')
        else:
            self.current+=1
            self.updateUI()

    def remove(self):
        'remove a car from inventory'
        self.im.removeInvenotry(im)
        self.updateUI()
        showinfo(title='Inventory',message='Car removed. Moving to the front of the list')

    def addCar(self):
        'add a automobile to inventory'
        color=self.colorEntry.get()
        model=self.modelEntry.get()
        make=self.makeEntry.get()
        year=self.yearEntry.get()

        if make=='':
            showinfo(title='Manager',message='Make Required')
        if model=='':
            showinfo(title='Manager',message='Model Required')
        if year=='':
            showinfo(title='Manager',message='Year Required')
        if color=='':
            showinfo(title='Manager',message='Color Required')
        self.im.addInventory(Automobile(self.Make.get(),self.Model.get(),self.Year.get(),self.Color.get()))
        self.updateUI()

    def saveFile(self):
        'save inventory to the file'
        try:
            outfile=open('inventory.txt','a')
            outfile.write('{},{},{},{}\n'.format(make,model,year,color))
            outfile.close()
            showinfo(title='Manager',message='Inventory Saved')
        except:
            showinfo(title='Manager',message='Sorry. The inventory was not saved')
        self.im.saveInventotry()
        self.updateUI()
        
    def make_widgets(self):
        'add widgets to the UI'
        Label(self, text='Dewey, Cheatem & Howe Motors Inventory').grid(row=0,column=3)
        Label(self, text='Make:').grid(row=4,column=0)
        Label(self,text='Model:').grid(row=5,column=0)
        Label(self,text='Year:').grid(row=6,column=0)
        Label(self,text='Color:').grid(row=7,column=0)

        self.makeEntry=Entry(self,width=30)
        self.makeEntry.grid(row=4,column=3)

        self.modelEntry=Entry(self,width=30)
        self.modelEntry.grid(row=5,column=3)

        self.yearEntry=Entry(self,width=30)
        self.yearEntry.grid(row=6,column=3)

        self.colorEntry=Entry(self,width=30)
        self.colorEntry.grid(row=7,column=3)

        self.btnp=Button(self,text='< Previous',command=lambda:self.previous())
        self.btnp.grid(row=3, column=0)

        self.btnn=Button(self,text='Next >',command=lambda:self.next())
        self.btnn.grid(row=3, column=8)

        self.btnr=Button(self,text='REMOVE',command=lambda:self.remove())
        self.btnr.grid(row=3, column=9)

        self.btna=Button(self,text='Add New Car',command=lambda:self.addCar())
        self.btna.grid(row=8, column=0)

        self.btns=Button(self,text='Save to File',command=lambda:self.saveFile())
        self.btns.grid(row=9, column=0)
        
        self.labelcar=Label(self)
        self.labelcar.grid(row=2, column=3)

        self.labeldetail=Label(self)
        self.labeldetail.grid(row=3,column=3)
        
#a=AutomobileInventoryManager()
#AIMGUI(a).mainloop()
                               
#print(recNestedListSum([[1,2,3]]))
#print(recNestedListSum([[[[[[[[[5]]]]]]]]]))
#print(recNestedListSum([[1,2,3],[4,[[[5]]]]]))

#print(recWordCount([],'a'))
#print(recWordCount([1,'a',3,4,5],'a'))
#print(recWordCount([[[[[[1,'test test']],3]]],[['test',5.0,'test test']]],'test'))

#dirPrint('Test',2)
#dirPrint('count',5)

#print('FILE COUNT: ', fileCount('Test','a.txt'))
#print('FILE COUNT: ', fileCount('Test','File.txt'))
#print('FILE COUNT: ', fileCount('Test','file.txt'))

###EXAMPLE############

class FileDialogExample(Tk):
    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('FileDialog Example')
        self.make_widgets()
    def getPath(self):
        path = filedialog.askdirectory(parent=self,initialdir="/",title='Please select a directory')
        print(path)
        
    def make_widgets(self):
        Button(self, text="Print Path", command=lambda:self.getPath()).grid(column=0,row=0)

#FileDialogExample().mainloop()
####END EXAMPLE########
