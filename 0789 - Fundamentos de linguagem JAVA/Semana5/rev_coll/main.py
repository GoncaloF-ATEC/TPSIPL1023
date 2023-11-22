nome = ["txt1", "txt2", "txt3", "txt2"]
#      [  0       1      2        3   ]


print(nome)
# acder a elm

print(nome[0])


# add elm
print("add elm")

nome.append("add elm no fim")

print(nome)

nome.insert(2, "add elm na pos 2")

print(nome)

print("-" * 10)
# remover elm
print("remover elm")

print(nome)
val = nome.pop() # <- remove o ultimo valor devolve o val removido
print(val)
print(nome)

nome.pop(2)
print(nome)


val1 = nome.remove("txt3")  # <- remove o um valor, nao devolve o val removido
print(val1)

#nome.clear()
#print(nome)

print("-" * 10)
# precorrer lista
print("precorrer lista")

for elm in nome:
    print(elm)

print("-" * 5)
list_size = len(nome)
list_size2 = nome.__len__()

for i in range(0, list_size2):
    print(f"o valor na pos {i} é: {nome[i]}")


print("-" * 10)














"""

Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.




ler 20 números inteiros
adicionar os numeros a uma lista

adicionar os números pares na lista -> Par 
adicionar os números impares na lista -> Impares  
Imprima
    lista com todos os numeros
    lista Par
    lista Impar

"""


"""
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos 
ossuem altura inferior à média de altura desses alunos.
 
"""

lista = [1, 3, 3]


def soma(lista):
    total = 0
    for elm in lista:
        # total2 = total + elm
        # total = total2
        total += elm

    return total

print(soma(lista))