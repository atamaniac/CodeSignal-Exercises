def commonCharacterCount(s1, s2):
    a = list(s1)
    b = list(s2)
    charCount = 0
    for i in range(len(a)):
        if a[i] in b:
            charCount += 1
            j=0
            while j<len(b):
                if a[i]==b[j]:
                    del b[j]
                    break
                else:
                    j += 1               
    return charCount
