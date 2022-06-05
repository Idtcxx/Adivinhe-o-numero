print('\n\t                 Adivinhe o numero\n\t')

def adv():

    import random
    import math

    menor = int(input('Digite o numero menor:\n\t---'))
    maior = int(input('Digite o numero maior:\n\t---'))
    x = random.randint(menor, maior)

    print('\n\tVoce tem ', round(math.log(maior - menor + 1, 2)), 'chances para ganhar\n\t')
    print('Digite um numero de', menor, 'a', maior, ':')

    count = 0
    while count < round(math.log(maior - menor + 1, 2)):
        numero = int(input('---'))


        count += 1

        if numero == x:
            print('Parabéns você ganhou com', count, 'tentativas!!!')
            break

        elif numero < x:
            print('O numero digitado estar a baixo do numero sorteado\n\t.................')
        elif numero > x:
            print('O número digitado estar a cima do numero sorteado\n\t.................')

    if count  > round(math.log(maior - menor + 1, 2)):
        print('Você perdeu,o numero sorteado é',x)

    print('Deseja continuar? sim ou nao')
    qst = input('-')
    print('\t.................')

    if qst == 'sim':
        adv()
    else:
        print('Adeus!!')
adv()
