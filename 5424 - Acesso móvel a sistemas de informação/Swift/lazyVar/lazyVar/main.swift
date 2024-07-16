//
//  main.swift
//  lazyVar
//
//  Created by Gonçalo Feliciano on 11/06/2024.
//

import Foundation

class foo{
    
   lazy var sum = self.soma()
    var escola = "ATEC"
    

    func soma() -> Int{
        var soma = 0
        for i in 0...100_000_000{
            soma += i
       
        }
        
        return soma
    }
}


print("e o porgrama inicia")


var f = foo()
print(f.escola)

print("e o porgrama continua1")

print(f.sum)

print("e o porgrama continua2")
