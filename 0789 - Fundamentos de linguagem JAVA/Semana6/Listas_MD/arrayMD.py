list = [1,2,3]

lista2d = [[1,2,3],
           [4,5,6],
           [7,8,9]]


lista3d = [
    [
        [1,2,3],
        [1,2,3],
        [1,2,3]
    ],
    [
        [4,5,6],
        [4,5,6],
        [4,5,6]
    ],
    [
        [7, 81, 9],
        [7, 82, 9],
        [7, 83, 9]

    ]
]



list[0] # 1


lista2d[0] # [1,2,3]
lista2d[0][1] # 2


lista3d[0] # [1,2,3],[1,2,3],[1,2,3]
lista3d[0][1] # [1,2,3]
lista3d[0][1][2] # 3


print(lista3d[2][1][1])


