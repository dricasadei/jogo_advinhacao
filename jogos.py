import adivinhacao
import forca

print('*************************************')
print('*********Bem-vindo aos jogo!*********')
print('*************************************')

print('Você pode escolher entre dois divertidos jogos:')
print('1 - Adivinhação  | 2 - Forca')
jogo = int(input('Digite o número do jogo desejado:'))

if (jogo == 1):
    print('Você escolheu o Jogo da Adivinhação!')
    adivinhacao.jogar_adivinhacao() # chamando a função do jogo e o import para executar
else:
    print('Você escolheu o Jogo da Forca!')
    forca.jogar_forca() # chamando a função do jogo e o import para executar
    
    