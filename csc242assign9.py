#I asked Patrick Fisher strip the data and get rid of the href I had in the testHParser. otherwise worked alone
import os

def findAllDirectories(root,dirName):
    """Takes a filename and will find the occurences of the name specified"""
    for item in os.listdir(root):  
        n = os.path.join(root,item)
        print(n)
        if os.path.isdir(n):
            a=findAllDirectories(dirName,n)
        elif os.path.isfile(n):
            if item.lower()==fname.lower():
                b=findAllDirectories(dirName,n)
        else:
            return findAllDirectories(dirName,n)

            
def crawl(filename,indent):
    """Takes a file and reads the lines. Will recursivly run through the remaining files to find it's children then move onto the next file"""
    try:
        infile=open(filename,'r')
        contents=infile.read()
        print(' '*indent+'Entering {}'.format(filename))
        for items in contents:
            item=open(filename,'r')
            items=item.readlines()
            crawl(items,indent+4)
        infile.close()
        print(' '*indent+'Entering {}'.format(items))
    except:
        print(' '*indent+'File not found: {}'.format(filename))


def nestingCount(pathname):
    """Recusivly returns a count of files that pertain to the folder"""
    count=1
    for item in os.listdir(pathname):
        itemPath=os.path.join(pathname,item)
        if os.path.isdir(itemPath):
            val=nestingCount(itemPath)+1
            if val>count:
                count=val
    return count
    
from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

def testParser(url):
    content = urlopen(url).read().decode()
    parser = AnchorParser()
    parser.feed(content)
    return parser.getLabels()

class AnchorParser(HTMLParser):
    def __init__(self):
        """Will go through and find instances of a and href in the html"""
        HTMLParser.__init__(self)
        self.lst=[]
        self.foundPTag=False
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.foundPTag=True

    def handle_endtag(self, tag):
        if tag == 'a':
            self.foundPTag=False
            
    def handle_data(self, data):
        if self.foundPTag==True:
            data.strip('')
            data.strip("\r")
            data.strip("\n")
            data.strip('\r\n')
            data.strip('\r\n\r\n')
            data.strip('\r\n ')
            self.lst.append(data)
        
    def getLabels(self):
        return self.lst

def testHParser(url):
    content = urlopen(url).read().decode()
    parser = HeaderParser()
    parser.feed(content)
    return parser.getHeadings()

class HeaderParser(HTMLParser):
    def __init__(self):
        """Will go throguh and find the instances of li in the html"""
        HTMLParser.__init__(self)
        self.lst=[]
        self.foundPTag=False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'li':
            self.foundPTag=True

    def handle_endtag(self, tag):
        if tag == 'li':
            self.foundPTag=False
            
    def handle_data(self, data):
        if self.foundPTag==True:
            data.strip('')
            data.strip("\r")
            data.strip("\n")
            data.strip('\r\n')
            data.strip('\r\n\r\n')
            data.strip('\r\n ')
            self.lst.append(data)
        
    def getHeadings(self):
        return self.lst


