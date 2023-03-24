#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9
"""

__version__ = "0.1.0"

import sys
arguments = {
    'operacao': None,
    'n1': None,
    'n2': None,
}
operacoes = ('sum', 'sub', 'mul', 'div')

user_operacao = 0
user_n1 = 0
user_n2 = 0
result = 0

if len(sys.argv[1:]) == 0:
    user_operacao = input("operação: ")
    user_n1 = int(input("n1: "))
    user_n2 = int(input("n2: "))
else:
    user_operacao = sys.argv[1]
    user_n1 = int(sys.argv[2])
    user_n2 = int(sys.argv[3])

if user_operacao == operacoes[0]:
    simbol = "+"
    result = user_n1 + user_n2
elif user_operacao == operacoes[1]:
    simbol = "-"
    result = user_n1 - user_n2
elif user_operacao == operacoes[2]:
    simbol = "*"
    result = user_n1 * user_n2
elif user_operacao == operacoes[3]:
    simbol = "/"
    result = user_n1 / user_n2
    
print(f"{user_n1} {simbol} {user_n2} = {result}")

# for arg in sys.argv[1:]:
# #     # TODO: Tratar ValueError
#     operacao, n1, n2 = arg.split()
#     print(operacao)
#     print(n1)
#     print(n2)
# #     value = value.strip()
# #     if key not in arguments:
# #         print(f"Invalid Option`{key}`")
# #         sys.exit()
# #     arguments[key] = value


# # print(sys.argv[2])