//
//  Agenda.swift
//  classes
//
//  Created by Gonçalo Feliciano on 11/06/2024.
//

import Foundation


class Aegenda{
    
    static var shared = Aegenda()
    
    
    var listaContatos:[Contacto]
    
    init() {
        self.listaContatos = []
    }
    
    func addContacto(ct: Contacto){
        self.listaContatos.append(ct)
    }
    
    func addContacto(ct: [Contacto]){
        self.listaContatos.append(contentsOf: ct)
    }
    
    func listContactos(){
        
        for ct in self.listaContatos{
            print(ct.getInfo())
            
        }
        
    }
    
    
    
}
