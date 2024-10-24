from Aluno import Aluno
import pymongo



conn = pymongo.MongoClient('mongodb://10.211.55.16:27017/')
db = conn['Escola']
collection_Alunos = db.get_collection('Alunos')




al = Aluno("Carlos", "GRSI")

# print(al.__dict__)

# collection_Alunos.insert_one(al.__dict__)

resp = collection_Alunos.find({"nome": al.nome}, {"_id": 0})


for aluno in resp:
    print(aluno)

print("----------------")

al2 = Aluno.init_from_dict({"nome": "Gonçalo", "Turma":"TPSI"})

print(al2)