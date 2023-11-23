list = [1,2,3]

lista2d = [[1,2,3],
           [4,5,6,10,14],
           [7,8,9]]


for elm in list:
    print(elm)

print("-" * 10)

for elm in lista2d:
    for elm2 in elm:
        print(elm2)

print("-" * 10)


for i in range(len(list)):
    print(list[i])

print("-" * 10)

for i in range(len(lista2d)):

    for j in range(len(lista2d[i])):

        print(lista2d[i][j])




"""
1   2   3
4   5   6
7   8   9

jogada: 

--  --  --
--  --  --
--  --  --

Linha: 
col: 


--  --  --
--  --  --
--  --  --

cordenada: 0,0






"""