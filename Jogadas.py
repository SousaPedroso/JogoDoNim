# -*- coding; utf-8 -*-

from random import randint

#Função para o computador jogar
def JogadaComputador(num_pecas_rests, num_pecas_rodada, nivel):
  peca_comp_nv3 = num_pecas_rodada
  #A partir do médio é possível o computador utilizar do que foi proposto para sempre ganhar
  def nivel_3(peca_comp_nv3):
    while ((num_pecas_rests - peca_comp_nv3) % (num_pecas_rodada + 1)) != 0:
      peca_comp_nv3 = peca_comp_nv3 - 1

    if peca_comp_nv3 == 0:
      peca_comp_nv3 = num_pecas_rodada

    if (num_pecas_rests <= num_pecas_rodada):
      peca_comp_nv3 = num_pecas_rodada

    return peca_comp_nv3

  #No nível 1 jogar apenas de maneira aleatória
  if nivel == 1:
    if num_pecas_rodada > num_pecas_rests:
      peca_comp = randint(1, num_pecas_rests)
    else:
      peca_comp = randint(1, num_pecas_rodada)
    return peca_comp
  
  #A partir do nível 2 há uma chance do computador utilizar da técnica para ganhar
  elif nivel == 2:
    if num_pecas_rodada > num_pecas_rests:
          peca_comp = randint(1, num_pecas_rests)
    else:
      peca_comp = randint(1, num_pecas_rodada)
    return peca_comp
  
  #O computador sempre utilizará da técnica para sempre ganhar
  elif nivel == 3:
    peca_comp = nivel_3(num_pecas_rodada)
    return peca_comp


#Usuário escolher quantas peças que retirar durante sua jogada
def JogadaUsuario(num_pecas_rests,num_pecas_rodada):
  erro = True
  while erro:
    try:
      pecas_usuario = int(input("Quantas peças você vai tirar?"))
    except ValueError:
      print("Você não digitou um número, tente novamente")
    else:
      if pecas_usuario > num_pecas_rodada:
        print("Número de peças excede o máximo por rodada")
        print("Tente retirar outro número de peças")

      elif pecas_usuario <= 0:
        print("Número de peças muito baixo")
        print("Tente retirar outro número de peças")

      elif num_pecas_rests - pecas_usuario < 0:
        print("Irá faltar peças")
        print("Tente retirar outro número de peças")

      else:
        erro = False

  return pecas_usuario