//
//  utils.swift
//  demo
//
//  Created by Gonçalo Feliciano on 10/07/2024.
//

import Foundation



extension Int{
    
    func toDouble() -> Double{
        Double(self)
    }
    
    
    func normalizar() -> Double{
        self.toDouble()/255.toDouble()
    }
    
    
}
