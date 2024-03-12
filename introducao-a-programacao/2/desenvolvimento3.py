"""
Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
"""
def main():
    loop_for()
    loop_while()

def loop_for():
    print("##########################")
    print("Implementação com loop for")
    print("##########################")
    for i in range(21):
        if (i == 0):
            print("Térreo")
        elif (i != 13):
            print("{}° andar".format(i))
    print("")
    
def loop_while():
    print("##########################")
    print("Implementação com loop while")
    print("##########################")
    i = 20
    while (i >= 0):
        if ((i != 13) and (i != 0)):
            print("{}° andar".format(i))
        if (i == 0):
            print("Térreo")
        i = i - 1
    print("")

main()