'I asked Patrick Fisher if there is nothing in an exisitng .txt to reutrn [] otherwise worked on my own.'
#part One
class Storm(object): 
    'a class that abstracts a storm'
    def __init__(self, rain=0, wind=0 , year=1900):
        'takes string of rainfall, wind, and year as integers'
        self.wind=wind
        self.rain=rain
        self.year=year

    def getWindSpeed(self):
        'get max wind speed as MPH'
        return self.wind

    def getRainFall(self):
        'get rainfall in inches per hour'
        return self.rain

    def getYear(self):
        'get year storm recorded'
        return self.year

    def setYear(self,year):
        'set year recorded'
        self.year=year

    def setRainFall(self,rain):
        'set rainfall inches per hour'
        self.rain=rain

    def setWindSpeed(self,speed):
        'set windspeed MPH'
        self.wind=speed

    def __repr__(self):
        'get canoncial representation of Storm'
        return ('Storm({},{},{})').format(self.rain,self.wind,self.year)

    def __str__(self):
        'get string represetation of Storm'
        return('I am Storm with peak winds of {} mph, peak rain fall of {} inches per hour in the year {}').format(self.wind,self.rain,self.year)

#part Two
class TropicalStorm(Storm):
    'a class that abstracts a tropical storm'

    def __init__(self, rain=0, wind=0 , year=1900, name='default'):
        'initalize Tropical Storm.'
        self.rain=rain
        self.wind=wind
        self.year=year
        self.name=name
    def getName(self):
        'Get storm name'
        return self.name

    def setName(self,name):
        'set storm name'
        self.name=name

    def __repr__(self):
        'get canoncial representation of TropicalStorm'
        return ('TropicalStorm({},{},{},{})').format(self.rain,self.wind,self.year,str(self.name))

    def __str__(self):
        'get string representation of TropicalStorm'
        return ('I am a Tropical Storm named {}. I have peak winds of {} mph, peak rain fall of {} inches per hour in the year {}').format(self.name,self.wind,self.rain,self.year)

#part Three
class Hurricane(TropicalStorm):
    'a class that abstracts a Hurricane'
    
    def __init__(self, rain=0, wind=0 , year=1900, name='default', category=0):
        'Initialize a Hurricane'
        self.rain=rain
        self.wind=wind
        self.year=year
        self.name=name
        if category>5:
            category=5
        self.category=category
    def getName(self):
        'get name'
        return self.name
    def setName(self, name):
        'set name'
        self.name=name

    def getCategory(self):
        'get category'
        return self.category

    def setCategory(self,category):
        'set category'
        self.category=category
        if category<0:
            category=0
        elif category>5:
            category=5

    def __repr__(self):
        'get canoncial representation of Hurricane'
        return ('Hurricane({},{},{},{},{})').format(int(self.category),int(self.rain),int(self.year),str(self.name),int(self.wind))

    def __str__(self):
        'get string representation of Hurricane'
        return ('I am a category {} Hurricane named {}. I have peak winds of {} mph, peak rain fall of {} inches per hour in the year {}').format(int(self.category),str(self.name),int(self.wind),int(self.rain),int(self.year))

#Main Code
def processTropicalStorms(filename):
    'Takes a file, reads each line and prints each one appending it to a new list'
    try:
        infile=open(filename,'r')
        contents=infile.readlines()
        infile.close()
        if len(contents)==0:
            return[]
    except:
        print('The file',filename,'could not be found. Exiting.')
        return
    lst=[]
    for line in contents:
        splitline=line.split(',')
        t=TropicalStorm(int(splitline[2]),int(splitline[1]),int(splitline[3]),splitline[0])
        lst.append(t)
    return(t)
