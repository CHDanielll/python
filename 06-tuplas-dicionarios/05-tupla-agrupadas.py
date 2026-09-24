alunos = (
    ("carlos", 17),
    ("ana", 18),
    ("joão", 16)

) 

print(alunos[0])

print(alunos[0][0])

print(alunos[0][1])

for aluno in alunos: 
    print("-------------------")
    print("nome: ", aluno[0])
    print("Idade: ", aluno[1])
    print("-------------------")