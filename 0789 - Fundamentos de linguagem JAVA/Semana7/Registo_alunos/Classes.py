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

    def __str__(self):
        return f"{self.turma}\t{self.numero}\t{self.nome}"

