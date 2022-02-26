print('*************************************')
print('*********Bem-vindo aos jogo!*********')
print('*************************************')

print('Você pode escolher entre dois divertidos jogos:')
print('1 - Adivinhação  | 2 - Forca')
jogo = int(input('Digite o número do jogo desejado:'))

if (jogo == 1):
    print('Você escolheu o Jogo da Adivinhação!')
    import adivinhacao
else:
    print('Você escolheu o Jogo da Forca!')
    import forca