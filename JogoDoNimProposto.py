# -*- coding: utf-8 -*-

import sys
from Utilidades import BoasVindas, NumeroPecas, NumPartidas
from ModoDeJogo import partidaUnica, campeonato

def jogo():
    
	nivel = BoasVindas()
	print("Escolha um modo de jogo")
	erro = True
	while erro:
		try:
			modo_de_jogo = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))
   
		except ValueError:
			print("Não foi identificado um número, escolha 1 dos 2 modos de jogo")

		else:
			if modo_de_jogo < 1 or modo_de_jogo > 2:
				print("Número invalido, escolha de 1 a 2 para o modo de jogo")
			else:
				erro = False

	if modo_de_jogo == 1:
		print("Você escolheu uma partida isolada!")
		num_total_pecas, num_pecas_rodada = NumeroPecas()
		partidaUnica(num_total_pecas, num_pecas_rodada, nivel)

	elif modo_de_jogo == 2:
		print("Você escolheu um campeonato!")
		num_partidas = NumPartidas()
		num_total_pecas, num_pecas_rodada = NumeroPecas()
		campeonato(num_partidas,num_total_pecas, num_pecas_rodada, nivel)


jogo()