//
//  ContentViewModel.swift
//  2_demo_ui_2
//
//  Created by Gonçalo Feliciano on 16/07/2024.
//

import Foundation

class ContentViewModel: ObservableObject{
    @Published var nome: String
    @Published var nomeTF: String
    @Published var erro = false{
        didSet{
            print("Erro - \(erro)")
        }
    }
    
    
    init(nome: String = "" , nomeTF: String = "" ) {
        self.nome = nome
        self.nomeTF = nomeTF
    }
    
    
    func mudarNome(){
        if self.nomeTF.isEmpty{
            self.erro.toggle()
            return
        }
        self.nome = self.nomeTF
        self.nomeTF = ""
    }
    
    
    func setName(){
        self.nome = "Sem nome"
        
    }
    
    
}
