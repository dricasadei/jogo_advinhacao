import random

def jogar_forca():
    print('********************************')
    print('*********Jogo de forca!*********')
    print('********************************')
    
    palavras = []
    
    # com o with não preciso fechar o arquivo (.close()), pois 
    # mesmo se houver erro o python já fecha o arquivo após execução
    with open('palavras.txt') as arquivo: 
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
      
    
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    enforcou = False
    acertou = False
    erros = 0
    
    # conforme o número de letras da palavra, cria o layout: "_", "_"....
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    print(letras_acertadas)
    
    while (not enforcou and not acertou):
        chute = input('Digite uma letra: ')
        chute = chute.strip().upper() # strip --> retira os espaços em branco no inicio e fim da palavra
        
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print('Errou!')
        enforcou = erros == 6 # quando atingir 6 o enforcou virá True e o while para. 
        acertou = '_'not in letras_acertadas # o usuário acertou todas as letras das palavras.   
        print(letras_acertadas)
    
    if (acertou):
        print('Você ganhou!')
    else:
        print('Você perdeu!')
    
    print('Fim do jogo!')



if(__name__ == '__main__'):
    jogar_forca()