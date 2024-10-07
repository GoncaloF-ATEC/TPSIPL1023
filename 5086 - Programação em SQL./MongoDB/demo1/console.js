use TPSIPL1023_v2

show dbs

use local

show collections

use admin

show collections

use TPSIPL1023_v2


db.createCollection("Alunos")

db.createCollection("Formadores")

show collections

db.Formadores.drop()

db.Alunos.drop()


show collections

db.Alunos.insertOne({
nome: "Ana",
idade: 20,
escola: "ATEC"
})


db.Alunos.insertMany([
    {
        nome: "Joana",
        idade: 20,
        escola: "ATEC"
    },
    {
        nome: "Rui",
        idade: 10,
        escola: "ATEC"
    },
    {
        nome: "Pedro",
        idade: 20,
        escola: "ATEC"
    },
    {
        nome: "Zulmira",
        idade: 36,
        escola: "IEFP"
    }
])


db.Alunos.insertOne({

        nome: "Xavier",
        idade: 36,
        escola: "IEFP",
        cidade: "Lisboa"

})


db.Alunos.find() // Select *

db.Alunos.find().skip(2) // salta os 2 1os

db.Alunos.find().limit(2) // selecoiona apenas 2 valroes


db.Alunos.insertOne({
        nome: "Aaron",
        idade: 40,
        escola: "IEFP",
        cidade: "Porto"
})

/*
class Aluno:
    mome: str
    idade: int
    escola: str
    cidade: str

*/

db.Alunos.find().sort({nome: -1})


db.Alunos.find().sort({nome: 1, cidade: -1})


db.Alunos.find({escola: "ATEC"})

db.Alunos.find({escola: "ATEC", idade: 20})


db.Alunos.find({escola: "ATEC", idade: 20}, {nome: 1})


db.Alunos.find({escola: "ATEC", idade: 20}, {_id: 0, escola: 0, idade:0})

db.Alunos.find({escola: "ATEC", idade: 20}, {_id: 0, nome:1, cidade:1})

db.Alunos.findOne({escola: "ATEC", idade: 20}, {_id: 0, nome:1, cidade:1})

db.Alunos.find({escola: "ATEC", idade: 20}, {_id: 0, nome:1, cidade:1}).limit(1)


db.Alunos.find({}, {_id: 0, nome:1, cidade:1})