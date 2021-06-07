# - Imprime todos los números del 0 al 10
for x in range(10 + 1):
    print(x)
# - Básico : imprime todos los enteros del 0 al 150.
for x in range(1,150+1,1):
    print(x)
# - Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for x in range(5,1000+1,5):
    print(x)

#Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".
for x in range(100+1):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0: 
        print("Coding")
    else: print(x)

#¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.

suma = 0
for x in range(1,500000,2):
    suma = suma + x
print(suma)

# Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.

for i in range(2018,0,-4):
    print(i)

#Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, 
# imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)


lowNum=2
highNum=21
mult=3

for i in range(lowNum, highNum + 1,1):
    if i % mult == 0:
        print(i)

# BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000?

numero =0
while numero<=1000:
    contador=1
    x=0
    while contador<= numero:
        if numero % contador == 0:
            x=x+1
        contador = contador + 1
    if x == 2:
        print (numero)
    numero = numero + 1
