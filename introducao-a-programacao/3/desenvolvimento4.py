"""
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
"""

def calculadora(num1, num2, operation: int):
    '''
    Função que calcula dois números

    Parameters
    ----------
    num1 : primeiro número
    num2 : segundo número
    operation (int): operação a ser realizada (1.Soma, 2.Subtração, 3.Multiplicação, 4.Divisão)

    Returns:
    result (float): Retorna um valor numérico 
    '''

    # Array com as opções de operação disponíveis
    options = [1,2,3,4]

    if operation not in options:
        result = 0
    if operation == 1:
        result = num1 + num2
    if operation == 2:
        result = num1 - num2
    if operation == 3:
        result = num1 * num2
    if operation == 4:
        result = num1 / num2        
    return result

# Soma
print(calculadora(1,1,1))

# Subtração
print(calculadora(1,1,2))

# Multiplicação
print(calculadora(1,1,3))

# Divisão
print(calculadora(1,1,4))

# Zero
print(calculadora(1,1,5))