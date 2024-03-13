"""
Para implementação dos loop propostos nos exercícios, decidi criar uma função genérica que se adapte as diversas situações apresentadas.
optei por criar uma função chamada regar que recebe alguns parâmetros em sua chamada e realiza o processamento de acordo com os mesmos.
"""

def regar(lista_de_plantas, planta_escolhida = 'todas', sentido = 'crescente'):
    """
    função para regar as plantas

    Parâmetros
    ----------
    lista_de_plantas : list
    planta_escolhida : string
    sentido : string
    """

    try:
        if planta_escolhida == 'todas': # parâmetro padrão, varre todo o array de plantas
            if sentido == 'crescente':
                for i in range(0, len(lista_de_plantas)):
                    print("Regando {} na posição {}".format(lista_de_plantas[i], i))
            elif sentido == 'decrescente':
                for i in range(len(lista_de_plantas)-1, -1, -1):
                    print("Regando {} na posição {}".format(lista_de_plantas[i], i))
        else:
            if sentido == 'crescente':
                for i in range(0, len(lista_de_plantas)):
                    if planta_escolhida not in lista_de_plantas[i]: # testa se a planta atual varrida pelo index é igual a planta escolhida
                        pass
                    else: # A planta atual varrida pelo index é igual a planta escolhida, então será impressa na saída
                        print("Regando {} na posição {}".format(lista_de_plantas[i], i))
            elif sentido == 'decrescente':
                for i in range(len(lista_de_plantas)-1, -1, -1):
                    if planta_escolhida not in lista_de_plantas[i]:
                        pass
                    else:
                        print("Regando {} na posição {}".format(lista_de_plantas[i], i))
        print('\n')
    except:
        print("Aconteceu algo errado...não conseguimos regar as plantas :( ")


# Caso 3
print ("Caso 3")
lista_de_plantas = ['tomate', 'tomate', 'tomate', 'batata', 'batata', 'batata']
regar(lista_de_plantas, 'batata')

# Caso 4
print ("Caso 4")
lista_de_plantas = ['tomate', 'tomate', 'batata', 'batata', 'tomate', 'tomate']
regar(lista_de_plantas, 'tomate')

# Caso 5
print ("Caso 5")
lista_de_plantas = ['tomate', 'batata', 'cenoura', 'tomate', 'batata', 'cenoura']
regar(lista_de_plantas, sentido='decrescente')