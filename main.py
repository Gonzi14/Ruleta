import random
from unicodedata import name


def Ruleta():
    theList = []
    cantidad = int(input("Cantidad: "))
    for i in range(cantidad):
        name = input("nombre: ")
        theList.append(name)
    random.shuffle(theList)
    print(theList)

Ruleta()
