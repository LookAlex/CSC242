def average(filename):
    try:
        wordCount=0
        totalSize=0
        file = open(filename,'r')
        content=file.read()
        file.close()
        table = str.maketrans('!,.:;?', 6*' ')
        content=content.translate(table)
        words=content.split()
        for word in words:
            wordCount=wordCount+1
            totalSize=totalSize+len(word)
        return totalSize//wordCount
    except (IOError, FileNotFoundError):
        print('An error occured trying to open that file')
        return 0
    except:
        print('An unknown error occured')
        return 0

def uniqueWords(filename):
    try:
        wordset=set()
        file = open(filename,'r')
        content=file.read()
        file.close()
        table = str.maketrans('!,.:;?', 6*' ')
        content=content.translate(table)
        content=content.lower()
        words=content.split()
        for word in words:
            wordset.add(word)
        return wordset
    except (IOError, FileNotFoundError):
        print('An error occured trying to open that file')
    except:
        print('An unknown error occured')

print(average('sampleFile1.txt'))
print(average('sampleFile2.txt'))

print(uniqueWords('sampleFile1.txt'))
print(uniqueWords('sampleFile2.txt'))
