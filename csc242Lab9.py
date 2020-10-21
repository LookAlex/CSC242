def reversable(lst):
    if len(lst)==0 or 1:
        return True
    if reversable(lst)==reversable(lst-1):
        return True
    else:
        return False
