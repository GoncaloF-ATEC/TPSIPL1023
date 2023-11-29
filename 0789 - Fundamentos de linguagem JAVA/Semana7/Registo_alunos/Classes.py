from dataclasses import dataclass

@dataclass
class Turma:
    nome: str
    ano: int

    def __str__(self):
        return f"{self.nome}{self.ano}"

@dataclass
class Aluno:
    numero: int
    nome: str
    turma: Turma

    def __str__(self): #rep como string
        return f"{self.turma}\t{self.numero}\t{self.nome}"

    def __eq__(rhs, lhs): # definição da condição da condição de igualdade  <->  al1 == al2
        return rhs.numero == lhs.numero

