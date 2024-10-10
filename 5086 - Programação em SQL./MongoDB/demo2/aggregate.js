use demo_escola

db.createCollection("Aluno")
db.createCollection("Morada")


db.Aluno.insertOne({
    id: 1,
    nome: "Gonçalo",
    morada_id:1
})

db.Aluno.insertOne({
    id: 2,
    nome: "Joao",
    morada_id:1
})

db.Aluno.insertOne({
    id: 3,
    nome: "Rita",
    morada_id:2,
    email: "foo@gmail.com"
})

db.Morada.insertOne({
    id: 1,
    rua: "Rua 1",
    cp: "1111-111",
    localidade: "Lisboa"

})

db.Morada.insertOne({
    id: 2,
    rua: "Rua 1",
    cp: "2222-222",
    localidade: "Sintra"

})



data = db.Aluno.aggregate(
    {
        $lookup: {
            from:"Morada",
            localField: "morada_id",
            foreignField: "id",
            as: "morada"
        }
    }
)



db.Aluno.find()

db.Aluno.aggregate([
    {
        $match: {
            $or:[
                {id: 1},
                {id: 4}
            ]
        }
    },
    {
        $lookup: {
            from:"Morada",
            localField: "morada_id",
            foreignField: "id",
            as: "morada"
        }
    }
])




/*
db.Aluno.insertOne({
    id: 3,
    nome: "Rita",
    morada_id:2,
    email: "foo@gmail.com"
})

class Aluno:
    _id: str
    id: int
    nome: str
    morada_id:int
    email: str


db.Morada.insertOne({
    id: 2,
    rua: "Rua 1",
    cp: "2222-222",
    localidade: "Sintra"

})

class Morda:
    _id: str
    id: int
    rua: str
    cp: str
    localidade: str



class Aluno_Morda:
    _id: str
    id: int
    nome: str
    morada_id:int
    email: str
    morada: Morada


 */