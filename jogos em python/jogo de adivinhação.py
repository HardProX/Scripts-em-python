#  the code is an arte
from random import randint
print('\033[7m-=' * 40,'\033[m')
nome = str(input('Digite seu Nome: ')).strip().lower()
print(f'Sejá Bem vindo {nome}.')
print('-' * 20)
print('\033[1;36mEscolha um nivel:\033[m')
print("""\033[32m[1] -> Facil\033[m
\033[32m[2] -> Médio\033[m
\033[32m[3] -> Dificil\033[m
\033[32m[4] -> Very Hard\033[m
\033[32m[5] -> Imporsivel\033[m
\033[32m[6] -> Imporsivel 2.0\033[m""")
print('-' * 20)
opcão = int(input('Sua Escolha: '))
if opcão not in (1,2,3,4,5,6) :
    while True :
        opcão = int(input('\033[1;31mDIGITE NOVAMENTE\033[m,Sua Escolha: '))
        if opcão in (1,2,3,4,5,6) :
            break
if opcão == 1:
    escolha_computador = randint(1,10)
    cont = 0
    print('-' * 20)
    print('Voçê escolheu o nivel Facil, preparado?')
    print('\033[34mO computador Pensou em um numero de 1 a 10...\033[m')
    while True:
        escolha_jogador = int(input('Qual é o numero que o computador pensou? '))
        if escolha_jogador == escolha_computador:
            print(f'\033[1;30mParabens! o numero {escolha_jogador} é o correto\033[m')
            break
        else:
            if escolha_jogador > escolha_computador :
                print('-' * 20)
                print('\033[4;36mUm pouco menos...\033[m')
                print('\033[31mTente novamente\033[m')
            elif escolha_jogador < escolha_computador:
                print('-' * 20)
                print('\033[4;36mUm pouco mais...\033[m')
                print('\033[31mTente novamente\033[m')
        cont += 1
if opcão == 2:
    escolha_computador = randint(1,20)
    cont = 0
    print('-' * 20)
    print('Voçê escolheu o nivel Médio, preparado?')
    print('\033[34mO computador Pensou em um numero de 1 a 20...\033[m')
    while True:
        escolha_jogador = int(input('Qual é o numero que o computador pensou? '))
        if escolha_jogador == escolha_computador:
            print(f'\033[1;30mParabens! o numero {escolha_jogador} é o correto\033[m')
            break
        else:
            if escolha_jogador > escolha_computador :
                print('-' * 20)
                print('\033[4;36mUm pouco menos...\033[m')
                print('\033[31mTente novamente\033[m')
            elif escolha_jogador < escolha_computador:
                print('-' * 20)
                print('\033[4;36mUm pouco mais...\033[m')
                print('\033[31mTente novamente\033[m')
        cont += 1
if opcão == 3:
    escolha_computador = randint(1,30)
    cont = 0
    print('-' * 20)
    print('Voçê escolheu o nivel Dificil, preparado?')
    print('\033[34mO computador Pensou em um numero de 1 a 30...\033[m')
    while True:
        escolha_jogador = int(input('Qual é o numero que o computador pensou? '))
        if escolha_jogador == escolha_computador:
            print(f'\033[1;30mParabens! o numero {escolha_jogador} é o correto\033[m')
            break
        else:
            if escolha_jogador > escolha_computador :
                print('-' * 20)
                print('\033[4;36mUm pouco menos...\033[m')
                print('\033[31mTente novamente\033[m')
            elif escolha_jogador < escolha_computador:
                print('-' * 20)
                print('\033[4;36mUm pouco mais...\033[m')
                print('\033[31mTente novamente\033[m')
        cont += 1
if opcão == 4:
    escolha_computador = randint(1,100)
    cont = 0
    print('-' * 20)
    print('Voçê escolheu o nivel Very Hard, preparado?')
    print('\033[34mO computador Pensou em um numero de 1 a 100...\033[m')
    while True:
        escolha_jogador = int(input('Qual é o numero que o computador pensou? '))
        if escolha_jogador == escolha_computador:
            print(f'\033[1;30mParabens! o numero {escolha_jogador} é o correto\033[m')
            break
        else:
            if escolha_jogador > escolha_computador :
                print('-' * 20)
                print('\033[4;36mUm pouco menos...\033[m')
                print('\033[31mTente novamente\033[m')
            elif escolha_jogador < escolha_computador:
                print('-' * 20)
                print('\033[4;36mUm pouco mais...\033[m')
                print('\033[31mTente novamente\033[m')
        cont += 1
if opcão == 5:
    escolha_computador = randint(1,1000)
    cont = 0
    print('-' * 20)
    print('Voçê escolheu o nivel Imposivel, Voçê tem muita coragem não é?')
    print('\033[34mO computador Pensou em um numero de 1 a 1000...\033[m')
    while True:
        escolha_jogador = int(input('Qual é o numero que o computador pensou? '))
        if escolha_jogador == escolha_computador:
            print(f'\033[1;30mParabens! o numero {escolha_jogador} é o correto\033[m')
            break
        else:
            if escolha_jogador > escolha_computador :
                print('-' * 20)
                print('\033[4;36mUm pouco menos...\033[m')
                print('\033[31mTente novamente\033[m')
            elif escolha_jogador < escolha_computador:
                print('-' * 20)
                print('\033[4;36mUm pouco mais...\033[m')
                print('\033[31mTente novamente\033[m')
        cont += 1
if opcão == 6:
    escolha_computador = randint(1,10000)
    cont = 0
    print('-' * 20)
    print('Voçê escolheu o nivel Imposivel 2.0, Voçê tem muita coragem não é?')
    print('\033[34mO computador Pensou em um numero de 1 a 10000...\033[m')
    while True:
        escolha_jogador = int(input('Qual é o numero que o computador pensou? '))
        if escolha_jogador == escolha_computador:
            print(f'\033[1;30mParabens! o numero {escolha_jogador} é o correto\033[m')
            break
        else:
            if escolha_jogador > escolha_computador :
                print('-' * 20)
                print('\033[4;36mUm pouco menos...\033[m')
                print('\033[31mTente novamente\033[m')
            elif escolha_jogador < escolha_computador:
                print('-' * 20)
                print('\033[4;36mUm pouco mais...\033[m')
                print('\033[31mTente novamente\033[m')
        cont += 1
print('\033[35m=' * 30,'\033[m')
print(f'{"ESCORE":^30}')
print('-' * 30)
print(f'\033[1;33mNome: {nome}')
print(f'\033[37mNivel: {opcão}')
print(f'\033[1;36mtotal de Erros: {cont}')
print('\033[1;30mMuito obrigado por Jogar!')
print('\033[35m=' * 30, '\033[m')
print('\033[7m-=' * 40,'\033[m')
