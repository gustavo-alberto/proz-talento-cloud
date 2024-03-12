"""
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
"""

def main():
    nome = input("Digite seu nome completo: ")

    try:
        ano_nascimento = int(input("Digite o seu ano de nascimento: "))
        if (ano_nascimento < 1922) or (ano_nascimento > 2023):
            main()
        idade = 2024 - ano_nascimento
        print("Nome completo: {}".format(nome))
        print("Completará {} anos em 2024".format(idade))
    except:
        print("Erro")
        main()

main()