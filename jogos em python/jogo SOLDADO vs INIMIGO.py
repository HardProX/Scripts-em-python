'''
Regras do jogo:
1-> no começo escolha qual personagem jogar, temos o SOLDADO e o INIMIGO.
2-> definar um nome para voçê e para seu adversário.
3-> o jogo começou! escolha entre as 3 opçõens disponiveis, a cada 5 escolhas uma nova opção aparecerá,
e voçê deve decidir se vai ou não usa-la.
4-> o combate fucionar da seguinte forma:
    a) para tira vida do seu oponete, o seu ataquer deve ser maior que a defesa dele, se esse for o caso
        o seu ataquer será subtraido com a defesa do advésario, e o que sobrá será tirado da vida do mesmo.
    b) se o ataquer for igual a defesa do advesário nenhum dano será causado para ambos os lados.
    c) se o ataquer for menor que a defesa do advesário, então sua vida será subtraida com a defesa do
        oponete.
5-> voçê pode escolher entre aumenta o ataquer, defesa e nivel(quando disponivel), mas lembre-sé a um limite
    de vezes para aumentar cada um deles:
    ataquer -> só poderá ser aumentado até 10.
    defesa -> só poderá ser aumentado até 10.
    nivel -> só poderá ser aumentado até 4.
    * caso tente aumentar mais que a capacidade, aparecerá um mensagem dizendo que não pode!
6 -> a função do nivel é multiplicar o ataquer e a defesa em determinada situação:
    1-> quando voçê for atacado a sua defesa será ajustada de acordo com seu nivel, sé seu nivel for
        2 sua defesa será multiplicada por 2, ser for 3 vai ser multiplicada por 3.
    2-> isso tambem vale quando for atacar o seu ataquer será multiplicado de acordo com seu nivel.
    3-> fique ciente que essas regras também valem para o adversário, então tenha cuidado.
7 -> no final será exibido um ESCORE.
'''

from random import randint

class npc:
    ata = 0  # 1 a 10
    defe = 0  # 1 a 10
    niv = 0  # 1 a 4
    life = 0  # 100

    def aumentar_ata(self,n):
        if self.ata < 10:
            self.ata += 1
            print(f'\033[1;33m{n} aumentou seu ataquer!\033[m')
        else:
            print('\033[1;36mo ataquer já está no MAXIMO\033[m')

    def aumentar_defe(self,n):
        if self.defe < 10:
            self.defe += 1
            print(f'\033[1;33m{n} aumentou sua defesa!\033[m')
        else:
            print('\033[1;36ma defesa já está no MAXIMO\033[m')

    def aumentar_niv(self,n):
        if self.niv < 4:
            self.niv += 1
            print(f'\033[1;33m{n} aumentou seu nivel\033[m')
        else:
            print('\033[1;36mNivel está no MAXIMO\033[m')

class soldado(npc):
    nome = ""

    def __init__(self, n):
        self.nome = n
        self.ata = 1
        self.defe = 1
        self.niv = 1
        self.life = 100

    def ataquer(self, inimigo,n,n2):
        ataO = self.ata
        defeO = inimigo.defe
        # configurando o ataque do soldado
        if self.niv == 1:
            self.ata *= 1
        elif self.niv == 2:
            self.ata *= 2
        elif self.niv == 3:
            self.ata *= 3
        elif self.niv == 4:
            self.ata *= 4

        # configurando a defesa do inimigo
        if inimigo.niv == 1:
            inimigo.defe *= 1
        elif inimigo.niv == 2:
            inimigo.defe *= 2
        elif inimigo.niv == 3:
            inimigo.defe *= 3
        elif inimigo.niv == 4:
            inimigo.defe *= 4

        if self.ata > inimigo.defe:
            self.ata -= inimigo.defe
            if self.ata > 0:
                inimigo.life -= self.ata
                print(f'\033[4;30m{n2} sofreu um dano de {self.ata} pontos\033[m')
                self.ata = ataO
                inimigo.defe = defeO
            elif self.ata == 0:
                print(f'\033[4;30m{n2} não sofrerá nenhum dano!\033[m')
                self.ata = ataO
                inimigo.defe = defeO
        elif self.ata == inimigo.defe:
            print('\033[4;30mataquer igual a defesa! nenhum dano para ambos os lados!\033[m')
            self.ata = ataO
            inimigo.defe = defeO
        elif self.ata < inimigo.defe:
            self.life -= inimigo.defe
            print(f'\033[4;30m{n} levou dano! menos {inimigo.ata} pontos de vida\033[m')
            self.ata = ataO
            inimigo.defe = defeO

    def status(self):
        print(f'Nome: {self.nome}')
        print(f'Vida: {self.life}')
        print(f'Nivel: {self.niv}')
        print(f'Ataquer: {self.ata}')
        print(f'Defesa: {self.defe}')
        print('-' * 20)

