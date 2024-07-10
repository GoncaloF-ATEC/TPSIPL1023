//
//  Contacto.swift
//  classes
//
//  Created by Gonçalo Feliciano on 11/06/2024.
//

import Foundation

class Contacto{
    
    static var id = 12344
    
    var nome: String
    var telefone: Int
    var email: String?
    
    
    init(nome: String, telefone: Int) {
        self.nome = nome
        self.telefone = telefone
        self.email = "sem email"
    }
    
    
    init(nome: String, telefone: Int, email: String? = nil) {
        self.nome = nome
        self.telefone = telefone
        self.email = email
    }
   
    func getInfo() -> String{

        "nome: \(self.nome) \t - \(self.telefone)"
        
    }
   
}

struct Contacto2{
    
    var nome: String
    var telefone: Int
    var email: String?
    
}
