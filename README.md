## Proposta do jogo

- O jogo do Nim consiste nos jogadores retirarem peças até acabar o número de peças.
- O último jogador a retirar peças ganha a partida.

- Seja *__m__* o número máximo de peças por rodada, a estratégia vencedora consite em deixar sempre múltiplos de __(m+1)__ peças restantes para o adversário. Essa estratégia do jogo utilizada no projeto foi imposta originalmente pelo [exercício](https://www.coursera.org/learn/ciencia-computacao-python-conceitos/programming/yEPxE/programa-completo-jogo-do-nim), sendo que caso o número __inicial__ de peças fosse um __múltiplo__ de __(m+1)__ o computador deve deixar o usuário começar a jogar. Assim, torna-se impossível ganhar do computador.

- A ideia foi implementar um jogo amigável em diferentes dificuldades, de modo que seja possível que o usuário também ganhe.

## Execução do jogo

- Para jogar, *clone* esse repositório e execute no terminal:
```
python JogoDoNimOriginal.py
```
Se quiser jogar a proposta inicial, ou:
```
python JogoDoNimProposto.py
```
Se quiser jogar a modificação proposta.

## Diferenças para a prosposta inicial

- Para implementar o jogo amigável, foram escolhidos 3 níveis de dificuldades para o usuário escolher jogar:

  - Dificuldade Fácil, o computador apenas escolherá de forma aleatória o número de peças, podendo ou não atingir atingir a estratégia vencedora.

  - Dificuldade Médio, o computador aleatoriamente poderá escolher um número aleatório de peças ou então escolher a estratégia vencedora para retirar o número de peças.

  - Dificuldade Impossível, o computador usará todas as estratégias para sempre vencer no jogo, a mesma utilizada no [jogo original](https://github.com/SousaPedroso/JogoDoNim/blob/master/JogoDoNimOriginal.py).
  
- A seleção de níveis pode ser conferida [aqui](/imagens/Dificuldades.PNG).

- Outra mudança ocorreu no campeonato, foi deixado ele mais customizável, com escolha para jogar 3, 5, 7 ou 9 partidas.
- A seleção de quantas partidas vão ser jogadas no campeonato pode ser verificada [aqui](/imagens/Campeonato.PNG).
- Por último, foram feitos tratamentos de erro para que o usuário não tenha que reiniciar suas partidas por ter digitado algo errado :smile:.

## Contribuição

Encontrou algum problema no jogo ou gostaria de melhorá-lo? Siga os seguintes passos.
1. Faça um Fork do projeto
2. Cria uma nova Branch para suas modificações
3. Comite suas modificações
4. Faça o Push da Branch
5. Abra um Pull Request

## Licença

- Distribuído sobre a licença MIT. Veja `LICENSE` para mais informações.
