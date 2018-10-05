lista = []

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)

print(lista)

if 3 in lista:
    lista.remove(3)

print(lista)

if 6 in lista:
    lista.remove(6)

print(lista)

print(len(lista))

lista[3] = 6

print(lista)