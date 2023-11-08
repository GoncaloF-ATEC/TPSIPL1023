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

print("-" * 10)


#set

#dicionarios


#funcs