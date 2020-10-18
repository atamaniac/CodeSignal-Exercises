def areSimilar(a, b):
    difcount = 0
    for i in range(len(a)):
        if a[i]!=b[i]:
            difcount += 1
    a.sort()
    b.sort()
    if a==b and difcount <= 2:
        return True
    return False
    
