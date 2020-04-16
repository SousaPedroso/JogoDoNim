import sys

def usuario_escolhe_jogada(n, m):
	p = int(input("Quantas peças você vai tirar?"))
	while p > m or p <=0 or n - p < 0:
		print("Oops! Jogada inválida! Tente de novo.")
		p = int(input("Quantas peças você vai tirar?"))
	return(p)

	
def computador_escolhe_jogada(n, m):
	z = m
	if ((n - z) % (m + 1)) != 0:
		while ((n - z) % (m + 1)) != 0:
			z = z - 1
		if z == 0:
			z = m
	else:
		if (n <= z):
			z = n
	return(z)
	


def  partida():
	jogo()
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	while ((n and m) < 1):
		print("Oops! Valor inválido!")
		n = int(input("Quantas peças? "))
		m = int(input("Limite de peças por jogada? "))
	if (n % (m + 1)) == 0:
		print("Você começa")
		while n > 0:
			p = usuario_escolhe_jogada(n, m)
			n = n - p
			print("Você tirou", p, "peças")
			print("Agora restam", n, "peças")
			s = computador_escolhe_jogada(n, m)
			n = n - s
			print("O computador tirou", s, "peças")
			print("Agora restam", n, "peças")
			if (n == 0):
				print("Fim do jogo! O computador ganhou!")
	if (n % (m + 1)) != 0:
		print("Computador começa")
		while n > 0 :
			s = computador_escolhe_jogada(n, m)
			n = n - s
			print("O computador tirou", s, "peças")
			print("Agora restam", n, "peças")
			if (n == 0):
				print("Fim do jogo! O computador ganhou!")
				sys.exit(0)
			p = usuario_escolhe_jogada(n, m)
			n = n - p
			print("Você tirou", p, "peças")
			print("Agora restam", n, "peças")
			

def partida1():			
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	while ((n and m) < 1):
		print("Oops! Valor inválido!")
		n = int(input("Quantas peças? "))
		m = int(input("Limite de peças por jogada? "))
	if (n % (m + 1)) == 0:
		print("Você começa")
		while n > 0:
			p = usuario_escolhe_jogada(n, m)
			n = n - p
			print("Você tirou", p, "peças")
			print("Agora restam", n, "peças")
			s = computador_escolhe_jogada(n, m)
			n = n - s
			print("O computador tirou", s, "peças")
			print("Agora restam", n, "peças")
			if (n == 0):
				print("Fim do jogo! O computador ganhou!")
				partida2()
	if (n % (m + 1)) != 0:
		print("Computador começa")
		while n > 0 :
			s = computador_escolhe_jogada(n, m)
			n = n - s
			print("O computador tirou", s, "peças")
			print("Agora restam", n, "peças")
			if (n == 0):
				print("Fim do jogo! O computador ganhou!")
				partida2()
			p = usuario_escolhe_jogada(n, m)
			n = n - p
			print("Você tirou", p, "peças")
			print("Agora restam", n, "peças")

def campeonato():
		partida1()



def jogo():
	print("Bem vindo ao jogo do NIM! Escolha: ")
	print("1 - para jogar uma partida isolada")
	l = int(input("2 - para jogar um campeonato"))
	if l == 1:
		print("Você escolheu uma partida isolada!")
	if l == 2:
		print("Você escolheu um campeonato!")
		print("**** Rodada 1 ****")
		campeonato()
		
		
		
def partida2():
	print("**** Rodada 2 ****")
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	while ((n and m) < 1):
		print("Oops! Valor inválido!")
		n = int(input("Quantas peças? "))
		m = int(input("Limite de peças por jogada? "))
	if (n % (m + 1)) == 0:
		print("Você começa")
		while n > 0:
			p = usuario_escolhe_jogada(n, m)
			n = n - p
			print("Você tirou", p, "peças")
			print("Agora restam", n, "peças")
			s = computador_escolhe_jogada(n, m)
			n = n - s
			print("O computador tirou", s, "peças")
			print("Agora restam", n, "peças")
			if (n == 0):
				print("Fim do jogo! O computador ganhou!")
				partida3()
	if (n % (m + 1)) != 0:
		print("Computador começa")
		while n > 0 :
			s = computador_escolhe_jogada(n, m)
			n = n - s
			print("O computador tirou", s, "peças")
			print("Agora restam", n, "peças")
			if (n == 0):
				print("Fim do jogo! O computador ganhou!")
				partida3()
			p = usuario_escolhe_jogada(n, m)
			n = n - p
			print("Você tirou", p, "peças")
			print("Agora restam", n, "peças")

def partida3():
	print("**** Rodada 3 ****")
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	while ((n and m) < 1):
		print("Oops! Valor inválido!")
		n = int(input("Quantas peças? "))
		m = int(input("Limite de peças por jogada? "))
	if (n % (m + 1)) == 0:
		print("Você começa")
		while n > 0:
			p = usuario_escolhe_jogada(n, m)
			n = n - p
			print("Você tirou", p, "peças")
			print("Agora restam", n, "peças")
			s = computador_escolhe_jogada(n, m)
			n = n - s
			print("O computador tirou", s, "peças")
			print("Agora restam", n, "peças")
			if (n == 0):
				print("Fim do jogo! O computador ganhou!")
				print("**** Final do campeonato! ****")
				print("Placar: Você: 0 X 3 Computador")
				sys.exit(0)
	if (n % (m + 1)) != 0:
		print("Computador começa")
		while n > 0 :
			s = computador_escolhe_jogada(n, m)
			n = n - s
			print("O computador tirou", s, "peças")
			print("Agora restam", n, "peças")
			if (n == 0):
				print("Fim do jogo! O computador ganhou!")
				print("**** Final do campeonato! ****")
				print("Placar: Você: 0 X 3 Computador")
				sys.exit(0)
			p = usuario_escolhe_jogada(n, m)
			n = n - p
			print("Você tirou", p, "peças")
			print("Agora restam", n, "peças")

partida()