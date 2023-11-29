"""
Criar uma app que premita registar alunos numa turma

"""


import os
from utils import *

"""
al = Aluno(2, "Gonçalo", turma)
al2 = Aluno(20, "Ana", turma)

print(al)
print(al2)

"""

menu = """
----------Menu----------
|                      |
|Adicionar Aluno --- 1 |
|Listar Alunos ----- 2 |
|Sair -------------- 3 |
|                      |
------------------------
"""


while True:
    os.system('cls||clear')
    print(menu)
    opt = input("Selcione uma opeção: ")

    match opt:
        case "1":
            print("Adicionar Aluno")
            add_alunos()
            input("precione uma tecla para continuar")
        case "2":
            print("Listar Aluno")
            listar_alunos()
            input("precione uma tecla para continuar")
        case "3":
            break
        case _:
            print("opção invalida")
            input("precione uma tecla para continuar")



print("Saiu do porgrama")