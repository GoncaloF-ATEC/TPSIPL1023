

print("Hello, World!")

var nome = "Gonçalo"
print(nome)

let idade = 30

nome = "33"
print(nome)


var nome2:String
nome2 = "novo contudo"



var i = 10
var d = 10.2
var f:Float =  10.2

var soma = Double(i) + d

print(soma)

print("a soma é " + String(soma))
print("a soma é \(soma)")


var nome1 = 10
var _nome = 12
var _nome2 = 12
//var 1nome = 10
//var $teste = 10
var 🐶 = "Gato"
print(type(of: 🐶))
var π = 3.141519
var 读写汉字 = "（书、杂志等中区别于图片的）正文，文字材料, （移动电话或传呼机发送的）短消息，短信（同text message）, （学习某课程必读的）课本，教科书"

print(读写汉字)



var idade1 = 10
if idade1 == 10{
    
    print("idade = 10")
    
}else if idade >= 18{
    print("idade >= 18")
    
}else{
    print("idade não 10")
}


print(Int.min)
print(Int.max)

var dia = 1
switch(dia){
case 1:
    print("Domingo")
    fallthrough
case 2:
    print("2f")
case 3:
    print("3f")
default:
    print("dia invalido")
}
print("Pos swift")

// ler do teclado

print("qual o seu nome? ")
var nome3 = readLine()!

print("o seu nome é \(nome3)")


print(Int("10")!)
print("--------------------")
var tp = ("Gonçalo", 10, false)

print(tp.0)
print(tp.1)
print(tp.2)
print("--------------------")

var tp2 = (nome:"Gonçalo",anos: 10, ativo:false)


print(tp2.nome)
print(tp2.0)
print("--------------------")

tp2.nome = "Novo Nome"
print(tp2)

print("--------------------")

var tp3:(String, Int, Bool)

var tp4:(nome:String, anos:Int, ativo:Bool)


tp3 = (nome:"Gonçalo",anos: 10, ativo:false)
print(tp3.0)


tp4 = ("Gonçalo", 110, false)
print(tp4.anos)

var soma22 = 3 + 4

var k = 0

k += 1
k += 4
k -= 1
k *= 1


//saasd
/*
 
 adsad
 dsadasd
 sasa
 d
 */
