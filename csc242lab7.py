
def recProd(k,n):
    if k>n:
        return 1
    if k==n:
        return k

    return k*recProd(k+1,n)

def printTriangle(m,i):
    if m<=0:
        return
    else:
        print(i*' '+m*'*')
        printTriangle(m-2,i+1)
        
