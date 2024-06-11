//
//  Quadrado.swift
//  porp
//
//  Created by Gonçalo Feliciano on 11/06/2024.
//

import Foundation


class Quadrado{
    private var _lado: Float{
        willSet{
            print("a var area vai mudar de \(_lado) para \(newValue)")
        }
        
        didSet{
            print("a var area mudou de \(oldValue) para \(_lado)")
            // log
        }
    }
    
    var lado:Float{
        get{
            _lado
        }
    }
    

    var area:Float{
        get{
            pow(self._lado, 2)
        }
        
        set{
            self._lado = sqrtf(newValue)
        }
    }
    
    
    var pereimetro:Float{
        set{
            self._lado = newValue / 4
        }
    
        
        get{
            self._lado * 4
        }
        
        
    }
    
    
    
    
    
    
    
    init(lado: Float) {
        self._lado = lado
    }
    
    
    
    
    
    
    
}
