import pymongo
from Aluno import Aluno

conn = pymongo.MongoClient("mongodb://10.211.55.16:27017")

db = conn["Escola"]

coll_Alunos = db["Alunos"]

find_all = coll_Alunos.find()
lista_alunos = []


for al in find_all:
    aluno = Aluno.init_from_dict(al)
    lista_alunos.append(aluno)


for aluno in lista_alunos:
    print(aluno)






al = Aluno("Gonçalo", "Redes ")

al.save()

