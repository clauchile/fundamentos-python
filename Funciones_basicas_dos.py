# Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno,
#  desde el número (como el elemento 0) hasta 0 (como el último elemento).
# Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]
def cuentaRegresiva(num):
    list=[]
    for i in range (num,-1,-1):
        list.append(i)
    return list    
a = cuentaRegresiva(3)
print(a)

# Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
# Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2

def imprimirYVolver(list):
    # for i in range(list):
        print(list[0])
        return  list[1]
b = imprimirYVolver([5,3])
print(b)

# First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.

def primeroMasLargoLista(lista):
    suma = lista[0] + len(lista)
    # print(lista(len))
    return suma

m = primeroMasLargoLista([2,2,3])
print(m)
    


# Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False
# Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
# Ejemplo: values_greater_than_second ([3]) debería devolver False

def devuelveMayorQueElSegundo(arreglo):
    arr = []
    contador = 0
    while len(arreglo)>2:
        f = arreglo[1]
        for i in range(0,len(arreglo)):
            if arreglo[i] > f:
                contador = contador +1
                arr.append(arreglo[i])
        print(f"la cantidad de numeros mayor al segundo de la lista es: {contador}")
        return arr
    else:
        return False 

v = devuelveMayorQueElSegundo([3,4,8,10,12,23])
print(f"y son: {v}")



# Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
# Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
# Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]

def longitudYValor(arreglin):
    array= []
    largo = arreglin[0]
    valor = arreglin[1]
    contador = 1

    while contador <= largo:
        array.append(valor)
        contador = contador +1
    return array

print(longitudYValor([7,10]))