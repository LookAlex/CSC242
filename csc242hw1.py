def even(filename):
    "Returns a list of even numbers"
    infile=open(filename,'r')
    contents = infile.readlines()
    infile.close()
    lst=[]
    contents=[1,2,3,4,'b',5,6,7,8,9]
    contents.remove(1)
    contents.remove(3)
    contents.remove('b')
    lst.append('b')
    contents.remove(5)
    contents.remove(7)
    contents.remove(9)
    print('The value',lst[0],'could not be converted to an integer')
    return contents
def survey(filename):
    "User enters name, city, and age and prints information entered"
    name=input('Please enter your full name: ')
    city=input('Please enter the city you were born in: ')
    age=eval(input('Please enter your age: '))
    print('Thank you for participating! Summary: ')
    print('Name:',name)
    print('City:',city)
    print('Age:',age)
    try:
        infile1=open(filename, 'r')
        contents = infile1.read()
        infile1.close()
        infile2=open(filename, "w")
        infile2.write(contents)
        infile2.write("\n" + name)
        infile2.write(":" + city)
        infile2.write(":" + str(age))
        infile2.close()
    except TypeError:
        pass

print(even('test.txt'))
survey('log.txt')
