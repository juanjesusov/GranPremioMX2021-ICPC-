def esPrimo(i,j):
    contadorPrimos = 0
    for numerosHastaNumero in range(i,j+1,1):
        verificarPrimo = 1
        contadorDivisores=0
        for verificarPrimo in range(verificarPrimo, numerosHastaNumero+1,1):
            if (numerosHastaNumero%verificarPrimo==0): contadorDivisores += 1
        if (contadorDivisores==2):contadorPrimos+=1 
    return contadorPrimos

T = int(input())
out = []

if (1<=T<=100000):
    for counter in range(0,T,1):
        entrada = input()
        lista = entrada.split(' ')     
        if (1<=lista[0]<=lista[1]<=1000000):
            cantidadPrimos = esPrimo(lista[0],lista[1])
            out.append(cantidadPrimos)    
        else:
            exit()  
    for element in out:
        print(element)
else:
    exit()