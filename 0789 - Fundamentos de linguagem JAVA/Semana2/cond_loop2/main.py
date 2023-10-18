# condições

"""

int i = 1;
int n = 10

if(n == 10){

    int i = 3

    i *= 3
    print(i) <- 9

}else if(n == 15){

}else{

}

print(i) <- 1

"""


#if

num = 10
"""
if (num == 10){
    print("num = 10")
}
"""


""" 
if num == 10:
    print("num = 10")
else:
    print("Outro valor")

# match <- swith  py 3.10


match num:
    case 5:
        print("Match - num = 10")
    case 15:
        print("Match - mum = 15")

"""


nota1 = float(input("nota1: "))
nota2 = float(input("nota1: "))
nota3 = float(input("nota1: "))
nota4 = float(input("nota1: "))

soma = nota1 + nota2 + nota3 + nota4

media = soma / 4

print(f" media e de {media}")

if media >= 9.5:
    print(f"o Aluno foi apovado com {media}")
else:
    print(f"O aluno tem de estudar mais, teve media de {media}")


print("\n\nMais de 8 pode fazer um exame oral\n\n")

if media >= 9.5:
    print(f"o Aluno foi apovado com {media}")
elif media >= 8: # else if
    print(f"o Aluno tem de ir a oral teve media de {media}")
else:
    print(f"O aluno tem de estudar mais, teve media de {media}")


"""
==
>
<
>=
<=

and (&&)
or ( || )
not ( ! )

"""

if not (True and False): # if not (False) -> if not False -> if True
    print("True")
else:
    print("False")



if not ((not False or False) and not False):
    # if not ((True or False) and not False):
    # if not ((True) and not False):
    # if not (True and not False):
    # if not (True and True):
    # if not (True):
    # if not True:
    #if False:
    print("")
else:
    print("")






print("\n\nmatch\n\n")

mes = 2

match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")

# loops