def isLucky(n):
    size = len(str(n))
    num = list(map(int,str(n)))
    sum1 = 0
    for i in range(int(size/2)):
        sum1 += num[i]
    j=size
    sum2 = 0
    while j>int(size/2):
        sum2 += num[j-1]
        j -= 1
    return sum1==sum2
