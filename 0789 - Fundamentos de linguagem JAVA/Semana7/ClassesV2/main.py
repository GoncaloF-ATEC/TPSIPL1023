from Escola import Escola


atec = Escola("ATEC")

atec.criar_aluno("Gonçalo", 18, "TPSIPL1023")
atec.criar_aluno("Maria", 18, "TPSIPL1023")

atec.cirar_turma("GRSIPL", 1022)

atec.criar_aluno("Maria", 18, "GRSIPL1022")

atec.show_turmas()
atec.show_Alunos()


atec.turmas[0].nome = "Outra Turma"

atec.show_Alunos()


