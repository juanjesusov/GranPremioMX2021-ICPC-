def digits(Nstr):
    digitsList = [int(i) for i in Nstr]
    return digitsList

def times(digitsList):
    newNum=1
    for i in digitsList:
        newNum *= i
    return newNum

def printLis(listaCont):
    for i in listaCont:
        print(i)


T = int(input())
if (1<=T<=1000):
    numbers = list(range(0,T))
    listaCont=[]
    for i in numbers:
        Nstr = input()        
        if (0<=len(Nstr)<=1000000000):
            cont=0
            while len(Nstr)>1:
                digitsList = digits(Nstr)
                Nstr = str(times(digitsList))
                cont+=1
            listaCont.append(cont)
        else:
            exit()
    printLis(listaCont)
else:
    exit()
