def palindromeRearranging(inputString):
    tab = {}
    for word in inputString:
        if word not in tab:
            tab[word] = 1
        else:
            tab[word] += 1
            
    oc = [l for l in tab if tab[l] % 2]
    if len(oc) > 1:
        return False
    else:
        return True
