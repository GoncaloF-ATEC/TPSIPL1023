from functools import reduce

x = lambda param: param * 2

lista_principal = [1,2,5,4,3,2,6,9,6,7,11,13]

exp = "--"

lista2 = [x(elm) for elm in lista_principal if elm % 2 == 0]

print(lista2)


"""
[2, 4, 2, 6, 6]


[4, 8, 4, 12, 12]
"""


print("--" * 10)
# map executa a mesma ação em todos os elementos da lista
print(lista_principal)

map_lista_principal = map(lambda elm2: elm2 * 3, lista_principal)

lista_principal2 = list(map_lista_principal)


print(lista_principal2)

# reduce -> executa uma função de agregação, reduz a num so valor
[4, 8, 4, 12, 12]
valor = reduce(lambda param1, param2: param1 + param2, lista3)
'''
[4, 8, 4, 12, 12]



'''
print(valor)