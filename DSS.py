from time import sleep

class Class:
    def __init__(self, name='', phyAttack=1, magAttack=1, phyDef=1, magDef=1, criticalChance=1, 
        hp=1, mp=1, souls=0, level=0, weapom='', shield='', estus_flask=2, class_name=''):
        self.phyAttack = phyAttack
        self.magAttack = magAttack
        self.phyDef = phyDef
        self.magDef = magDef
        self.hp = hp
        self.mp = mp
        self.souls = souls
        self.level = level
        self.criticalChance = criticalChance
        self.estus_flask = estus_flask
        self.class_name = class_name

    def createCharacter(self):
        print('-' * 60)
        print('CRIAÇÃO DE PERSONAGEM'.center(60))
        print()
        self.name = str(input('Digite o nome do personagem: '))

    def choseClass(sef):
        print('')
        print('-=' * 30)
        print('SELEÇÃO DA CLASSE'.center(60))
        print("""
    1 - WARRIOR
    2 - KNIGHT
    3 - THIEF
    4 - BANDIT
    5 - HUNTER
    6 - SORCERER
    7 - PYROMANCER
    8 - DEPRIVED
    
    """)
        while True:
            select = int(input('Digite o número da classe escolhida: '))
            
            if select > 8 or select < 1:
                print('ERRO! Escolha uma opção válida:')

            else:
                break



        #Classe Warrior
        if select == 1:
            hero.class_name = 'Warrior'
            hero.phyAttack = 13
            hero.magAttack = 9
            hero.phyDef = 12
            hero.magDef = 8
            hero.criticalChance = 13
            hero.hp = 110
            hero.mp = 50
            hero.souls = 0

        #Classe Knight
        elif select == 2:
            hero.class_name = 'Knight'
            hero.phyAttack = 11
            hero.magAttack = 9
            hero.phyDef = 10
            hero.magDef = 10
            hero.criticalChance = 11
            hero.hp = 140
            hero.mp = 50
            hero.souls = 0

        #Classe Thief
        elif select == 3:
            hero.class_name = 'Thief'
            hero.phyAttack = 9
            hero.magAttack = 12
            hero.phyDef = 9
            hero.magDef = 11
            hero.criticalChance = 15
            hero.hp = 90
            hero.mp = 11
            hero.souls = 0

        #Classe Bandit
        elif select == 4:
            hero.class_name = 'Bandit'
            hero.phyAttack = 14
            hero.magAttack = 10
            hero.phyDef = 14
            hero.magDef = 8
            hero.hp = 120
            hero.mp = 50
            hero.souls = 0

        #Classe Hunter
        elif select == 5:
            hero.class_name = 'Hunter'
            hero.phyAttack = 12
            hero.magAttack = 9
            hero.phyDef = 11
            hero.magDef = 9
            hero.hp = 11
            hero.mp = 50
            hero.souls = 0

        #Classe Sorcerer
        elif select == 6:
            hero.class_name = 'Sorcerer'
            hero.phyAttack = 9
            hero.magAttack = 15
            hero.phyDef = 8
            hero.magDef = 15
            hero.hp = 80
            hero.mp = 100
            hero.souls = 0

        #Classe Pyromancer
        elif select == 7:
            hero.class_name = 'Pyromancer'
            hero.phyAttack = 12
            hero.magAttack = 12
            hero.phyDef = 11
            hero.magDef = 10
            hero.hp = 100
            hero.mp = 80
            hero.souls = 0

        #Classe Deprived
        elif select == 8:
            hero.class_name = 'Deprived'
            hero.phyAttack = 11
            hero.magAttack = 11
            hero.phyDef = 11
            hero.magDef = 11
            hero.hp = 110
            hero.mp = 50
            hero.souls = 0

        print('-' * 50)

        print('''
Atributos da Classe:
    
    Classe: {}
    Ataque Físico: {}
    Ataque Mágico: {}
    Defesa Física: {}
    Defesa Mágica: {}
    HP: {}
    MP: {}
    '''.format(hero.class_name, hero.phyAttack, hero.magAttack, hero.phyDef, hero.magDef, hero.hp, hero.mp))

        print('''
[ 1 ] CONFIRMAR A ESCOLHA
[ 2 ] VOLTAR
''')

        choose = int(input('Escolha uma opção: '))

        if choose == 1:
            pass
        elif choose == 2:
            hero.choseClass()

    def equipWeapom(self, other):
        self.phyAttack += other.phyAttack
        self.magAttack += other.magAttack
        self.weapom = other.name


