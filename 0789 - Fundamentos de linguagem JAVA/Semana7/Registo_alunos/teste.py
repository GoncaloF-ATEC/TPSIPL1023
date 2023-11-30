import sys
from Classes import *


numI = 1023
numS = "1023"

print(sys.getsizeof(numI))
print(sys.getsizeof(numS))



"""
demo de:

    def __eq__(self, other): ## comparação == <->  al1 == al2
        return self.numero == other.numero

"""

print("-" * 10)
turma = Turma("TPISPL", 1023)
turma2 = Turma("TPISPl", 1023)

print(turma == turma2)

print("-" * 10)
al = Aluno(2, "Gonçalo", turma)
al2 = Aluno(20, "Ana", turma)
al3 = Aluno(20, "Rita", turma)

print(al == al2)
print(al3 == al2)


al.teste()
