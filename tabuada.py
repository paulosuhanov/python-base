
"""Imprime a tabuada do 1 ao 10"""
__version__ = "0.1.1"
__author__ = "Paulo"



#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1, 11))

 # iterable (percorriveis)

for n1 in numbers:
    print("{:-^18}".format(f"Tabuada do {n1:02d}"))
    print()
    for n2 in numbers:
        result = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {result}"))
    print("#" * 18)

