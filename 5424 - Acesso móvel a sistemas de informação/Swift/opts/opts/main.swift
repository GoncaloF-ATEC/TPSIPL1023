//
//  main.swift
//  opts
//
//  Created by Gonçalo Feliciano on 28/05/2024.
//

import Foundation

// tuplos

var tp1 = ("Gonçalo", 10, true)

print(tp1.0)

tp1.0 = "Novo nome"


var tp2:(String, Int, Bool)

tp2 = ("Gonçalo", 10, true)
tp2 = tp1

print(tp2)
tp1.0 = "Ana"
print(tp2)

print(tp1.0)

print("---------")

var tp3 = (nome:"Gonçalo", media:10, aprovado:true)

print(tp3.nome)
print(tp3.0)
print("---------")
var tp4:(String, Int, Bool)

tp4 = (nome:"Gonçalo", media:10, aprovado:true)

print(tp4.0)

print("---------")
var tp5:(nome:String, media:Int, estado:Bool)
tp5 = ("Gonçalo", 10, true)

print(tp5.nome)
print(tp5.0)
print("---------")

var tp6:(nome:String, media:Int, estado:Bool)

tp6 = (nome:"Gonçalo", media:10, estado:true)

tp6 = (nome:"Gonçalo", media:10, estado:true)

print("---------")
print("---------")

// opts

// Int ≠ Int?  <- tipos de dados dif


var idade:Int? // -> nil
var idade2:Int // -> -----

//print(idade)

idade = 10

idade = nil


//aceder ao valor unwrapping
print("-----unwrapping ->  ! ----")


// !



print(Int("10000")!)

print("-----unwrapping ->  ??  ----")
// ??



print(Int("10000") ?? 0)
print(Int("10_000") ?? 0)

// if let
print("-----unwrapping ->  if let  ----")

var f:String? = "Var com valor"

if let myF = f{
    print(myF)
    
}else{
    print("Sem valor")
}


if let f { // <=> if let f = f {
    print(f)
    
}else{
    print("Sem valor")
}


print("-----unwrapping ->  if let -> v2  ----")
var num: Int? = 5

if let num, num % 2 == 0 {
    print("\(num) existe e é par")
    
}else{
    print("Sem valor ou é impar")
}


// gaurd -> falar dps de funcs

print("-----unwrapping ->  gaurd  ----")

func teste(nota:Int? = nil){
    
    guard let nota else{ // <=>  guard let nota = nota else{
        print("nota sem valor")
        return
    }
    
    print(nota)
    
    print("codigo, codigo e mais codigo")
    
}


teste(nota: nil)
teste()
teste(nota: 31)

// Null -> None -> nil



// funcs

print("---- funcs ----")

func info(nome:String, ano:Int) -> String {
    
    var msg = "nome: \(nome), ano: \(ano)"
    
    return msg
}


func info2(nome:String, ano:Int) -> String {
    "nome: \(nome), ano: \(ano)" // <=> return "nome: \(nome), ano: \(ano)"
}

let resp = info(nome: "Gonçalo", ano: 2024)

print(resp)



func soma2(n1 valor1:Int, n2 valor2:Int) -> Int{
    valor1 + valor2
}

let f3 = soma2(n1: 3, n2: 3)



func soma(_ valor1:Int, com valor2:Int) -> Int{
    valor1 + valor2
}
let f1 = soma(59, com: 2)





