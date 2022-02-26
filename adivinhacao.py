import random

def jogar_adivinhacao():
    print('*******************************')
    print('******Jogo de advinhação!******')
    print('*******************************')

    numero_secreto = random.randint(1,100)
    tentativas = 0
    pontos = 1000
    pontos_perdidos = 0

    print('Escolha o nível de dificuldade do jogo.')
    print('1 - Fácil | 2 - Médio | 3 - Difícil')
    nivel = int(input('Digite o nível de dificuldade escolhido: '))

    if (nivel == 1):
        tentativas = 10
    elif (nivel == 2):
        tentativas = 5
    else:
        tentativas = 3


    for rodada in range(1, tentativas + 1):
        print('---------------------------------------------------------------------------------------------------------')
        print(f'Tentativa {rodada} de {tentativas}')
        print('---------------------------------------------------------------------------------------------------------')
        chute = int(input('Digite um número entre 1 e 100: '))
        
        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100:')
            continue
        if numero_secreto == chute:
            print('Parabéns! Você acertou!') 
            print(f'Seu chute foi: {chute} e o número secreto é: {numero_secreto}')
            print('Você fez {} pontos'. format(pontos))
            print('---------------------------------------------------------------------------------------------------------')
            break
        elif chute > numero_secreto:
            print('O número secreto é menor que o seu chute!')

        elif chute < numero_secreto:
            print('O número secreto é maior que seu chute!')
        else:
            print('Suas chances acabaram! O número secreto é: ', numero_secreto)
            print('--------------------------------------------------------------------------------------------------------')
        pontos_perdidos = abs(numero_secreto -  chute)
        pontos = pontos - pontos_perdidos
    print('O número secreto é: ', numero_secreto)
    print('Fim do jogo!')
    print('---------------------------------------------------------------------------------------------------------')
