from time import sleep
import random
import math

class Class:
    def __init__(self, name='', phyAttack=0,max_phy_attack=0, magAttack=0, max_mag_attack=0, 
        phyDef=0, magDef=0, criticalChance=0, hp=0, mp=0, souls=0, level=0, weapom='', 
        shield='', estus_flask=2, class_name=''):
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
        self.max_phy_attack = max_phy_attack
        self.max_mag_attack = max_mag_attack

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
            hero.max_phy_attack = 23
            hero.magAttack = 7
            hero.max_mag_attack = 17
            hero.phyDef = 12
            hero.magDef = 8
            hero.criticalChance = 5
            hero.hp = 110
            hero.mp = 50
            hero.souls = 0

        #Classe Knight
        elif select == 2:
            hero.class_name = 'Knight'
            hero.phyAttack = 11
            hero.max_phy_attack = 21
            hero.magAttack = 8
            hero.max_mag_attack = 18
            hero.phyDef = 10
            hero.magDef = 10
            hero.criticalChance = 5
            hero.hp = 140
            hero.mp = 50
            hero.souls = 0

        #Classe Thief
        elif select == 3:
            hero.class_name = 'Thief'
            hero.phyAttack = 9
            hero.max_phy_attack = 19
            hero.magAttack = 8
            hero.max_mag_attack = 18
            hero.phyDef = 9
            hero.magDef = 11
            hero.criticalChance = 10
            hero.hp = 90
            hero.mp = 11
            hero.souls = 0

        #Classe Bandit
        elif select == 4:
            hero.class_name = 'Bandit'
            hero.phyAttack = 14
            hero.max_phy_attack = 24
            hero.magAttack = 10
            hero.max_mag_attack = 20
            hero.phyDef = 10
            hero.magDef = 8
            hero.criticalChance = 8
            hero.hp = 120
            hero.mp = 50
            hero.souls = 0

        #Classe Hunter
        elif select == 5:
            hero.class_name = 'Hunter'
            hero.phyAttack = 12
            hero.max_phy_attack = 22
            hero.magAttack = 9
            hero.max_mag_attack = 19
            hero.phyDef = 11
            hero.magDef = 9
            hero.criticalChance = 9
            hero.hp = 11
            hero.mp = 50
            hero.souls = 0

        #Classe Sorcerer
        elif select == 6:
            hero.class_name = 'Sorcerer'
            hero.phyAttack = 9
            hero.max_phy_attack = 19
            hero.magAttack = 15
            hero.max_mag_attack = 25
            hero.phyDef = 8
            hero.magDef = 15
            hero.criticalChance = 5
            hero.hp = 80
            hero.mp = 100
            hero.souls = 0

        #Classe Pyromancer
        elif select == 7:
            hero.class_name = 'Pyromancer'
            hero.phyAttack = 10
            hero.max_phy_attack = 20
            hero.magAttack = 12
            hero.max_mag_attack = 22
            hero.phyDef = 11
            hero.magDef = 10
            hero.criticalChance = 5
            hero.hp = 100
            hero.mp = 80
            hero.souls = 0

        #Classe Deprived
        elif select == 8:
            hero.class_name = 'Deprived'
            hero.phyAttack = 10
            hero.max_phy_attack = 20
            hero.magAttack = 10
            hero.max_mag_attack = 20
            hero.phyDef = 10
            hero.magDef = 10
            hero.criticalChance = 5
            hero.hp = 110
            hero.mp = 50
            hero.souls = 0

        print('-' * 50)

        print('''
Atributos da Classe:
    
    Classe: {}
    Ataque Físico: {}/{}
    Ataque Mágico: {}/{}
    Defesa Física: {}
    Defesa Mágica: {}
    Chance Crítica: {}%
    HP: {}
    MP: {}
    '''.format(hero.class_name, hero.phyAttack, hero.max_phy_attack, hero.magAttack, 
        hero.max_mag_attack, hero.phyDef, hero.magDef, hero.criticalChance, hero.hp, hero.mp))

        print('''
[ 1 ] CONFIRMAR A ESCOLHA
[ 2 ] VOLTAR
''')

        choose = int(input('Escolha uma opção: '))

        if choose == 1:
            pass
        elif choose == 2:
            hero.choseClass()

    def equipWeapon(self, other):
        self.phyAttack += other.phyAttack
        self.max_phy_attack += other.max_phy_attack
        self.magAttack += other.magAttack
        self.max_mag_attack += other.max_mag_attack
        self.criticalChance += other.critical_chance
        self.weapom = other.name
        print('Você equipou {}!'.format(other.name))


class Equips:
    def __init__(self, ID, name='', phyAttack=0, max_phy_attack=0, magAttack=0, 
        max_mag_attack=0, critical_chance=0, price=0):
        self.ID = ID
        self.name = name
        self.phyAttack = phyAttack
        self.max_phy_attack = max_phy_attack
        self.magAttack = magAttack
        self.max_mag_attack = max_mag_attack
        self.critical_chance = critical_chance
        self.price = price


