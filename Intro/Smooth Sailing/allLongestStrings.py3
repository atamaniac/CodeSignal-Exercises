def allLongestStrings(inputArray):
    longest=[]
    longCout=0
    for word in inputArray:
        if len(word)>=longCout:
            longCout=len(word)
            longest.append(word)
    i=0
    while i<len(longest):
        if len(longest[i])<longCout:
            del(longest[i])
        else: i+=1
    return longest
