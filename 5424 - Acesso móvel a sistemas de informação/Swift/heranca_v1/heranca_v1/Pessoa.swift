//
//  Pessoa.swift
//  heranca_v1
//
//  Created by Gonçalo Feliciano on 25/06/2024.
//

import Foundation


class Pessoa{
    
    var nome: String
    var idade: Int
    var email: String
    
    init(nome: String, idade: Int, email: String) {
        self.nome = nome
        self.idade = idade
        self.email = email
    }
    
    
    func getInfo() -> String{
        "nome: \(nome)\n\(idade)\n\(email)"
    }
    
    
}