class Equips:
    def __init__(self, name='', phyAttack=0, magAttack=0):
        self.name = name
        self.phyAttack = phyAttack
        self.magAttack = magAttack


class Monster:
    def __init__(self, name='', phyAttack=50, magAttack=65, phyDef=40, magDef=35, 
        hp=500, mp=100, souls=50):
        self.name = name
        self.phyAttack = phyAttack
        self.magAttack = magAttack
        self.phyDef = phyDef
        self.magDef = magDef
        self.hp = hp
        self.mp = mp
        self.souls = souls

    def attack(self, other):
        dano = self.phyAttack - other.phyDef
        other.hp -= dano
        if other.hp <= 0:
            print('{}:'.format(self.name))
            print('Você recebeu {} de dano!'.format(dano))

        else:
            print('{}:'.format(self.name))
            print('Você recebeu {} de dano!'.format(dano))
        dano = 0

    def magic(self, other):
        pass


class Hero(Class):
    def __init__(self, name='', phyAttack=1, magAttack=1, phyDef=1, magDef=1, criticalChance=1, 
        hp=1, mp=1, souls=0, level=0, weapom='', shield='', estus_flask=2, class_name=''):
        super(Hero, self).__init__(name, phyAttack, magAttack, phyDef, magDef, 
            criticalChance, hp, mp, souls, level, weapom, shield, estus_flask, class_name)
        
    def createCharacter(self):
        super(Hero, self).createCharacter()

    def choseClass(self):
        super(Hero, self).choseClass()

    def attack(self, other):
        dano = self.phyAttack - other.phyDef
        other.hp -= dano

        print('STATUS DA BATALHA:\n')
        if other.hp <= 0:
            print('{}:'.format(self.name))
            other.hp = 0
            hero.souls += other.souls
            print('Parabéns, você derrotou {}!'.format(other.name))
            print('Você adquiriu {} souls'.format(other.souls))

        else:
            print('{}:'.format(self.name))
            print('Você causou {} de dano no inimigo'.format(dano))
            print('HP {}: {}\n'.format(other.name, other.hp))

    def estusFlask(self):
        if self.estus_flask > 0:
            self.estus_flask -= 1
            self.hp += 100

            if self.hp > max_hp:
                self.hp = max_hp
            print('Você recuperou 100 pontos de vida!\n'.format(self.estus_flask))
        
        else:
            print('Você não possui Estus Flask!')

    def magic(self, other):
        pass


def battle_interface(enemy):
    global max_hp

    #Numero de rodadas por batalha
    turn = 0

    while True:
        turn += 1

        if turn == 1:
            max_hp = hero.hp

        print('-' * 50)
        choice = int(input("""
------------------------------------------
| Vida: {}   | Mana: {}  | Qtd Estus: {} |
------------------------------------------
  
[ 1 ] ATACAR
[ 2 ] ESTUS FLASK
[ 3 ] FUGIR

Escolha uma opção: """.format(hero.hp, hero.mp, hero.estus_flask)))
        print('-' * 50)

        if choice == 1:
            hero.attack(enemy)
            if enemy.hp <= 0:
                break

        elif choice == 2:
            hero.estusFlask()
            if hero.estus_flask == 0:
                continue

        elif choice == 3:
            print('Você fugiu!')
            break

        enemy.attack(hero)

        if hero.hp <= 0:
            print('Você foi derrotado!')
            break



