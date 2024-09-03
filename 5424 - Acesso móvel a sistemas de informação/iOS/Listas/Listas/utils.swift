//
//  utils.swift
//  Listas
//
//  Created by Gonçalo Feliciano on 23/07/2024.
//

import Foundation



extension Array<Contacto>{
    
    mutating func addDummyData(){
        self.append(Contacto(nome: "Ana"))
        self.append(Contacto(nome: "Carlos"))
        self.append(Contacto(nome: "Claudia"))
        
    }
    
    
}


extension String{
    
    static var emptyString:String{
        ""
    }
}
