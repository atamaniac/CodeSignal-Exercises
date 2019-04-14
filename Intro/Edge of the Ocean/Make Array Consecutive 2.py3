def makeArrayConsecutive2(statues):
    statues.sort()
    count = 0
    for i in range(len(statues)-1):
        if statues[i] != statues[i+1]+1:
            count += statues[i+1]-statues[i]-1
    return count
        
    
