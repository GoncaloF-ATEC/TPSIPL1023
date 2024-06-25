//
//  main.swift
//  heranca_v1
//
//  Created by Gonçalo Feliciano on 25/06/2024.
//

import Foundation



var al = Aluno(nome: "Carlos", idade: 20, email: "foo@sapo.pt", turma: "TPSI")
var al2 = Aluno(nome: "Rita", idade: 20, email: "Rita@sapo.pt", turma: "TPSI")

var porf = Professor(nome: "João", idade: 30, email: "jcp@atec.pt")
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
    
    guard let p2 = p as? Professor else {
        print("\(p.nome) não é Porfessor")
        continue
    }
    p2.funcDoProfessor()
    
}
