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

