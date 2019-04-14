def adjacentElementsProduct(inputArray):
    max = None
    for i in range(len(inputArray)-1):
        il =  inputArray[i]*inputArray[i+1]
        if max is None or il>max:
            max = il
    return max


