# -*- coding; utf-8 -*-

from Jogadas import JogadaComputador, JogadaUsuario
from Interface import mostraResultado, start, Placar, Apresentacao
from Utilidades import alternaJogadas, NumeroPecas

#Criação da função pro campeonato
def campeonato(num_partidas, num_pecas_restantes, num_pecas_rodada, nivel, num_partidas_passadas=1, VitComp=0, VitUsuario=0):

    if nivel != 3:
        Apresentacao(num_partidas_passadas)
        inicio = start()
        ganhador = alternaJogadas(inicio,num_pecas_restantes, num_pecas_rodada, nivel)
    
    else:
        Apresentacao(num_partidas_passadas)
        print("Computador começa!")
        ganhador = alternaJogadas(1,num_pecas_restantes, num_pecas_rodada, nivel)


    if num_partidas != 1:
        if ganhador == "Computador":
            Placar(num_partidas_passadas, VitComp+1, VitUsuario)
            num_pecas_restantes, num_pecas_rodada = NumeroPecas()
            campeonato(num_partidas-1,num_pecas_restantes,num_pecas_rodada,nivel,num_partidas_passadas+1,VitComp+1,VitUsuario)

        else:
            Placar(num_partidas_passadas, VitComp, VitUsuario+1)
            num_pecas_restantes, num_pecas_rodada = NumeroPecas()
            campeonato(num_partidas-1,num_pecas_restantes,num_pecas_rodada,nivel,num_partidas_passadas+1,VitComp,VitUsuario+1)
    else:
        if ganhador == "Computador":
            VitComp += 1
        else:
            VitUsuario += 1
        if VitComp > VitUsuario:
            print("Final do campeonato! Computador ganhou")
        else:
            print("Final do campeonato! Você ganhou")
        
        print("Placar final! Computador: %d x Você: %d"%(VitComp, VitUsuario))
        

#Uma única partida
def partidaUnica(num_pecas_restantes, num_pecas_rodada, nivel):

    if nivel != 3:
        inicio = start()
        alternaJogadas(inicio,num_pecas_restantes, num_pecas_rodada, nivel)

    else:
        print("Computador começa!")
        alternaJogadas(1,num_pecas_restantes, num_pecas_rodada, nivel)