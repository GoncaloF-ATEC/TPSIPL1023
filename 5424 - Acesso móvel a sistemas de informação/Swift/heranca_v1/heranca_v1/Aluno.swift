//
//  Aluno.swift
//  heranca_v1
//
//  Created by Gonçalo Feliciano on 25/06/2024.
//

import Foundation


class Aluno: Pessoa{
    
    
    var turma: String
    
    
    init(nome: String, idade: Int, email: String, turma: String) {
    
        
        self.turma = turma
        super.init(nome: nome, idade: idade, email: email)

    }
    
    func funcDoAluno(){}
    
    func funcEmComum(){}
    
    override func getInfo() -> String {
        "nome: \(nome)\n\(idade)\n\(email)\n\(turma)"
    }
    
    
}
