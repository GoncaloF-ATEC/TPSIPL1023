//
//  main.swift
//  heranca_v1
//
//  Created by Gonçalo Feliciano on 25/06/2024.
//

import Foundation



var al = Aluno(nome: "Carlos", idade: 20, email: "foo@sapo.pt", turma: "TPSI")
var al2 = Aluno(nome: "Rita", idade: 20, email: "Rita@sapo.pt", turma: "TPSI")

var porf = Professor(nome: "João", idade: 30, email: "jcp@atec.pt", listaTurmas: ["turma do joao"])
var porf2 = Professor(nome: "Maria", idade: 50, email: "mcp@atec.pt")


var p = Pessoa(nome: "Ana", idade: 23, email: ".....")

var lista = [al, al2, porf, porf2]

print(type(of: lista))

print("-----------------------------")

for p in lista{
    
    if p is Professor{

        let p2 = p as! Professor
        
        p2.funcDoProfessor()
    
    }
}

print("-----------------------------")


for p in lista{
    
    guard let p2 = p as? Professor, p2.listaTurmas.isEmpty else {
        print("\(p.nome) não é Porfessor ou é um Porfessor ja com turma")
        continue
    }
    p2.listaTurmas.append("Nova turma")
}

print("-----------------------------")

for p in lista{
    
    if p is Professor{

        let p2 = p as! Professor
        
        print(p2.getInfo())
    
    }
}

print("-----------------------------")


print(lista.getArrayType())
print("-----------------------------")


var notas = [10, 13, 14, 9, 19, 18]
print(notas.media())

var notas2 = [10, 13]
print(notas2.media())


lista.getArrayType()
