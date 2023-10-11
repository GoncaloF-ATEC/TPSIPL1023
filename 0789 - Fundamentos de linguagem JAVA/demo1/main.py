"""

int - num inteiro
str - texto 
    " "
    ''
    """ """
    ''' '''
    
float / double - num decimal
bool - T / F

"""

nome = 0
print(nome)


nome = "João"
print(nome)


nome_aluno = "Carlos"

nome2 = 0




_nome = 10
print(_nome)

var_bool = True



print(var_bool)



my_name = bool(input("Qual o seu nome: ")) # lê um input e "converte" para bool

"""
comentario multi linha 
"""


# comentario linha

my_name2 = input("Qual o seu nome: ")

# "ola my_name2"
print("ola " + my_name2)
print("ola", my_name2)
print("ola", my_name2, "em 2023") # str formatada
print(f"ola {my_name2} em 2023") # str formatada




print("-" * 10, "Operações", "-" * 10)

"""

+ <- att 1 + att2
- <- att 1 - att2
/ <- att 1 / att2
* <- att 1 * att2


"""


soma1 = 10 + 10
print(soma1)

soma2 = 10 + 10.6
print(soma2)


# soma3 = 10 + "Joao" # neste contexto não e possivel
# print(soma3)


soma4 = "Joao" + "Carlos"
print(soma4)

soma5 = 10 + True
print(soma5)

soma6 = 10 + False
print(soma6)

# soma7 = "10" - "10"
# print(soma7)

#  " "1023" "
num_as_str = "o valor é \"1023\"  "
print(num_as_str)



media = 10
print(f"o joao foi aluno da \"ATEC\" com media de {media}")
