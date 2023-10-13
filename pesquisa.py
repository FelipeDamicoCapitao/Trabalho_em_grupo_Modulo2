######################################################################################################################################################
import csv
import datetime
from time import sleep as espera
import os


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

perg1 = "1) Você é usuario frequente de trem?"
perg2 = "2) Você acha que os trens da Supervia em todos os ramais estão em bom estado de conservação?"
perg3 = "3) Você acha que o valor da passagem está de acordo com o serviço oferecido? "
perg4 = "4) Você se sente seguro andando de trem? "
perg5 = "5) Os horários bem como as integrações nos ramais facilitam o dia a dia dos usuários? "

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
    data_e_hora_atual = datetime.datetime.now() 
    data_formatada = data_e_hora_atual.strftime('%Y-%m-%d')
    hora_formatada = data_e_hora_atual.strftime('%H:%M:%S')
    tupla_individual =  (idade, gen, resp1, resp2, resp3, resp4, resp5, data_formatada, hora_formatada)
    lista_geral.append(tupla_individual)
    return lista_geral

# ######################################################################################################################################################
# 5 Passo - Função que define o genero

def genero():
    """
    # Pergunta o Genero + Prevenção de bug + transformação de resposta
    """
    while True:
        print (f"\n{NCiano}B - Qual o seu genero? {Corfim}")
        print(f"{NAmarelo}1 = Masculino\n2 = Feminino\n3 = Não Binario{Corfim}")
        genero = input(f"{NVerde}Selecione entre as opções [1/2/3]:{Corfim}")
        if genero == "1":
            genero = "Masculino"
            return genero
            break
        elif genero == "2":
            genero = "Feminino"
            return genero
            break
        elif genero == "3":
            genero = "Não Binario"
            return genero
            break
        else:
            espera(0.2)
            print(f"{NVermelho}Digite apenas 1, 2 ou 3 de acordo com os indices{Corfim}")
            
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
            resposta = "Nao"
            return resposta
            break
        elif resposta == "3":
            resposta = "Nao sei Responder"
            return resposta
            break
        else:
            espera(0.2)
            print(f"{NVermelho} Digite apenas 1, 2 ou 3{Corfim}")

# ######################################################################################################################################################
# 7 Passo - Pergunta Genero + 5 perguntas do questionario

def questionario():
    """
    1 - Realiza as 5 perguntas + executa função bug e tranformação + armazena resposta
    2 - Retorna os 6 valores

    """


# Execução das 5 perguntas do Questionario
    padrao()
    print(f"\n{NCiano}{perg1}{Corfim}")
    resp1 = resposta()

    padrao()
    print(f"\n{NCiano}{perg2}{Corfim}")
    resp2 = resposta()

    padrao()
    print(f"\n{NCiano}{perg3}{Corfim}")
    resp3 = resposta()

    padrao()
    print(f"\n{NCiano}{perg4}{Corfim}")
    resp4 = resposta()

    padrao()
    print(f"\n{NCiano}{perg5}{Corfim}")
    resp5 = resposta()
    limpar_tela()

#Retorna os 5 valores
    return(resp1, resp2, resp3, resp4, resp5)

# ######################################################################################################################################################
# Separação de cabeçalho

def sep(X):
    L = 80

    Y = int(((L-len(X)))/2)
    Y2 = (" "*Y)
    espera(0.2)
    print("")
    print(f"{NBranco}={Corfim}"*L)
    print(f"{Y2}{NBranco}{X}{Corfim}")
    print(f"{NBranco}={Corfim}"*L)
    print("")

# divisão de uma linha
def sep3():
    L = 80
    Y2 = (" "*L)
    print("")
    print(f"{NCinza}={Corfim}"*L)

import os

def limpar_tela():
    os.system('cls')

def padrao():
    limpar_tela()
    espera(0.4)


# ######################################################################################################################################################
# Execução em looping - Pergunta Idade 

X = "Supervia - Avaliação de Clientes"
sep(X)
espera(0.2)
print(f"{NBranco}Seja bem vindo ao questionario de avaliação da Supervia\nDaremos inicio ao cadastro do primeiro cliente: {Corfim}")

while True:
    espera(0.2)
    print (f"{NCiano}\nA - Qual a sua idade? {Corfim}")
    idade  = input(f"{NVerde}Digite sua idade: {Corfim}")
        
    if idade  == "00":
        espera(0.2)
        X = "Obrigado, pesquisa encerrada"
        sep(X)
        break
    else:
        try:
            idade = int(idade)
            if idade <= 0:
                espera(0.2)
                print(f"{NVermelho}Digite um Numero inteiro maior que zero{Corfim}")
            else:
                lista_geral = lista_candidatos()
                print (f"{NCiano}\nDados cadastrados com sucesso!\nAguarde um instante.")
                espera(3)
                limpar_tela()
                sep(X)
                print(f"{NBranco}Seguimos para o próximo cadastro.{Corfim}")
                print(f"{NBranco}Lembre-se, digite 00 para encerar a entrada de dados.{Corfim}")
        except:
            espera(0.2)
            print(f"{NVermelho}Digite um Numero inteiro maior que zero{Corfim}")



# ######################################################################################################################################################
# Criando Arquivo CSV
# 0 - idade
# 1 - genero
# 2 - resposta1
# 3 - resposta2
# 4 - resposta3
# 5 - resposta4
# 6 - resposta5
# 7 - Data e Hora de cadastro


with open('pesquisa.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escreva os cabeçalhos (opcional)
    cabeçalhos = ['Idade', 'Genero', 'Pergunta 1', 'Pergunta 2', 'Pergunta 3', 'Pergunta 4', 'Pergunta 5', "Data da entrevista", "Hora da entrevista"]
    escritor_csv.writerow(cabeçalhos)

    
    for linha in lista_geral:
        escritor_csv.writerow(linha)






