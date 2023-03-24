
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

for atividade in atividades:
    print()
    print(f"Alunos da atividade {atividade}")
    print("-" * 40)
    
    atividade_sala1 = set(escola["sala_1"]) & set(atividades[atividade])
    atividade_sala2 = set(escola["sala_2"]) & set(atividades[atividade])
    
    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)

    print("-" * 40)
    print()
    print("#" * 40)
