class Turma:
    nome: str
    ano: int

    def __init__(self, nome: str, ano: int):
        self.nome = nome
        self.ano = ano

    # func chamada em turma == "nome"
    def __eq__(self, other):
        return f"{self.nome}{self.ano}" == other

    # rep da class como txt
    # toString() <=> __str__
    def __str__(self):
        return f"{self.nome}{self.ano}"