#-------------------------------------------------------------------------------------------
#Objects: WEAPONS |
#_________________|

#Swords:
broken_straight_sword = Equips('Broken Straight Sword', 10)
straight_sword = Equips('Straight Sword', 20)
bastard_sword = Equips('Bastard Sword', 30)
straight_sword_hilt = Equips('Straight Sword Hilt', 40)

#Great Swords:

#-------------------------------------------------------------------------------------------
#Objects: BOSSES  |
#_________________|
#name, phyAttack=50, magAttack=65, phyDef=40, magDef=35, hp=500, mp=100, souls=50

asylum_demon = Monster('Asylum Demon', 25, 0, 15, 30, 300, 100, 500)


#-------------------------------------------------------------------------------------------
#Início do programa

#introdução
'''
print('-=' * 50)
print('Na Era dos Antigos,')
sleep(3)
print('O mundo era disforme, envolto por névoa.')
sleep(3)
print('Uma terra de penhascos cinzentos, arquiárvores e dragões eternos.')
sleep(3)
print('Mas então, fez-se o fogo.')
sleep(3)
print('Mas com o fogo, veio a disparidade.')
sleep(3)
print('Calor e frio,')
sleep(3)
print('vida e morte,')
sleep(3)
print('e é claro... Luz e Escuridão.')
sleep(3)
print('E então, da Escuridão eles vieram,')
sleep(3)
print('e encontraram as almas dos lordes na chama.')
sleep(3)
print('Nito, o Primeiro dos Mortos,')
sleep(3)
print('a Bruxa de Izalith com suas filhas do Caos,')
sleep(3)
print('Gwyn, o Lorde da Luz Solar, com seus leais cavaleiros,')
sleep(3)
print('e o furtivo pigmeu, tão facilmente esquecido.')
sleep(3)
print('Com a força dos lordes, eles desafiaram os dragões.')
sleep(3)
print('Os poderosos raios de Gwyn perfuraram suas escamas de pedras.')
sleep(3)
print('As bruxas conjuraram violentas tempestades de fogo')
sleep(3)
print('Nito lançou um miasma de morte e pestilência.')
sleep(3)
print('E Seath, o Descamado, traiu sua espécie.')
sleep(3)
print('Com isso, os dragões sucumbiram.')
sleep(3)
print('E assim teve início a Era do Fogo.')
sleep(3)
print('Sem demora, contudo, as chamas se apagarão e restará somente a Escuridão.')
sleep(3)
print('Mesmo agora, há apenas brasas,')
sleep(3)
print('e no lugar da luz, a humanidade vê apenas noites sem fim.')
sleep(3)
print('Além disso, entre os vivos se vê portadores da amaldiçoada Marca Negra.')
print('-=' * 50)

#Introdução 2
sleep(3)
print('Sim, de fato.')
sleep(3)
print('A Marca Negra assinala os Mortos-vivos.')
sleep(3)
print('E nesta terra,')
sleep(3)
print('os Mortos-vivos são agrupados e levados ao norte,')
sleep(3)
print('onde são então trancados e deixados à espera do fim do mundo.')
sleep(3)
print('...Esse é o seu destino.')
print()
sleep(3)
'''

print("""

      _____             _       _____             _     
     |  __ \           | |     / ____|           | |    
     | |  | | __ _ _ __| | __ | (___   ___  _   _| |___ 
     | |  | |/ _` | '__| |/ /  \___ \ / _ \| | | | / __|
     | |__| | (_| | |  |   <   ____) | (_) | |_| | \__ \

 
""")


hero = Hero()

#Escolher o nome do personagem
hero.createCharacter()

#Escolher a classe do personagem
hero.choseClass()

#Equipando a arma
hero.equipWeapom(straight_sword_hilt)


battle_interface(asylum_demon)


#print(hero.__dict__)







