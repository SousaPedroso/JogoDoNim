# -*- coding; utf-8 -*-

from Jogadas import JogadaComputador, JogadaUsuario
from Interface import mostraResultado

#Função para alternar entre os jogadores
def alternaJogadas(comeco, num_pecas_restantes, num_pecas_rodada, nivel, ultimaJogada=""):

    #Critério de parada para a recursão, retornar o vencedor
    if num_pecas_restantes == 0:
        return ultimaJogada
    else:
        if comeco == 0:
            pecas_usuario = JogadaUsuario(num_pecas_restantes, num_pecas_rodada)
            num_pecas_restantes -= pecas_usuario
            mostraResultado(num_pecas_restantes, pecas_usuario, "Você")
            return alternaJogadas(1, num_pecas_restantes, num_pecas_rodada, nivel, "Você")

        else:
            pecas_computador = JogadaComputador(num_pecas_restantes, num_pecas_rodada, nivel)
            num_pecas_restantes -= pecas_computador
            mostraResultado(num_pecas_restantes, pecas_computador, "Computador")
            return alternaJogadas(0, num_pecas_restantes, num_pecas_rodada, nivel, "Computador")


#Boas vindas para o jogo e seleção da dificuldade do jogo
def BoasVindas():
    print("Bem vindo ao jogo do NIM!")
    erro = True
    #Evitar possíveis erros ao digitar ou bugs
    while erro:
    	print("Deseja jogar em qual nível?")
    	try:
      		niv = int(input("1-Fácil\n2-Médio\n3-Impossível\n"))

    	except ValueError:
      		print("Não foi identificado um número, escolha 1 dos 3 níveis")

    	else:
            if niv < 1 or niv > 3:
                print("Número invalido, escolha de 1 a 3 o nível para jogar")
            else:
                erro = False
    
    return niv


#Definição do número de peças para cada rodada
def NumeroPecas():
    
    erro = True
    #Possibilitar apenas números possíveis de peças para jogar
    while erro:
        try:
            num_pecas_totais = int(input("Qual o número total de peças?\n"))
        
        except ValueError:
            print("Número não detectado! Tente novamente.")

        else:
            if num_pecas_totais < 1:
                print("Valor incorreto para jogar! Tente novamente.")
            else:
                erro = False
    
    #Definir valores possíveis para o número de peças por rodada
    erro = True
    while erro:
        try:
            num_pecas_rodada = int(input("Número de peças por rodada: "))

        except ValueError:
            print("Número não detectador! Tente novamente.")
        
        else:
            if num_pecas_rodada < 1:
                print("Valor incorreto para jogar! Tente novamente.")
            elif num_pecas_rodada > num_pecas_totais:
                print("Números de peças por rodada maior que o número total de peças.")
            else:
                erro = False

    return num_pecas_totais, num_pecas_rodada


#Definição do número de partidas para o campeonato
def NumPartidas():
    erro = True
    #Evitar valores indisponíveis
    while erro:
        print("Escolha quantas partidas jogar")
        try:
            quant_partidas = int(input("3\n5\n7\n9\n"))
        except ValueError:
            print("Não foi detectado um número, tente novamente")

        else:
            if (quant_partidas != 3 and quant_partidas != 5 and quant_partidas != 7 and quant_partidas != 9):
                print("Número indisponível, tente outro.")
            else:
                erro = False
        
    return quant_partidas