class Monster:
    def __init__(self, name='', phyAttack=50, max_phy_attack=60, magAttack=65, max_mag_attack=75, 
        phyDef=40, magDef=35, hp=500, mp=100, souls=50):
        self.name = name
        self.phyAttack = phyAttack
        self.max_phy_attack = max_phy_attack
        self.magAttack = magAttack
        self.max_mag_attack = max_mag_attack
        self.phyDef = phyDef
        self.magDef = magDef
        self.hp = hp
        self.mp = mp
        self.souls = souls

    def attack(self, other):
        #dano = self.phyAttack - other.phyDef
        dano = random.randint(self.phyAttack, self.max_phy_attack) - other.phyDef
        other.hp -= dano

        sleep(1)
        if other.hp <= 0:
            print('{}:'.format(self.name))
            print('Você recebeu {} de dano!'.format(dano))

        else:
            print('{}:'.format(self.name))
            print('Você recebeu {} de dano!'.format(dano))
        #dano = 0

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
        dano = random.randint(self.phyAttack, self.max_phy_attack) - other.phyDef

        hero.critChance()
        if crit:
            dano *= 2

        other.hp -= dano

        sleep(1)
        print('STATUS DA BATALHA:')
        print('------------------\n')

        if other.hp <= 0:
            print('{}:'.format(self.name))
            other.hp = 0
            hero.souls += other.souls
            if crit:
                print('ATAQUE CRÍTICO!')
            print('Você causou {} de dano no inimigo\n'.format(dano))
            print('Parabéns, você derrotou {}!'.format(other.name))
            print('Você adquiriu {} souls'.format(other.souls))

        else:
            print('{}:'.format(self.name))
            if crit:
                print('ATAQUE CRÍTICO!')
            print('Você causou {} de dano no inimigo'.format(dano))
            print('HP {}: {}\n'.format(other.name, other.hp))


    def estusFlask(self):
        if self.estus_flask > 0:
            self.estus_flask -= 1
            self.hp += 100

            sleep(0.5)
            if self.hp > max_hp:
                self.hp = max_hp
            print('Você recuperou 100 pontos de vida!\n'.format(self.estus_flask))
        
        else:
            print('Você não possui Estus Flask!')


    def magic(self, other):
        pass


    def critChance(self):
        global crit 

        crit = False
        critical = random.randint(0, 100)

        if critical <= self.criticalChance:
            crit = True
            return crit


class Store:
    def __init__(self, swords, shields):
        self.swords = swords

    def weaponStore(self):
        print('-=' * 15)
        print('Espadas'.center(30))
        print('-=' * 15)

        for i in self.swords:
            print('''
Código de compra: {}
Nome: {}
Ataque físico: {}/{}
Ataque mágico: {}/{}
Chance Crítica: {}%
Preço: {} Souls'''.format(i.ID, i.name, i.phyAttack, i.max_phy_attack, i.magAttack, 
    i.max_mag_attack, i.critical_chance, i.price))

            print('-' * 25)

        buy = int(input('Digite o código de compra ou 0 para voltar: '))
        if buy == 0:
            pass
        else:
            check = int(input('''
                
                |[1 - CONFIRMAR]| |[2 - CANCELAR]|
                
                Escolha uma opção: '''))
            
            if check == 1:
                if buy == 1:
                    hero.equipWeapon(broken_straight_sword)
                elif buy == 2:
                    hero.equipWeapon(straight_sword)
                elif buy == 3:
                    hero.equipWeapon(bastard_sword)
                elif buy == 4:
                    hero.equipWeapon(straight_sword_hilt)


# Menu de batalha
def battle_interface(enemy):
    global max_hp

    #Numero de rodadas por batalha
    turn = 0

    while True:
        turn += 1

        if turn == 1:
            max_hp = hero.hp

       	sleep(1)
        print('-' * 50)
        choice = int(input("""
------------------------------------------
| Vida: {}   | Mana: {}  | Qtd Estus: {} |
------------------------------------------
  

 -======================-
 *[ 1 ] ATACAR          *
 *[ 2 ] ESTUS FLASK     *
 *[ 3 ] FUGIR           *
 -======================-

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
#ID, name='', phyAttack=0, max_phy_attack=0, magAttack=0, max_mag_attack=0, critical_chance=0, price=0)
broken_straight_sword = Equips(1, 'Broken Straight Sword', 10, 15, 0, 0, 0, 200)
straight_sword = Equips(2, 'Straight Sword', 20, 25, 0, 0, 5, 500)
bastard_sword = Equips(3, 'Bastard Sword', 30, 37, 0, 0, 5, 1500)
straight_sword_hilt = Equips(4, 'Straight Sword Hilt', 40, 50, 0, 0, 10, 2000)

#Lista dos objetos swords que suprirá a loja
swords = [broken_straight_sword, straight_sword, bastard_sword, straight_sword_hilt]

#Great Swords:

#-------------------------------------------------------------------------------------------
#Objects: BOSSES  |
#_________________|
#name='', phyAttack=50, max_phy_attack=60, magAttack=65, max_mag_attack=75, phyDef=40, 
#magDef=35, hp=500, mp=100, souls=50

asylum_demon = Monster('Asylum Demon', 25, 35, 0, 0, 15, 30, 300, 100, 500)


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
store = Store(swords, [])

#Escolher o nome do personagem
hero.createCharacter()

#Escolher a classe do personagem
hero.choseClass()


#Equipando a arma
#hero.equipWeapom(straight_sword_hilt)


store.weaponStore()

battle_interface(asylum_demon)



#Reaproveitar código
'''

Atributos da Classe:
    
(Status player)

    Classe: {}
    Ataque Físico: {}
    Ataque Mágico: {}
    Defesa Física: {}
    Defesa Mágica: {}
    HP: {}
    MP: {}
    .format(hero.class_name, hero.phyAttack, hero.magAttack, hero.phyDef, hero.magDef, hero.hp, hero.mp))
'''




#print(hero.__dict__)







