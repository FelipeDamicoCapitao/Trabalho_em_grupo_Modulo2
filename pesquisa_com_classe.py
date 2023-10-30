######################################################################################################################################################
import csv
import datetime
from time import sleep as espera
import os

######################################################################################################################################################
def limpar_tela():
    os.system('cls')

######################################################################################################################################################
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
# ######################################################################################################################################################

class Pesquisa:
    X = "Supervia - Avaliação de Clientes"
    sep(X)
    espera(0.2)
    print(f"{NBranco}Seja bem vindo ao questionario de avaliação da Supervia\nDaremos inicio ao cadastro do primeiro cliente: {Corfim}")

# ##################################################
# Atributos da pesquisa = respostas
    def __init__(self):
        self.respostas = []
    
# ##################################################
# metodos = ações/manupulações para encontrar respostas

#A - Funções que serão executados externamente
#B - Funções alimentadores das funções A
#C - Funções complementadores

# A1 - Agrupa Dados em Lista - Coleta B1,B2 eB3
    def coletar_respostas(self):
        while True:
            # Retorna idade
            idade = self.f_idade()
            if idade == "00": # fim de programa
                break
            else: 
                # Retorna Genero
                genero = self.f_genero()
                limpar_tela()

                # Retorna Perguntas
                respostas_perguntas = self.f_perguntas()
                limpar_tela()

                #Define data e hora
                data_e_hora_atual = datetime.datetime.now() 
                data_formatada = data_e_hora_atual.strftime('%d/%m/%Y')
                hora_formatada = data_e_hora_atual.strftime('%H:%M:%S')

                #Cria uma tupla pra cada entrevistado e adiciona no atributo resposta
                self.respostas.append(([idade, genero] + respostas_perguntas + [data_formatada,hora_formatada]))
                
                #Executa menssagem de termino e inicio de nova entrevista
                self.menssagem_de_fim_e_inicio()

# B1 - Define idade:                                  
    def f_idade(self):
        while True:
            espera(0.2)
            print (f"{NCiano}\nA - Qual a sua idade? {Corfim}")
            idade  = input(f"{NVerde}Digite sua idade: {Corfim}")
                
            if idade  == "00":
                espera(0.2)
                X = "Obrigado, pesquisa encerrada"
                sep(X)
                return idade
            else:
                try:
                    idade = int(idade)
                    if idade <= 0: # Prevenção de Bug
                        espera(0.2)
                        print(f"{NVermelho}Digite um Numero inteiro maior que zero!{Corfim}")
                    else:
                        return idade
                except: # Prevenção de Bug
                    espera(0.2)
                    print(f"{NVermelho}Digite um Numero inteiro maior que zero{Corfim}")

# B2 - Define genero:           
    def f_genero(self):
        while True:
            print (f"\n{NCiano}B - Qual o seu genero? {Corfim}")
            print(f"{NAmarelo}1 = Masculino\n2 = Feminino\n3 = Não Binario{Corfim}")
            genero = input(f"{NVerde}Selecione entre as opções [1/2/3]:{Corfim}")
            if genero == "1":
                genero = "Masculino"
                return genero
            
            elif genero == "2":
                genero = "Feminino"
                return genero
            
            elif genero == "3":
                genero = "Não Binario"
                return genero
            
            else: # Prevenção de Bug
                espera(0.2)
                print(f"{NVermelho}Digite apenas 1, 2 ou 3 de acordo com os indices{Corfim}")

# B3 - Define Perguntas - Coleta CB1
    def f_perguntas(self):
        perg1 = "1) Você é usuario frequente de trem?"
        perg2 = "2) Você acha que os trens da Supervia em todos os ramais estão em bom estado de conservação?"
        perg3 = "3) Você acha que o valor da passagem está de acordo com o serviço oferecido? "
        perg4 = "4) Você se sente seguro andando de trem? "
        perg5 = "5) Os horários bem como as integrações nos ramais facilitam o dia a dia dos usuários? "
        perg6 = "6) Você acredita que o serviço irá melhorar em um futuro próximo "

        perguntas = [perg1, perg2, perg3, perg4, perg5, perg6]

        X = "Questionario:"
        sep(X)
        espera(0.2)

        respostas_perguntas = []
        for i in perguntas:
            print(f"\n{NCiano}{i}{Corfim}")
            resposta = self.opcoes_de_respostas()
            respostas_perguntas.append(resposta)
            
        return respostas_perguntas

# CB1 [Complemento de B1]- Respostas padronizadas
    def opcoes_de_respostas(self):

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
            else: # Prevenção de Bug
                espera(0.2)
                print(f"{NVermelho} Digite apenas 1, 2 ou 3{Corfim}")

# CA1 [Complemento de A1]- Menssagens de Término e Inicio de entrevista
    def menssagem_de_fim_e_inicio(self):
        print (f"{NCiano}\nDados cadastrados com sucesso!\nAguarde um instante.")
        espera(3)
        limpar_tela()

        X = "Supervia - Avaliação de Clientes"
        sep(X)
        espera(0.2)
        print(f"{NBranco}Seguimos para o próximo cadastro.{Corfim}")
        print(f"{NBranco}Lembre-se, digite 00 para encerar a entrada de dados.{Corfim}")

# A2 - Exportação de aquivo CSV
    def salvar_respostas_csv(self):
        with open('pesquisa.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Idade', 'Gênero', 'Resposta_1', 'Resposta_2', 'Resposta_3', 'Resposta_4', 'Resposta_5', 'Resposta_6', "Data da resposta", " Hora da resposta"])
            writer.writerows(self.respostas)
        print("Respostas salvas no arquivo 'pesquisa.csv'")


# ######################################################################################################################################################
# ######################################################################################################################################################
# Execução da Classe:

pesquisa = Pesquisa()
pesquisa.coletar_respostas() #A1
pesquisa.salvar_respostas_csv() #A2

