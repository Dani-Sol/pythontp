# Se pide leer numero enteros y cargar un arreglo con enteros, la carga finaliza al leer un cero o hasta haber leído 100 números.
# Se pide indicar el porcentaje números capicúas sobre el total de numero leídos
# Buscar el valor mínimo y cuantas veces se repite
# Crear otro arreglo con los números múltiplos de 4 y de 6 y mostrarlos ordenados de menor a mayor




numeros = []
mult4y6 = []


def ingresarNumeros():
    n = int(input('Ingrese un numero entero: '))
    while (len(numeros)) < 100 and (n != 0):
       numeros.append(n)
       n = int(input('Ingrese un numero entero: '))
            
            
def capicuas ():
    capicua = 0
    porcentaje = 0
    for i in range (len(numeros)):
        if es_capicua(numeros[i]):
            capicua = capicua + 1
    if (capicua != 0):
        porcentaje = capicua * 100 / len(numeros)
    print('El porcentaje de numeros capicuas es de', porcentaje, '%.')    
    


def es_capicua (n): 
    es = False
    AUX = n
    Cap = 0
    while (AUX > 0):
        R = AUX % 10
        Cap = Cap*10 + R
        AUX = AUX // 10
    if (Cap == n):
        es = True
    return (es)


def buscarminimo ():
    MIN = numeros[0]
    CANT = 1
    for i in range (2,len(numeros)):
        if (numeros[i] <= MIN):
            if (numeros[i] == MIN):
                CANT = CANT + 1
            else:
                MIN = numeros[i]
                CANT = 1
    print('El valor minimo es', MIN, 'y se repite', CANT, 'veces.')

                
def buscarmultiplos():
    for i in range (len(numeros)):
        if (numeros[i]%4 == 0) and (numeros[i]%6 == 0):
            mult4y6.append(numeros[i])
                    

def mostrarMultiplos():
    mult4y6.sort
    print('Los numeros multiplos de 4 y 6 son: ')
    for i in range (len(mult4y6)):
        print(mult4y6[i])



#algoritmoPpal
ingresarNumeros()
capicuas ()
buscarminimo()
buscarmultiplos()
mostrarMultiplos()