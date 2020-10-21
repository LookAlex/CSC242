'I asked Patrick Fisher how to set up init and addGorceryItem functions otherwise worked on my own'
#part 1
class GroceryItem(object):
    'Class represented as a Grocery List Item'
    def __init__(self,name=' ',cost=0,count=0,category=' '):
        'Constructor'
        self.name=name
        self.cost=cost
        self.count=count
        self.category=category
    def getName(self):
        'get the name of the item'
        return self.name
    def getCost(self):
        'get the cost of the item'
        return self.cost
    def getCount(self):
        'get the count of the item'
        return self.count
    def getCategory(self):
        'get the category name'
        return self.category
    def multiplyItemCount(self, number):
        'multiple the count of the number of items by the number passed in.Example passing in 2 doubles the count'
        self.count=number*2
        return self.count
    def setCount(self, count):
        'set the exact count of items'
        self.count=count
    def setName(self,name):
        'set the name of the item'
        self.name=name
    def setCost(self,cost):
        'set the count of the item'
        self.cost=cost
    def setCategory(self,category):
        'set the category name'
        self.category=category
    def __str__(self):
        'get the string representation of the item'
        return ('{}:{}:{}:{}').format(self.name,self.cost,self.count,self.category)
    def __repr__(self):
        'get the python representation of the item'
        return ('GroceryItem({},{},{},{})').format(self.name,self.cost,self.count,self.category)    

class GroceryList(object):
    'Class representing a Grocery List Collection'
    #part 2
    def __init__(self):
        'Initalizes an empty grocery list'
        self.list=[]
    def addGroceryItem(self,groceryItem):
        'adds a grocery list item to the collection'
        self.list.append(groceryItem) 
    def getItems(self):
        'gets a list of all the grocery list items'
        item_list=[]
        for line in self.list:
            name=line.__str__()
            item_list.append(name)
        return(item_list)
    def findItemsByCategory(self, category):
        'return a list of all of the grocery items that have a specific category'
        self.category=category
        lst_category=[]
        for item in self.list:
            cat=item.getCategory()
            if cat==category:
                name=item.__str__()
                lst_category.append(name)
            else:
                pass
        return(lst_category)
    def getTotalCost(self):
        'get the total cost of all the items in the list'
        lst_cost=[]
        for item in self.list:
            itemcount=item.getCount()
            itemcost=item.getCost()
            cost=itemcount*itemcost
            lst_cost.append(cost)
        return sum(lst_cost)

    def multiplyAllItemsCount(self,number):
        'increase count of each item in the list by multiple'
        for item in self.list:
            item.multiplyItemCount(number)
        return True

    def multiplyItemCountByCategory(self,category,number):
        'increase count of each item of a specific category in the list by multiple'
        for item in self.list:
            if item.getCategory()==category:
                item.multiplyItemCount(number)
        return True
        
    def __str__(self):
        'get the string representation of the grocery list'
        for item in self.list:
             print(str(item))
        return ''

    #part 3
    def writeListToFile(self,fileName):
        'write the contents of the list to a file'
        try:
            outfile=open(fileName,'w')
            gritems=str(self)
            outfile.write(grItems)
            outfile.close()
            for items in self.list:
                outfile.write(str(items)+'\n')
            outfile.close()
            return True
        except (IOError,FileNotFoundError):
            return False

    def readListFromFile(self,fileName):
        'read the contents of the list from a file'
        try:
            self.list2=[]
            infile=open(fileName,'r')
            contents=infile.readlines()
            for item in contents:
                val=item.strip().split(':')
                self.list2.append(GroceryItem(val[0],float(val[1]),int(val([2]),val[3])))
            infile.close()
            return True
        except Exception as ex:
            print(ex)
            self.list2.clear()
            
            return False

    #part 4
    def __iter__(self):
        'return an iterator'
        return iter(self.list)
    #part 5a
    def __lt__(self,otherGroceryList):
        'returns true if the the cost of the local list is less than the other list'
        if self.getTotalCost()<otherGroceryList.getTotalCost():
            return True
        else:
            return False
    def __gt__(self,otherGroceryList):
        'returns true if the the cost of the local list is greater than the other list'
        if self.getTotalCost()>otherGroceryList.getTotalCost():
            return True
        else:
            return False
    def __eq__(self,otherGroceryList):
        'returns true if the total cost of the grocery list is equal to the other grocery list'
        if self.getCost()==otherGroceryList.getTotalCost():
            return True
        else:
            return False
    #part 5b 
    def __add__(self,otherGroceryList):
        'returns a new grocery list that combines the local list and the other grocery list'
        newlist=[]
        for lst in newlist:
            newlist.append(self)
            newlist.append(otherGroceryList)
            return newlist

    