class inimigo(npc):
    nome = ""

    def __init__(self, n):
        self.nome = n
        self.ata = 1
        self.defe = 1
        self.niv = 1
        self.life = 100

    def ataquer(self, soldado,n,n2):
        ataO = self.ata
        defeO = soldado.defe
        # configurando o ataque do inimigo
        if self.niv == 1:
            self.ata *= 1
        elif self.niv == 2:
            self.ata *= 2
        elif self.niv == 3:
            self.ata *= 3
        elif self.niv == 4:
            self.ata *= 4

        # configurando a defesa do soldado
        if soldado.niv == 1:
            soldado.defe *= 1
        elif soldado.niv == 2:
            soldado.defe *= 2
        elif soldado.niv == 3:
            soldado.defe *= 3
        elif soldado.niv == 4:
            soldado.defe *= 4

        if self.ata > soldado.defe:
            self.ata -= soldado.defe
            if self.ata > 0:
                soldado.life -= self.ata
                print(f'\033[4;30m{n2} sofreu um dano de {self.ata} pontos\033[m')
                self.ata = ataO
                soldado.defe = defeO
            elif self.ata == 0:
                print(f'\033[4;30m{n2} não sofrerá nenhum dano!\033[m')
                self.ata = ataO
                soldado.defe = defeO
        elif self.ata == soldado.defe:
            print('\033[4;30mataquer igual a defesa! nenhum dano para ambos os lados!\033[m')
            self.ata = ataO
            soldado.defe = defeO
        elif self.ata < soldado.defe:
            self.life -= soldado.defe
            print(f'\033[4;30m{n} levou dano! menos {soldado.ata} pontos de vida\033[m')
            self.ata = ataO
            soldado.defe = defeO

    def status(self):
        print(f'Nome: {self.nome}')
        print(f'Vida: {self.life}')
        print(f'Nivel: {self.niv}')
        print(f'Ataquer: {self.ata}')
        print(f'Defesa: {self.defe}')
        print('-' * 20)

print('-=' * 40)
print('Qual personagem voçê quer jogar?')
print('[s] -> soldado')
print('[i] -> inimigo')
resp = str(input('qual é sua escolhar? ')).strip().lower()
while resp not in 'si':
    resp = str(input('\033[31mDigite novamente\033[m! qual é sua escolhar? ')).strip().lower()
if resp == 's':
    nome = str(input('Digite seu nome: ')).strip()
    nome2 = str(input('Digite o nome do seu adversario: ')).strip()
elif resp == 'i':
    nome2 = str(input('Digite seu nome: ')).strip()
    nome = str(input('Digite o nome do seu adversario: ')).strip()
