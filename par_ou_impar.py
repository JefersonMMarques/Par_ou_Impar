'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''

numero = input('Digite um número inteiro: ')

if numero.isdigit():
    if int(numero) % 2 == 0:
        print(f'número {numero} é par.')
    else:
        print(f'número {numero} é ímpar.')
else:
    print("Você não digitou um número inteiro.")
