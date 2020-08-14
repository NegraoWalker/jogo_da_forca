# Exemplo de um jogo da forca simples em python:
import random # Importando a biblioteca random para poder usar a função de escolha aleatória
palavra = ['perfume','sabonete','cadeira','sorvete','camiseta','bermuda','cotonete','geografia','sociologia','filosofia'
                  'biologia','laranja','amarelo','vermelho','caneta']

palavraSecreta = random.choice(palavra) # Recebendo uma palavra aleatória para poder jogar

letrasDigitadas = [] # Lista criada para armazenar as letras digitadas pelo usuário

chancesAcerto = 3 # Váriavel criada para definir quantas chances o usuário tem para acertar a palavra secreta

while True:

    if chancesAcerto <= 0:
        print('Perdeu !!! você não conseguiu completar a palavra secreta !!!!')
        break # Parada do jogo

    letra = input('Digite uma letra: ') # Recebendo a letra do usuário

    if len(letra) > 1: # Testando se o usuário digitou apenas uma letra
        print('Ahhhh isso não vale, digite apenas uma letra !!!')
        continue # Usando o comando continue pra dar prosseguimento ao programa
    letrasDigitadas.append(letra) # Armazenando a letra na lista atráves da função append

    if letra in palavraSecreta: # Testando se a letra digitada pelo usuário está dentro da palavra secreta
        print(f'Boa !!! a letra {letra} existe na palavra secreta')
        print()
    else:
        print(f'Tente outra vez !!! a letra {letra} não existe na palavra secreta')
        print()
        letrasDigitadas.pop() # Removendo a última letra digitada da lista

    temporaria = '' # Criação de uma variável para armazenar as letras temporariamente
    for letraSecreta in palavraSecreta: # Criando um laço para exibição dos acertos da palavraSecreta sem mostrar a resposta
        if letraSecreta in letrasDigitadas: # Testando se a letra digitada está na lista de acertos
            temporaria += letraSecreta # Armazenando os acertos de letras na variavel temporaria para sua exibição
        else:
            temporaria += '_' # Ocultando o resto das letras da palavraSecreta para a exibição na tela

    if temporaria == palavraSecreta: # Testando se as letras digitadas formam a palavraSecreta
        print()
        print(f'PARABÉNS VC É O GANHADOR !!!!! A palavra secreta era {temporaria}.')

        break # Parada do jogo
    else:
        print(temporaria) # Exibindo a variável temporária para o usuário ver como está as letras se encaixando na palavraSecreta
        print()
    if letra not in palavraSecreta: # Testando se a letra digitada não está na palavraSecreta para descrementar as chances do usuário
        chancesAcerto -= 1 # Decrementando
    print(f'Você ainda tem {chancesAcerto} chances para acertar a palavra secreta') # Exibindo as chances
    print()