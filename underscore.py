
from itertools import filterfalse
class Underscore:
    def map(self, iterable, callback):
        # tu código aqui
        return list(map(callback, iterable))
        # return "HOLAmap"
    def find(self, iterable, callback):
        # tu código aqui
        return next(filter(callback, iterable), "Vacio")
        # return "HOLAfind"
    def filter(self, iterable, callback):
        # tu código aqui
        return list(filter(callback,iterable))
        # return "HOLAfilter"
    def reject(self, iterable, callback):

        return list(filterfalse(callback, iterable))
        # tu código 
        #return list((callback,iterable))
        # return "HOLAreject"
# has creado una libreria con 4 métodos
# se crea la instancia de la clse
_ = Underscore() # sí, estamos configurando una instancia a una variable que es un guión bajo
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# debe retornar [2, 4, 6] después que termines de implementar el código de arriba

print(_.map([1,2,3], lambda x: x*2)) # debe retornar [2,4,6]
print(_.find([1,2,3,4,2,1], lambda x: x>4)) # debe retornar el primer valor que es mayor que 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # debe retornar [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # debe retornar [1,3,5]

class Underscore:
    def map(self, iterable, callback):
        for x in range(len(iterable)):
            iterable[x] = callback(iterable[x])
        return iterable
    def find(self, iterable, callback):
        for x in range(len(iterable)):
            i = callback(iterable[x])
            if i is True:
               return iterable[x]       
    def filter(self, iterable, callback):
        for x in range(len(iterable)-1,-1,-1):
            if callback(iterable[x]) is False:
                del iterable[x]
        return iterable
    def reject(self, iterable, callback):
        for x in range(len(iterable)-1,-1,-1):
            if callback(iterable[x]) is True:
                del iterable[x]
        return iterable
# has creado una libreria con 4 métodos
# se crea la instancia de la clse
_ = Underscore() # sí, estamos configurando una instancia a una variable que es un guión bajo
# debe retornar [2, 4, 6] después que termines de implementar el código de arriba

print(_.map([1,2,3], lambda x: x*2))
print(_.find([1,2,3,4,2,1], lambda x: x>4)) # debe retornar el primer valor que es mayor que 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # debe retornar [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # debe retornar [1,3,5]


