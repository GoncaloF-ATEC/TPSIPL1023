#F aça um Programa que verifique se uma letra digitada é vogal ou consoante.


letra = input("Digite uma letra: ")

match letra:
    case "a":
        print("vogal")
    case "e":
        print("vogal")
    case "i":
        print("vogal")
    case "o":
        print("vogal")
    case "u":
        print("vogal")
    case _: # caso predefinido e opctional
        print("Consoante")




if letra == "a" or letra == "b":
    print("If a var é a ou b")
else:
    print("If outra letra")