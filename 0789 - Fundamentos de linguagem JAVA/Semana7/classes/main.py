'''

var (criação, tipos de dados)
    Tipos de daods: int, float, string, bool
                    char - chacter


op
func (def)
cond (if e match)
loops (for e while)
listas (arrays) 1D, 2D, xD

Sets
dicionarios

pass <- defenir um bloco vazio

Classes
    :cirar tipdos de dados proprios

'''


"""


Aluno
    nome
    idade
    morada
    turma
"""


from dataclasses import dataclass

"""
class Turma:
    nome: str #TPIPL
    ano: int #1023

    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
"""


@dataclass
class Turma:
    nome: str
    ano: int

    def __str__(self):
        return f"{self.nome}{self.ano}"



turma = Turma("TPSIPL", 1023)
print(turma)


@dataclass
class Aluno:
    nome: str
    idade: int
    morada: str
    turma: Turma



turma = Turma("TPSIPL", 1023)

turma2 = Turma("TPSIMT", 1023)
print(turma)

aluno1 = Aluno("Gonçalo", 20, "Sintra", turma)
aluno2 = Aluno("Maria  ", 35, "Porto", turma2)
aluno3 = Aluno("Ana Maria", 35, "Porto", Turma("TPSICAS", 1023))

print(aluno1)
print(aluno2)
print(aluno3)

print("--" * 10)


print(aluno1.nome)
print(aluno1.turma)
print(aluno1.turma.nome)
print(f"{aluno1.nome} esta na turma {aluno1.turma.nome}{aluno1.turma.ano}")
print(f"{aluno1.nome} esta na turma {aluno1.turma}")