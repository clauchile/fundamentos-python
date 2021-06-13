# Actualiza los valores en diccionarios y listas


# Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x = [ [5,2,3], [10,8,9] ] 
x[1][0]= 15
print(x)
# print(l)

# Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
# students[0]['last_name'] = 'Bryant'

for valor in students:
    if valor['last_name']=='Jordan':
        valor['last_name'] = 'Bryant'

print(students)


# En el directorio sports_directory, cambia 'Messi' a 'Andres'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

# print(sports_directory['soccer'][0])

for directorio in sports_directory:
    
    for i in range (len(sports_directory[directorio])):
        if sports_directory[directorio][i]== 'Messi':
           sports_directory[directorio][i] = 'Andres'
print(sports_directory)


# Camba el valor 20 en z a 30

z = [ {'x': 10, 'y': 20} ]

z[0]['y']=30

print(z)

# Itera a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios,
#  la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado.
#   Por ejemplo, dada la siguiente lista:

nuevosDatos = [
        {'first_name':  'Rodrigo', 'last_name' : 'Dominguez'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}]

def devuelve(nombre = " ", lista =  [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]):
    
    for datos in lista:   
        print(datos[nombre])

devuelve('first_name', nuevosDatos)
print("\n")
devuelve('last_name', nuevosDatos)

        # print(students[datos])
# iterateDictionary(students) 
# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel.

# 3 - Obtén valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, 
# dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. 
# Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
for datos in students:
    print(datos['first_name'])


for datos in students:  
    print(datos['last_name'])




# 4 Itera a través de un diccionario con valores de listas
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, 
# imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores 
# asociados dentro de la lista de cada clave. Por ejemplo:
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

for key in dojo:
    largo = len(dojo[key])
    print(" ")  

    print (largo , key.upper())
    for datos in dojo[key]:
        print(datos)


    # print (key)
    # print(dojo['locations'][0])
    # print(key)
        
# printInfo(dojo)                                                                    # printInfo(dojo)
                                                                    # # output:
                                                                    # 7 LOCATIONS
                                                                    # San Jose
                                                                    # Seattle
                                                                    # Dallas
                                                                    # Chicago
                                                                    # Tulsa
                                                                    # DC
                                                                    # Burbank
                                                                        
                                                                    # 8 INSTRUCTORS
                                                                    # Michael
                                                                    # Amy
                                                                    # Eduardo
                                                                    # Josh
                                                                    # Graham
                                                                    # Patrick
                                                                    # Minh
                                                                    # Devon
