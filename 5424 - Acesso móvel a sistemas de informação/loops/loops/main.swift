//
//  main.swift
//  loops
//
//  Created by Gonçalo Feliciano on 04/06/2024.
//

import Foundation

// for



var r = 0...9 // range(0, 10) -> 0 a 10

var r2 = 0 ..< 9 // range(0, 9) -> 0 a 9



for i in 0..<10 {
    print(i, terminator: "-")
}

print("\n")


func teste(_ bla: Int) -> Bool{
    return  bla % 2 == 0
    
}


var f = 1
for i in 0...100 where teste(i) {
    
    
    if i == 10 || i == 20{
        continue
    }
    
    if i == 26{
        break
    }
    
    print(i)
}

/*
for i in 0...100 {
    if i % 2 == 0{
        print(i)
    }
}
 */

// while () {}



/*
repeat{
    
}while()
*/




var val = 10
switch val{
case 10:
    print("val: 10")
    fallthrough
    
case 15:
    print("val: 15")
case 20:
    print("val: 20")
    
default:
    print("Outro val")
    
}
