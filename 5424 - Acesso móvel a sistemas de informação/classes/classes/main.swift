//
//  main.swift
//  classes
//
//  Created by Gonçalo Feliciano on 11/06/2024.
//

import Foundation


print("-----class------")

var ct = Contacto(nome: "Carlos", telefone: 1213214234, email: nil )
print(ct.nome)
print(ct)

var c1 = ct
c1.nome = "Novo nome"

print(c1.nome)
print(ct.nome)
print("-----")
print(ct.email ?? "")
print("----")
print(c1 === ct) // === comp reef

// print(c1 == ct) <- no futuro....

print("----")
var ct12 = Contacto(nome: "Carlos", telefone: 1213214234 )


print(ct12 === ct)
print("----")


print(c1.getInfo())
print(ct12.getInfo())

print("-----struct------")
var ct2 = Contacto2(nome: "Carlos", telefone: 1213214234)
print(ct2.nome)
print(ct2)

var c2 = ct2
c2.nome = "Novo nome"

print(c2.nome)
print(ct2.nome)

print("-----------------------------------------------------------")


Aegenda.shared.addContacto(ct: [c1, ct, ct12])

Aegenda.shared.listContactos()