print('-=' * 10)
print(f'{"MENU":^20}')
print('-' * 20)
def esco_soldado():
    s1 = soldado(nome)
    i1 = inimigo(nome2)
    cont = 0
    new = 0
    op = False
    sextaD = False
    batalhas = 0
    vitoria = "Não"
    while True:
        s1.status()
        i1.status()
        print('-' * 20)
        print('\033[34m[1] -> ataquer ao adversario')
        print('\033[34m[2] -> aumentar ataquer')
        print('\033[34m[3] -> aumentar defesa\033[m')
        if new == 5:
            print('\033[1;32m[4] -> aumentar nivel\033[m')
            new = 0
            sextaD = True
        respos = int(input('Sua escolha? '))
        while respos not in (1,2,3,4) :
            respos = int(input('\033[31mDigite novamente!\033[m sua escolha? '))
            if respos in (1,2,3,4):
                break
        if respos == 1:
            op = True
            print(f'\033[1;34m{nome} escolheu atacar!\033[m')
            s1.ataquer(i1,nome,nome2)
            batalhas += 1
        elif respos == 2:
            op = True
            s1.aumentar_ata(nome)
        elif respos == 3:
            op = True
            s1.aumentar_defe(nome)
        elif respos == 4 and sextaD == True:
            op = True
            s1.aumentar_niv(nome)
            sextaD = False
        elif respos == 4 and sextaD == False :
            print('\033[1mopção não está disponivel no momento!\033[m')
        if op == True:
            opçãoI = randint(0,4)
            if opçãoI == 0:
                print(f'\033[1;31m{nome2} resolveu atacar!\033[m')
                i1.ataquer(s1,nome2,nome)
                batalhas += 1
            elif opçãoI == 1:
                i1.aumentar_ata(nome2)
            elif opçãoI == 2:
                i1.aumentar_defe(nome2)
            elif opçãoI == 3:
                i1.aumentar_niv(nome2)
            else:
                print(f'\033[1;31m{nome2} não feiz nada!\033[m')
            op = False
        new += 1
        if i1.life <= 0:
            vitoria = "Sim"
            break
        elif s1.life <= 0:
            vitoria = "Não"
            break
    print('-=' * 20)
    print(f'\033[1;36;40m{"ESCORE":^40}\033[m')
    print('-' * 40)
    print(f'\033[1;34mPersonagem:\033[m{"SOLDADO"}')
    print(f'\033[32mnome:\033[m {s1.nome}')
    print(f'\033[32mVida:\033[m {s1.life}')
    print(f'\033[32mnivel:\033[m {s1.niv}')
    print(f'\033[32mataquer:\033[m {s1.ata}')
    print(f'\033[32mdefesa:\033[m {s1.defe}')
    print(f'\033[1;31mtotal de batalha travadas:\033[m {batalhas}')
    print(f'\033[1;30mVitoria:\033[m {vitoria}')
    print('-=' * 20)
def esco_inimigo():
    i1 = soldado(nome2)
    s1 = inimigo(nome)
    cont = 0
    new = 0
    op = False
    sextaD = False
    batalhas = 0
    vitoria = "Não"
    while True:
        i1.status()
        s1.status()
        print('-' * 20)
        print('\033[34m[1] -> ataquer ao adversario')
        print('\033[34m[2] -> aumentar ataquer')
        print('\033[34m[3] -> aumentar defesa\033[m')
        if new == 5:
            print('\033[1;32m[4] -> aumentar nivel\033[m')
            new = 0
            sextaD = True
        respos = int(input('Sua escolha? '))
        while respos not in (1,2,3,4) :
            respos = int(input('\033[31mDigite novamente!\033[m sua escolha? '))
            if respos in (1,2,3,4):
                break
        if respos == 1:
            op = True
            print(f'\033[1;34m{nome2} escolheu atacar!\033[m')
            i1.ataquer(s1,nome2,nome)
            batalhas += 1
        elif respos == 2:
            op = True
            i1.aumentar_ata(nome2)
        elif respos == 3:
            op = True
            i1.aumentar_defe(nome2)
        elif respos == 4 and sextaD == True:
            op = True
            i1.aumentar_niv(nome2)
            sextaD = False
        elif respos == 4 and sextaD == False :
            print('\033[1mopção não está disponivel no momento!\033[m')
        if op == True:
            opçãoI = randint(0,4)
            if opçãoI == 0:
                print(f'\033[1;31m{nome} resolveu atacar!\033[m')
                s1.ataquer(i1,nome,nome2)
                batalhas += 1
            elif opçãoI == 1:
                s1.aumentar_ata(nome)
            elif opçãoI == 2:
                s1.aumentar_defe(nome)
            elif opçãoI == 3:
                s1.aumentar_niv(nome)
            else:
                print(f'\033[1;31m{nome} não feiz nada!\033[m')
            op = False
        new += 1
        if s1.life <= 0:
            vitoria = "Sim"
            break
        elif i1.life <= 0:
            vitoria = "Não"
            break
    print('-=' * 20)
    print(f'\033[1;36;40m{"ESCORE":^40}\033[m')
    print('-' * 40)
    print(f'\033[1;34mPersonagem:\033[m{"INIMIGO"}')
    print(f'\033[32mnome:\033[m {i1.nome}')
    print(f'\033[32mVida:\033[m {i1.life}')
    print(f'\033[32mnivel:\033[m {i1.niv}')
    print(f'\033[32mataquer:\033[m {i1.ata}')
    print(f'\033[32mdefesa:\033[m {i1.defe}')
    print(f'\033[1;31mtotal de batalha travadas:\033[m {batalhas}')
    print(f'\033[1;30mVitoria:\033[m {vitoria}')
    print('-=' * 20)

if resp == 's':
    esco_soldado()
elif resp == 'i':
    esco_inimigo()
