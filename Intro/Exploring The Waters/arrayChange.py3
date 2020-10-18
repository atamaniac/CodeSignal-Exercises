def arrayChange(a):
    check = 0
    for i in range(len(a)-1):
        if a[i] >= a[i+1]:
            check += a[i] - a[i+1] + 1
            a[i+1] += a[i] - a[i+1] + 1
    return check
     
