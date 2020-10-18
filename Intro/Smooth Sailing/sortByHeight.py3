def sortByHeight(a):
    b = list(filter(lambda x: x != -1, a))
    b.sort()
    i=0
    for x in b:
        while a[i] == -1:
            i += 1
        a[i]=x
        i += 1
    return a
 
