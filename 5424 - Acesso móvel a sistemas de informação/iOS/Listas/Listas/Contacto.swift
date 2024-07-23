//
//  Contacto.swift
//  Listas
//
//  Created by Gonçalo Feliciano on 23/07/2024.
//

import Foundation


class Contacto:Identifiable{
    
    var id = UUID() // exp:  550e8400-e29b-41d4-a716-446655440000
    var nome:String
    
    init(nome: String) {
        self.nome = nome
    }
    
    
}
