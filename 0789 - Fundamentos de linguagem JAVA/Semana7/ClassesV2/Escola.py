from Aluno import Aluno
from Turma import Turma


class Escola:
    nome: str
    turmas: list[Turma]
    alunos: list[Aluno]

    def __init__(self, nome: str):
        self.nome = nome
        self.turmas = []
        self.alunos = []

    def cirar_turma(self, nome: str, ano: int):
        t = Turma(nome, ano)
        self.turmas.append(t)

    """
        recebe um nome - TPSIPL1023
        devolve a turma TPSIPL1023, se não existir criar uma nova 
            turma, adiciona a lista de turma e devolve a nova turma
    """
    def get_turma(self, nome) -> Turma:
        try:
            i = self.turmas.index(nome)
            return self.turmas[i]
        except ValueError:
            #criar turma

            """
                nome = TPSIPL1022
                
                nome_turma = TPSIPL
                ano = 1022
                
            """
            nome_sep = nome[:-4]
            ano_sep = int(nome[-4:])

            t = Turma(nome_sep, ano_sep)
            self.turmas.append(t)
            return t


    def criar_aluno(self, nome: str, idade: int, turma: str):
        t = self.get_turma(turma)
        a = Aluno(nome, idade, t)
        self.alunos.append(a)


    def show_turmas(self):
        print("-----Turmas-----")
        for t in self.turmas:
            print(t)
        print("----------------")

    def show_Alunos(self):
        print("-----Alunos-----")
        for a in self.alunos:
            print(a)
        print("----------------")