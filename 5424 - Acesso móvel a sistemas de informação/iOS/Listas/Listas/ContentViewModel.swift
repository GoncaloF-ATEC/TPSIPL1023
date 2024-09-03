//
//  ContentViewModel.swift
//  Listas
//
//  Created by Gonçalo Feliciano on 23/07/2024.
//

import Foundation


class ContentViewModel: ObservableObject{
    
    @Published var listaContactos: [Contacto]
    @Published var newName:String = .emptyString
    @Published var showErroe = false
    private var _startChar:Set<String> = []{
        didSet{
            newName = .emptyString
        }
        
    }
    var startChar:[String]{
        Array(_startChar).sorted()
        
    }
    
    
    init(listaContactos: [Contacto] = []) {
        self.listaContactos = listaContactos
        
    }
    
    
    
    func getContactosStarted(by char: String) -> [Contacto]{
        
        listaContactos.filter({$0.nome.lowercased().starts(with: char)})
    }
    
    
    func addNome(){
        
        if !newName.isEmpty{
            let ct = Contacto(nome: self.newName)
            
            _startChar.insert(ct.nome.first!.lowercased())
            
            
            self.listaContactos.append(ct)
        }else{
            self.showErroe.toggle()
        }
     
        
    }
    
    
    
}
