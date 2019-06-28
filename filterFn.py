def filter1(fn,lst):
    newLst=[]
    for l in lst:
        if fn(l)==True:
            newLst.append(l)

    return newLst
