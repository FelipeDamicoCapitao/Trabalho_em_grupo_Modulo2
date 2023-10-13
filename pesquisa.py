######################################################################################################################################################
# Cores
# \033[style; text; back m
NCinza = "\033[1;30;1m"
NVermelho = "\033[1;31;1m"
NVerde = "\033[1;32;1m"
NAmarelo = "\033[1;33;1m"
NMagenta = "\033[1;34;1m"
NRosa = "\033[1;35;1m"
NCiano = "\033[1;36;1m"
NBranco = "\033[1;37;1m"
Corfim = "\033[m"


# ######################################################################################################################################################
# 1 Passo - definir perguntas

perg1 = "1. Você é usuario frequente de trem?"
perg2 = "2. Você acha que os trens da Supervia em todos os ramais estão em bom estado de conservação?"
perg3 = "3 Você acha que o valor da passagem está de acordo com o serviço oferecido? "
perg4 = "4. Você se sente seguro andando de trem? "
perg5 = "5. Os horários bem como as integrações nos ramais facilitam o dia a dia dos usuários? "

# ######################################################################################################################################################
# 3 Passo - Cria uma lista vazia para armazenar os resultados

lista_geral = []

# ######################################################################################################################################################
# 4 Passo - Cria uma Lista com varias Tuplas dentro, onde cada uma representa 1 entrevistado

def lista_candidatos():
    """
    1 - pega os valores de genero + 5 perguntas de questionario()
    2 - Cria uma tupla para cada entrevistado com as 7 variaveis
    3 - Adiona esta tupla na lista geral de entrevistados
    """
    gen = genero()
    resp1, resp2, resp3, resp4, resp5 = questionario()
    tupla_individual =  (idade, gen, resp1, resp2, resp3, resp4, resp5)
    lista_geral.append(tupla_individual)
    return lista_geral

# ######################################################################################################################################################
# 5 Passo - Função que define o genero

def genero():
    """
    # Pergunta o Genero + Prevenção de bug + transformação de resposta
    """
    while True:
        genero = input(f"{NVerde}\nQual o seu genero? [M/F/O]\n{NCinza}(M = Masculino, F = Feminino, O = Outros{Corfim})").upper()
        if genero == "M":
            genero = "Masculino"
            return genero
            break
        elif genero == "F":
            genero = "Feminino"
            return genero
            break
        elif genero == "O":
            genero = "Outros"
            return genero
            break
        else:
            print(f"{NVermelho} Digite apenas M, F ou O{Corfim}")
            
# ######################################################################################################################################################
# 6 Passo - Prevenção de bug e alteração de srintgs das 5 perguntas [Repetição]

def resposta():
    """
    # - Apresenta as opçoes
    #   Cria uma Função que trans forma os indicies 1,2 e 3 em Strings
    #   Previne bugs - respostas divergentes
    """

    print( f"{NAmarelo}1 - Sim{Corfim}")
    print( f"{NAmarelo}2 - Não{Corfim}")
    print( f"{NAmarelo}3 - Não sei Responder{Corfim}")

    while True:
        resposta = input(f"{NVerde}Selecione uma das opções acima [1/2/3]: {Corfim}")
        if resposta == "1":
            resposta = "Sim"
            return resposta
            break
        elif resposta == "2":
            resposta = "Não"
            return resposta
            break
        elif resposta == "3":
            resposta = "Não sei Responder"
            return resposta
            break
        else:
            print(f"{NVermelho} Digite apenas 1, 2 ou 3{Corfim}")

# ######################################################################################################################################################
# 7 Passo - Pergunta Genero + 5 perguntas do questionario

def questionario():
    """
    1 - Realiza as 5 perguntas + executa função bug e tranformação + armazena resposta
    2 - Retorna os 6 valores

    """


# Execução das 5 perguntas do Questionario
    print(f"\n{NCiano}{perg1}{Corfim}")
    resp1 = resposta()

    print(f"\n{NCiano}{perg2}{Corfim}")
    resp2 = resposta()

    print(f"\n{NCiano}{perg3}{Corfim}")
    resp3 = resposta()

    print(f"\n{NCiano}{perg4}{Corfim}")
    resp4 = resposta()

    print(f"\n{NCiano}{perg5}{Corfim}")
    resp5 = resposta()

#Retorna os 6 valores
    return(resp1, resp2, resp3, resp4, resp5)


# ######################################################################################################################################################
# Execução em looping - Pergunta Idade 

while True:

    idade  = input(f"{NVerde}\nQual a sua idade? {Corfim}")
        
    if idade  == "00":
        print (f"{NCiano}Obrigado, pesquisa encerrada{Corfim}")
        break
    else:
        try:
            idade = int(idade)
            if idade <= 0:
                print(f"{NVermelho}Digite um Numero inteiro maior que zero{Corfim}")
            else:
                lista_geral = lista_candidatos()
                print(f"{NCiano}\nSeguimos para o próximo cadastro{Corfim}")
                print(f"{NCiano}lembre-se, digite 00 para encerar a entrada de dados.{Corfim}")
        except:
            print(f"{NVermelho}Digite um Numero inteiro maior que zero{Corfim}")



# ######################################################################################################################################################
# Indice das Tuplas
# 0 - idade
# 1 - genero
# 2 - resposta1
# 3 - resposta2
# 4 - resposta3
# 5 - resposta4
# 6 - resposta5

print(lista_geral)