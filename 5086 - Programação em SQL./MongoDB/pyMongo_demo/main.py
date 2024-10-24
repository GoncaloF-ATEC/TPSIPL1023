import pymongo
import faker


fake = faker.Faker()

conn = pymongo.MongoClient('mongodb://10.211.55.16:27017/')

## print(conn.list_database_names())

mydb = conn['Escola']

# mydb.create_collection("Alunos")

# mydb.create_collection("Professor")

print(mydb.list_collection_names())


collection_Alunos = mydb['Alunos']


#for i in range(1500):
#    collection_Alunos.insert_one({"nome": f"{fake.name()}", "Turma": f"{fake.word()}" })


# resp = collection_Alunos.insert_one({"nome": "Ana", "Turma": "Turma 2"})

# print(resp)
# print(resp.inserted_id)


find_resp = collection_Alunos.find_one({"nome": "Ana"}, {"_id": 0,
                                                                     "Turma":1})
print(find_resp)

print("------------------")
find_all = collection_Alunos.find({}, {"_id": 0})

for al in find_all:
    print(al)


print("------------------")
resp = mydb.Alunos.find_one({"nome": "Ana"}, {"_id": 0, "Turma":1})

print(resp)

print("------------------")


collection_Alunos = mydb['Alunos']

collection_Alunos.delete_one({"nome": "Ana"})

print("------------------")

collection_Alunos.delete_many({"nome": "Ana"})

print("-------- Update one ----------")


query = {"nome": "Nome Aluno 1"}
newData = {"$set":{"nome": "Novo nome"}}


resp = collection_Alunos.update_one(query, newData)

print(resp.matched_count)
print(resp.modified_count)

print("-------- Update many ----------")

query = {"nome": "Novo nome"}
newData = {"$set":{"Turma": "TPSI"}}

resp = collection_Alunos.update_many(query, newData)

print(resp.matched_count)
print(resp.modified_count)

print("-------- sort  ----------")

find_all2 = collection_Alunos.find({}, {"_id": 0}).sort("nome", -1).limit(50)

for al in find_all2:
    print(al)



