# var
# condições
# loops

# quiz com 3 niveis de dificuldade
# 10 questões por nivel
# menu
# registar
#   num de jogos jogaodos
#   registo de qt de respostas correctas
#   registo de qt de respotas Erradas
#   ranking
# salvar num file
# app no treminal


#listas (arrys)

arr = ["nome1", "nome2", "nome3"]

print(arr[2])

print(arr.__len__())
print(len(arr))
print(arr)
# len -> num elm
# index -> 0 ate len-1
print("-" * 10)

arr.append("Novo nome")
print(arr.__len__())
print(len(arr))

print(arr[arr.__len__()-1])
print(arr)

print("-" * 10)
arr.insert(2, "nome na pos 2")

# 0, 1, 99, 2, 3, 4
print(arr[2])
print(arr)

print("-" * 10)

arr[2] = "Novo nome Alterado"
print(arr[2])
print(arr)

print("-" * 10, "arr.insert(\"Novo nome Alterado\")", "-" * 10)

arr.append("Novo nome Alterado")
print(arr)
arr.remove("Novo nome Alterado") # remove a 1 instancia

print(arr)

print("-" * 10)

arr.pop(2)
print(arr)

print("-" * 10)
#rr.append("Novo nome Alterado")
#arr.append("Novo nome Alterado")
#arr.append("Novo nome Alterado")

print(arr.count("Novo nome Alterado"))


print("-" * 10, "sort", "-" * 10)

arr.append("A Novo nome Alterado")
arr.append("a Novo nome Alterado")
arr.append("z Novo nome Alterado")

print(arr)
arr.sort() # ordena o arr em si, não cria um novo
print(arr)

arr2 = [2,3,1,2,9,1,2,1,0]
arr2.sort()
print(arr2)

print("-" * 10)

for elm in arr:
    print(elm)

print("-" * 10, "Set", "-" * 10)

#set

mySet = {"Polvilho doce", "Polvilho azedo", "leite", "sal", "oleo", "queijo"}
mySet2 = {"Polvilho azedo", "leite", "sal", "oleo", "agua", "açúcar"}


print(mySet)
# {'sal', 'leite', 'queijo', 'Polvilho doce', 'oleo', 'Polvilho azedo'}
# {'leite', 'oleo', 'Polvilho doce', 'queijo', 'Polvilho azedo', 'sal'}

#print(mySet[0])
print("-" * 10)
for elm in mySet:
    print(elm)

print("-" * 10)

print("sal" in mySet)
print("agua" in mySet)

print("-" * 10)

mySet.add("agua")

print(mySet)
print("agua" in mySet)

print("-" * 10)

mySet.remove("agua") # se agua nao existir gera um erro
print("agua" in mySet)
mySet.discard("agua")  # se agua nao existir não gera um erro

print("-" * 10)
print("-" * 10)
mySet.add("agua")
mySet.add("agua")
mySet.add("agua")


# https://media.geeksforgeeks.org/wp-content/uploads/20220110094813/download-660x416.png
print(mySet)
print(mySet2)
print("-" * 3)
print(mySet.union(mySet2))
print("-" * 3)
print(mySet.symmetric_difference(mySet2))

print("-" * 3)
print(mySet.intersection(mySet2))

print("-" * 3)

mySet = {"Polvilho doce", "Polvilho azedo", "leite", "sal", "oleo", "queijo"}
mySet2 = {"Polvilho azedo", "leite", "sal", "oleo", "agua", "açúcar"}


print(mySet.difference(mySet2))
print(mySet2.difference(mySet))

print("-" * 3)

#Dicionarios
print("-" * 10, "Dicionarios", "-" * 10)

myDict = {"key1": "Valor2",
          "key2": "Valor2",
          "key3": "Valor2"}

print(myDict)

print(myDict["key1"])

print(myDict.get("key1"))

print("-" * 3)

print(myDict.keys())
print(myDict.values())

print("-" * 3)

myDict["new Key"] = "new Val"
print(myDict)


myDict["new Key"] = "novo Valor"
print(myDict)

myDict["key1"] = "Foo"
print(myDict)

print("-" * 3)

"""
myDict.pop("key1") # a chave tem de existir
print(myDict)

del myDict["key2"] # a chave tem de existir
print(myDict)
"""

"""
del myDict
print(myDict) # remove o dict todo
"""
print("-" * 3)

print("-" * 3)

for elm in myDict.keys():  # for elm in myDict.keys():
    print(elm) #print das chaves
print("-" * 2)
for elm in myDict.values():
    print(elm) #print dos valroes



#funcs