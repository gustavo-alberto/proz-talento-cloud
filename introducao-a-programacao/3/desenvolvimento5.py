"""
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 
"""

def calculadora():
    loop_flag = True
    options_list = [1,2,3,4,0]

    while (loop_flag):
        print("########## Calculadora ##########")
        print("Operações")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")
        option = int(input("Escolha uma opção: "))

        if option not in options_list:
            print("Essa opção não existe\n")
        
        if option == 1:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            result = num1 + num2
            print("{} + {} = {}\n".format(num1, num2, result))
        if option == 2:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            result = num1 - num2
            print("{} - {} = {}\n".format(num1, num2, result))
        if option == 3:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            result = num1 * num2
            print("{} * {} = {}\n".format(num1, num2, result))
        if option == 4:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            result = num1 / num2
            print("{} / {} = {}\n".format(num1, num2, result))
        if option == 0:
            loop_flag = False

calculadora()