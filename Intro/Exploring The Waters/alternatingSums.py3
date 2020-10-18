def alternatingSums(a):
    team1 = []
    team2 = []
    i = 0
    while i<len(a):
        if i%2 == 0:
            team1.append(a[i])
        else:
            team2.append(a[i])
        i+=1
    return sum(team1), sum(team2)
