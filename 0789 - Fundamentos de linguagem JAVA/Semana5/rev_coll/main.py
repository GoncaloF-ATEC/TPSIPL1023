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