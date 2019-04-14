def centuryFromYear(y):
    return (int(y/100)+1,y/100)[y%100==0]
