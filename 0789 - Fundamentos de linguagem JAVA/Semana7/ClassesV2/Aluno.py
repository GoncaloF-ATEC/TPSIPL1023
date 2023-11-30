from Turma import Turma


# al = Aluno("", "", "") <-  construtor(em py __init__) <- metodo responsavel por criar a class
class Aluno:
    nome: str
    idade: int
    turma: Turma

    def __init__(self, nome: str, idade: int, turma: Turma):
        self.nome = nome
        self.idade = idade
        self.turma = turma

    def __str__(self):
        return f"{self.nome}\t{self.idade}\t{self.turma}"