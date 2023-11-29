from Classes import *

listaAlunos: list[Aluno] = []
turma = Turma("TPISPL", 1023)


def pedir_aluno() -> Aluno:
    nome = input("Nome do Aluno: ")
    num = None
    while num == None:
        try:
            num = int(input("Número do Aluno: "))
        except:
            print("o Número tem de ser numerico")

    aluno = Aluno(num, nome, turma)
    return aluno



def add_alunos():
    novo_aluno = "s"
    while novo_aluno == "s":
        os.system('cls||clear')

        al = pedir_aluno()
        listaAlunos.append(al)
        novo_aluno = input("s para adicioanr novo Aluno? ").lower()


def listar_alunos():
    if len(listaAlunos) == 0:
        print("não há alunos")

    else:
        for aluno in listaAlunos:
            print(aluno)
