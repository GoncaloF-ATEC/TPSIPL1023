contador = 3

while contador < 10:

    contador += 2

    print(f"bloco - {contador} ")

print("Fim do loop")

print("------------while continue------------------")
while contador < 20:

    contador += 1

    if contador % 2 == 0:
        continue

    print(contador)


