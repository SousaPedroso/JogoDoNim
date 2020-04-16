# -*- coding: utf-8 -*-

from random import randint

#mostrar as jogadas feitos pelo computador e pelo usuário
def mostraResultado(num_pecas_restantes, num_pecas_retiradas, jogador):
    if (num_pecas_restantes != 0):
        print("%s retirou %d peças."%(jogador, num_pecas_retiradas))
        print("Agora restam %d peças."%(num_pecas_restantes))

    else:
        if num_pecas_retiradas > 1:
            print("%s retirou as últimas %d peças e ganhou a rodada."%(jogador, num_pecas_retiradas))
        else:
            print("%s retirou a última %d peça e ganhou a rodada."%(jogador, num_pecas_retiradas))


#Quando não estiver na dificuldade impossível, determinar quem irá começar a jogar
def start():
    comeco = randint(0,1)
    if comeco == 0:
        print("Você começa!")
    
    else:
        print("Computador começa!")
    
    return comeco

#Mostrar o placar após cada partida jogada no campeonato
def Placar(rodadasJogadas,VitComp=0, VitUsuario=0):
    print("Rodada %d: Computador: %d x Você: %d" %(rodadasJogadas, VitComp, VitUsuario))


#Anunciar o número da partida no campeonato
def Apresentacao(rodadasJogadas):
    print("Partida %d"%rodadasJogadas)