while True:
    print("""
    ===================================
    ============ Menu Cool ============
    ===================================
    
    Opeção1 ------------------------- 1 
    Opeção2 ------------------------- 2
    Opeção3 ------------------------- 3
    Sair ---------------------------- 0
    
    ===================================
    """)

    opt = int(input("Selecione uma opeção: "))

    match opt:
        case 1:
            print("selecionou a opeção 1")
        case 2:
            print("selecionou a opeção 2")
        case 3:
            print("selecionou a opeção 3")
        case 0:
            print("Vai sair do programa")
            break # termina o loop em qualquer momento
        case _:
            print("selecionou uma opção invalida")