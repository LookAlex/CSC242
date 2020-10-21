def extractStr(lst):
    if lst==[]:
        return ''
    else:
        if type(lst[0])==str:
            return lst[0]+extractStr(lst[1:])
        if type(lst[1:])==list:
            return extractStr(lst[1:])

    return extractStr(lst[1:])
    
def recNumberSum(lst):
    lst2=0
    if len(lst)<=0:
        return lst2
    if type(lst[0])==list:
        sub=recNumberSum(lst[0])
        lst2+=sub
    if type(lst[0])==float:
        num=int(lst[0])
        lst2+=num
        return lst2+recNumberSum(lst[1:])
    if type(lst[0])==int:
        lst2=recNumberSum(lst[0])
        lst2+=sub
    else:
        return lst2+recNumberSum(lst[1:])
