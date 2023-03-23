
from pprint import pprint 

__version__ = "0.1.1"
__author__ = "Paulo Felix"

escola = {
    "sala_1": ["Antonio", "Joaquim", "Pedro", "Maria", "Gustavo"],
    "sala_2": ["Paulo", "Luana", "Manuela", "Carlos"],
    "extra": {
        "aula_musica": ["Luana", "Manuela", "Pedro", "Maria"],
        "aula_ingles": ["Antonio", "Paulo", "Gustavo", "Luana"],
        "aula_danca": ["Manuela", "Joaquim", "Carlos"]
    }
}

atividades = {
    "Ingles": escola['extra']['aula_ingles'],
    "Musica": escola['extra']['aula_musica'],
    "Danca": escola['extra']['aula_danca'],
}

#pprint(atividades)

# Listar alunos em cada atividades por sala

for extra, sala in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    # sala1 que tem interseção com a atividade

    atividade_sala1 = set(escola["sala_1"]) & set(atividades)
#    atividade_sala2 = escola["sala_2"]  .intersection(atividade)

#    print("Sala1 ", atividade_sala1)
#    print("Sala2 ", atividade_sala2)

#    print()
#    print("#" * 40)
