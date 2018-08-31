n = 6
arr = [-4, 3, -9, 0, 4, 1, ]

def plusMinus(arr):
    neg = 0
    pos = 0
    zer = 0
    for i in arr:
        if i > 0:
            pos +=1
        elif i == 0:
            zer +=1
        else:
            neg +=1
    negd = str(format((neg / n), '.6f'))
    posd = str(format((pos / n), '.6f'))
    zerd = str(format((zer / n), '.6f'))
    tot = str(posd+'\n'+negd+'\n'+zerd)
    return(tot)
plusMinus(arr)