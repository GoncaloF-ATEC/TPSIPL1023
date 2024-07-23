import Cocoa

var lista = ["Ana", "Carlos", "Catia", "Rita"]


lista.filter {$0.lowercased().starts(with: "a")}
lista.filter {$0.lowercased().starts(with: "r")}
lista.filter {$0.lowercased().starts(with: "c")}
lista.filter {$0.lowercased().starts(with: "d")}

