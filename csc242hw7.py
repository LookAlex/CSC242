'I asked Patrick Fisher how split data of the file separating each individual part. Otherwise I did the rest on my own'
def recLessThan(n):
    'create a less than symbol shape'
    if n<=0:
        return
    print(n*' '+'*')
    recLessThan(n-1)
    print(n*' '+'*')
def recHourGlassShape(c,n,i):
    'c is the character to display, n is number of characters on each line and i is indentation'
    if n<=0:
        return
    print(i*' '+n*c)
    recHourGlassShape(c,n-2,i+1)
    print(i*' '+n*c)
  
def recMultiplier(val):
    'Multiply each digit in an integer in the sequence right to left'
    if val<=10:
        return val
    
    return val%10*recMultiplier(val//10)

def recStringCombiner(lst):
    'concatinate all the strings in a list into one string'
    if len(lst) == 0:
        return ''
    else:
        if type(lst[0])==str:
            val=lst[0]
            return val + recStringCombiner(lst[1:])
        else:
            return recStringCombiner(lst[1:])
    
def recNumberCount(lst,n):
    'get a count of with a number in a flat list'
    if len(lst) > 0:
        if type(lst[0]) == list:
            return recNumberCount(lst[0],n) + recNumberCount(lst[1:],n)
        elif type(lst[0]) == int:
            if lst[0] == n:
                return 1 + recNumberCount(lst[1:],n)
            else:
                return recNumberCount(lst[1:],n)
    else:
        return 0
    
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

    def __repr__(self):
        return "Automobile('{}','{}','{}','{}')".format(self.make,self.model,self.year,self.color)

    def __str__(self):
        'get the string representation of the automobile'
        return 'A {}, {}, {} model year {}'.format(self.color,self.make,self.model,self.year)

class AutomobileInventoryManager(object):
    'Class to manage adding / removing inventory from the inventory file'

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
                self.lst.append(Automobile(details[0],details[1],details[2],details[3])))
            return True
        except:
            self.lst.clear()
            return False

    def saveInventory(self):
        'save the inventory to the file and overwrite the old data.'
        try:
            outfile=open(self.filename,'w')
            for items in self.lst:
                outfile.write('{},{},{},{}\n'.format(items.getMake(),items.getModel(),items.getYear(),items.getColor))
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
            self.lst[index]
        else:
            return None

    def __iter__(self):
        'get an iterator to loop through the automobile objects'
        return iter(self.lst)

    def __str__(self):
        'string represention of the inventory'
        return ('There are '+str(len(self.lst))+' automobiles in inventory')



