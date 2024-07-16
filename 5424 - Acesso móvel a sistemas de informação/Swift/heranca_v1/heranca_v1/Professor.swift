//
//  Professor.swift
//  heranca_v1
//
//  Created by Gonçalo Feliciano on 25/06/2024.
//

import Foundation


class Professor: Pessoa{
    
    var listaTurmas:[String]
    
    init(nome: String, idade: Int, email: String, listaTurmas: [String] = []) {
        self.listaTurmas = listaTurmas
        super.init(nome: nome, idade: idade, email: email)
    }
    
    func funcDoProfessor(){
        print("funcDoProfessor")
    }
    
    func funcEmComum(){}
    
    override func getInfo() -> String {
        "\(super.getInfo())\n\(listaTurmas)"
    }
    
}
