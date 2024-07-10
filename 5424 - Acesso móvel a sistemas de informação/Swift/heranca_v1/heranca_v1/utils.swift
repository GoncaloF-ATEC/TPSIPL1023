//
//  utils.swift
//  heranca_v1
//
//  Created by Gonçalo Feliciano on 25/06/2024.
//

import Foundation


extension Array{
    
    func getArrayType() -> [Any]{
        
        var aux:[Any] = []
        
        for i in self{
            
            aux.append(type(of: i))
        }
        
        print(type(of: aux))
        
        return aux
    }
    
    
   
    
}

extension Array<Int>{
    
    
    func media() -> Double{
        
        var sum:Int = 0
        
        for i in self {
            sum += i
        }
        
        return Double(sum) / Double(self.count)
    
    }
    
}
