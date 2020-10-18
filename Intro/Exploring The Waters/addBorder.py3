def addBorder(picture):
    rows = len(picture)
    cols = len(picture[0])
    tab = []
    line = ((cols+2) * "*")
    tab.append(line)
    for i in range(rows):
        tab.append("*" + (picture[i]) + "*")
    tab.append(line)
    return tab
