

__version__ = "0.1.0"
__author__ = "Paulo Felix"

sala_1 = ["Antonio", "Joaquim", "Pedro", "Maria", "Gustavo"]
sala_2 = ["Paulo", "Luana", "Manuela", "Carlos"]

aula_musica = ["Luana", "Manuela", "Pedro", "Maria"]
aula_ingles = ["Antonio", "Paulo", "Gustavo", "Luana"]
aula_danca = ["Manuela", "Joaquim", "Carlos"]

atividades = [
    ("Ingles", aula_ingles),
    ("Musica", aula_musica),
    ("Danca", aula_danca),
]

# Listar alunos em cada atividades por sala

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala_1:
            atividade_sala1.append(aluno)
        elif aluno in sala_2:
            atividade_sala2.append(aluno)

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)

    print()
    print("#" * 40)
