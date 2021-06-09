# Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

def cuentaRegresiva(arr):
    list=[]
    for i in range (len(arr)):
        if arr[i] > 0:
            list.append("big")
        else:
            list.append(arr[i])
    return list    
d = cuentaRegresiva([-1,4,8,-3])
print(d)

# Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número
#  de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives([- 1, 1, 1,1 ]) cambia la lista original a [-1, 1, 1, 3] y la devuelve
# Ejemplo: count_positives([1, 6, -4, -2, -7, -2]) cambia la lista a [1, 6, -4, -2, -7, 2] y la devuelve

def devuelveSumaPositivos(arr):
    cont= 0
    for i in range (len(arr)):
        if arr[i] > 0:
            # list.append(arr[i])
            cont = cont + 1
    arr[len(arr)-1]= cont 
    # lista[len(lista):] = [7] 
    return arr
d = devuelveSumaPositivos([-1,4,8,-3,5])
print(d)

# Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def devuelveSuma(arr):
    suma=0
    for i in range (len(arr)):
        suma = suma + arr[i]
    return suma
d = devuelveSuma([4,8,-3,5])
print(d)

# Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def devuelvePromedio(arr):
    suma=0
    cont = arr[len(arr)-1]
    prom = 0
    for i in range (len(arr)):
        suma = suma + arr[i]
    prom = suma / cont
    return prom
d = devuelvePromedio([4,4,4,4])
print(d)

# Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0

def devuelveLargo(arr):
   return len(arr)
d = devuelveLargo([1,2,3,7,8])
print(d)

# Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. 
# Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False

def devuelveMin(arr):
    
    for i in range(len(arr)):
        temp= arr[0]
        if temp > arr[i]:
            temp = arr[i]
    if len(arr)!= 0:
        return temp
    else: return False
d = devuelveMin([2,5,7])
print(d)

# Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. 
# Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False

def devuelveMax(arr):
    for i in range(len(arr)):
        temp= arr[0]
        if temp < arr[i]:
            temp = arr[i]
    if len(arr)!= 0:
        return temp
    else: return False
d = devuelveMax([2,5,7,90])
print(d)

# Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga
#  la suma total, promedio, mínimo, máximo y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}

def analisisFinal(arr):
    minimo = min(arr)
    maximo = max(arr)
    averag = sum(arr)/len(arr)
    largo = len(arr)
    suma = sum(arr)
    d={'total': suma, 'promedio': averag, 'minimo':minimo, 'maximo':maximo, 'longitud': largo}
    return d
d = analisisFinal([37,2,1, -9])
print(d) 
# Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos.
#  Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]


def listaInversa(lista):  
    long = len(lista)            
    mayor = long - 1
    h = int(long / 2)                
    for i in range(0, h):    
        temp = lista[mayor]     
        lista[mayor] = lista[i]
        lista[i] = temp
        mayor -= 1           
    return lista
d = listaInversa([37,2,1, 4,6,5,7,6,0])
print(d) 
