from time import sleep
import random
import math

class Class:
    def __init__(self, name='', phyAttack=0, max_phy_attack=0, magAttack=0, max_mag_attack=0, 
        phyDef=0, magDef=0, criticalChance=0, hp=0, mp=0, souls=0, level=1, weapom='', 
        shield='', estus_flask=2, class_name='', xp=0):
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
        self.xp = xp

    def createCharacter(self):
        print('-' * 60)
        print('CRIAÇÃO DE PERSONAGEM'.center(60))
        print()
        self.name = str(input('Digite o nome do personagem: '))

    def chooseClass(sef):
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
            hero.souls = 3000

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
            hero.souls = 500

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
            hero.souls = 500

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
            hero.souls = 500

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
            hero.souls = 500

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
            hero.souls = 500

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
            hero.souls = 500

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
            hero.souls = 500

        print('-' * 50)

        print('''
-=-=-=-=-=-=-=-=-=-=-=            
 Atributos da Classe:
-=-=-=-=-=-=-=-=-=-=-=
    
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


    def learnSpell(self, other):
        self.magAttack += other.magic_power
        self.max_mag_attack += other.max_magic_power

        print('Você aprendeu "{}"!'.format(other.name))


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


class Spells:
    def __init__(self, ID, name, magic_power, max_magic_power, mp_cost, price):
        self.ID = ID
        self.name = name
        self.magic_power = magic_power
        self.max_magic_power = max_magic_power
        self.mp_cost = mp_cost
        self.price = price


class Monster:
    def __init__(self, name='', phyAttack=50, max_phy_attack=60, magAttack=65, max_mag_attack=75, 
        phyDef=40, magDef=35, hp=500, mp=100, souls=500, xp=500):
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
        self.xp = xp

    def attack(self, other):

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
    def __init__(self, name='', phyAttack=1, max_phy_attack=1, magAttack=1, max_mag_attack=1, phyDef=1, magDef=1, criticalChance=1, 
        hp=1, mp=1, souls=0, level=0, weapom='', shield='', estus_flask=2, class_name='', xp=0):
        super(Hero, self).__init__(name, phyAttack, max_phy_attack, magAttack, max_mag_attack, phyDef, magDef, 
            criticalChance, hp, mp, souls, level, weapom, shield, estus_flask, class_name, xp)
        
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
            print('Você adquiriu {} souls e {} pontos de xp!'.format(other.souls, other.xp))
            hero.levelUp(other)

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


    def cast_spells(self, other, spell):
        soma_dano = random.randint(spell.magic_power, spell.max_magic_power) + random.randint(self.magAttack, self.max_mag_attack)
        dano = soma_dano - other.magDef

        if self.mp < spell.mp_cost:
            print('Você não tem mana suficiente para conjurar este feitiço!')

        else:
            self.mp -= spell.mp_cost

            other.hp -= dano

            sleep(1)
            print('STATUS DA BATALHA:')
            print('------------------\n')


            if other.hp <= 0:
                print('{}:'.format(self.name))
                other.hp = 0
                print('Você causou {} de dano no inimigo\n'.format(dano))
                print('Parabéns, você derrotou {}!'.format(other.name))
                print('Você adquiriu {} souls e {} pontos de xp!'.format(other.souls, other.xp))
                hero.levelUp(other)

            else:
                print('{}:'.format(self.name))
                print('Você causou {} de dano no inimigo'.format(dano))
                print('HP {}: {}\n'.format(other.name, other.hp))


    def critChance(self):
        global crit 

        crit = False
        critical = random.randint(0, 100)

        if critical <= self.criticalChance:
            crit = True
            return crit


    def levelUp(self, other):
        global nextLevel, points

        points = 0
        self.xp += other.xp
        nextLevel = 25

        while self.xp >= nextLevel:
            self.level += 1
            points += 2
            self.hp += 10
            self.mp += 5
            self.xp -= nextLevel
            nextLevel = round(nextLevel * 1.5)

        current_level = self.level

        print('''
-------------------------
Level: {}
xp: {}
Próximo level: {}
-------------------------
            '''.format(self.level, self.xp, nextLevel))


    def setLevelPoints(self, points):

        while points > 0:
            print('''
Você tem {} pontos para distribuir

<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>                 
[ 1 ]    Ataque Físico: {}/{}     --> {}/{}
[ 2 ]    Ataque Mágico: {}/{}     --> {}/{}
[ 3 ]    Defesa Física: {}        --> {}
[ 4 ]    Defesa Mágica: {}        --> {}
[ 5 ]    Chance Crítica: {}%      --> {}% 
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
                '''.format(points, self.phyAttack, self.max_phy_attack, self.phyAttack + 2, self.max_phy_attack + 2,
                    self.magAttack, self.max_mag_attack, self.magAttack + 2, self.max_mag_attack + 2, self.phyDef, self.phyDef + 2, 
                    self.magDef, self.magDef + 2, self.criticalChance, self.criticalChance + 0.5))

            up = int(input('Escolha um atributo: '))

            if up == 1:
                self.phyAttack += 2
                self.max_phy_attack += 2
            elif up == 2:
                self.magAttack += 2
                self.max_mag_attack += 2
            elif up == 3:
                self.phyDef += 2
            elif up == 4:
                self.magDef += 2
            elif up == 5:
                self.criticalChance += 0.5

            points -= 1
        bonfire()


class Store:
    def __init__(self, one_handed_swords, two_handed_greatsword, spells_list):
        self.one_handed_swords = one_handed_swords
        self.two_handed_greatsword = two_handed_greatsword
        self.spells_list = spells_list

    def weaponStore(self):

        print('''                 
                                 _            _       
                                | |          (_)      
                                | |      ___  _  ____ 
         (                      | |     / _ \\| |/ _  |
                                | |____| |_| | ( ( | |
            )                   |_______)___/| |\\_||_|
                                           (__/                                             
         ( _   _._
          |_|-'_~_`-._
       _.-'-_~_-~_-~-_`-._
   _.-'_~-_~-_-~-_~_~-_~-_`-._
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |  []  []   []   []  [] |
    |           __    ___   |          
  ._|  []  []  | .|  [___]  |_._._._._._._._._._._._._._._._._.  
  |=|________()|__|()_______|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|  
^^^^^^^^^^^^^^^ === ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^       
    _______      ===   
   <_Loja_>       === 
      ^|^             ===
       |                 ===

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
*    [ 1 ] ESPADAS DE UMA MÃO         *
*    [ 2 ] ESPADAS DE DUAS MÃOS       *
*    [ 3 ] FEITIÇOS                   *
*    [ 4 ] ESCUDOS                    *
*    [ 0 ] SAIR DA LOJA               *
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  

    O que deseja comprar?  
    ''')
       
        option = int(input('Escolha uma opção: '))

        if option == 1:

            print('''

                               _                     _          _                              _ 
                              | |                   | |        | |                            | |
          ___  ____   ____ ___| | _   ____ ____   _ | | ____ _ | |    ___ _ _ _  ___   ____ _ | |
         / _ \\|  _ \\ / _  |___) || \\ / _  |  _ \\ / || |/ _  ) || |   /___) | | |/ _ \\ / ___) || |
        | |_| | | | ( (/ /    | | | ( ( | | | | ( (_| ( (/ ( (_| |  |___ | | | | |_| | |  ( (_| |
         \\___/|_| |_|\\____)   |_| |_|\\_||_|_| |_|\\____|\\____)____|  (___/ \\____|\\___/|_|   \\____|
         
                                  /)
                                 //
                        .-------| |--------------------------------------------.__
                        |WMWMWMW| |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:>
                        `-------| |--------------------------------------------'^^
                                 \\
                                  \\)
    ''')

            print('-=' * 49)
            print('ESPADAS DE UMA MÃO\n'.center(98))
            print('Para guerreiros que além de focar em ataque físico, pretendem focar na defesa. PRÓS: Pode ser equipado em conjunto com escudo / CONTRAS: Ataque mediano')
            print('-=' * 49)

            for i in self.one_handed_swords:
                print('''
--------------------------------------------------------------------------------------------------
!Nome: {} | Ataque físico: {}/{} | Ataque mágico: {}/{} | Chance Crítica: {}%                    
!Preço: {} Souls | Código de compra: {}                                                          
--------------------------------------------------------------------------------------------------'''.format(i.name, i.phyAttack, i.max_phy_attack, i.magAttack, i.max_mag_attack, 
    i.critical_chance, i.price, i.ID))

            print()
            
            while True:
                buy = int(input('Digite o código de compra ou 0 para voltar: '))

                if buy > 5 or buy < 0:
                    print('Erro! Digite um ID válido ou 0 para voltar!')
                    print('-' * 40)
                    continue
                else:
                    break

            if buy == 0:
                store.weaponStore()

            else:

                while True:
                    check = int(input('''
                    
                    |[1 - CONFIRMAR]| |[2 - CANCELAR]|
                    
                    Escolha uma opção: '''))

                    print()

                    if check > 2 or check < 1:
                        print('Erro! Digite uma opção válida!')
                        print('-' * 40)
                    else:
                        break
                
                if check == 1:

                    if buy == 1:
                        if hero.souls >= broken_straight_sword.price:
                            hero.equipWeapon(broken_straight_sword)
                            my_weapons.append(broken_straight_sword)
                            one_handed_swords.remove(broken_straight_sword)

                        else:
                            print('-' * 55)
                            print('Você não tem souls suficiente para comprar este item')
                            print('Souls disponíveis: {}'.format(hero.souls))
                            print('Preço do item: {}'.format(broken_straight_sword.price))
                            store.weaponStore()

                    elif buy == 2:
                        if hero.souls >= straight_sword.price:
                            hero.equipWeapon(straight_sword)
                            my_weapons.append(straight_sword)
                            one_handed_swords.remove(straight_sword)
                        else:
                            print('-' * 55)
                            print('Você não tem souls suficiente para comprar este item')
                            print('Souls disponíveis: {}'.format(hero.souls))
                            print('Preço do item: {}'.format(straight_sword.price))
                            store.weaponStore()

                    elif buy == 3:
                        if hero.souls >= bastard_sword.price:
                            hero.equipWeapon(bastard_sword)
                            my_weapons.append(bastard_sword)
                            one_handed_swords.remove(bastard_sword)

                        else:
                            print('-' * 55)
                            print('Você não tem souls suficiente para comprar este item')
                            print('Souls disponíveis: {}'.format(hero.souls))
                            print('Preço do item: {}'.format(bastard_sword.price))
                            store.weaponStore()

                    elif buy == 4:
                        if hero.souls >= straight_sword_hilt.price:
                            hero.equipWeapon(straight_sword_hilt)
                            my_weapons.append(straight_sword_hilt)
                            one_handed_swords.remove(straight_sword_hilt)
                        else:
                            print('-' * 55)
                            print('Você não tem souls suficiente para comprar este item')
                            print('Souls disponíveis: {}'.format(hero.souls))
                            print('Preço do item: {}'.format(straight_sword_hilt.price))
                            store.weaponStore()

                else:
                    store.weaponStore()

        elif option == 2:

            print('''


                                _                     _          _                              _ 
             _                 | |                   | |        | |                            | |
            | |_ _ _ _  ___ ___| | _   ____ ____   _ | | ____ _ | |    ___ _ _ _  ___   ____ _ | |
            |  _) | | |/ _ (___) || \\ / _  |  _ \\ / || |/ _  ) || |   /___) | | |/ _ \\ / ___) || |
            | |_| | | | |_| |  | | | ( ( | | | | ( (_| ( (/ ( (_| |  |___ | | | | |_| | |  ( (_| |
             \\___)____|\\___/   |_| |_|\\_||_|_| |_|\\____|\\____)____|  (___/ \\____|\\___/|_|   \\____|
                                                                                                  

                                                       _.gd8888888bp._
                                                    .g88888888888888888p.
                                                  .d8888P""       ""Y8888b.
                                                  "Y8P"               "Y8P'
                                                     `.               ,'
                                                       \\     .-.     /
                                                        \\   (___)   /
             .------------------._______________________:__________j
            /                   |                      |           |`-.,_
            \\###################|######################|###########|,-'`
             `------------------'                       :    ___   l
                                                        /   (   )   \\
                                                       /     `-'     \\
                                                     ,'               `.
                                                  .d8b.               .d8b.
                                                  "Y8888p..       ,.d8888P"
                                                    "Y88888888888888888P"
                                                       ""YY8888888PP""
    ''')

            print('-=' * 49)
            print('ESPADAS DE DUAS MÃOS\n'.center(98))
            print('Perfeita para guerreiros que querem focar em ataque físico. PRÓS: Ataque físico anto / CONTRAS: Não pode usar em conjunto de escudos.')
            print('-=' * 49)

            for i in self.two_handed_greatsword:
                print('''
--------------------------------------------------------------------------------------------------
!Nome: {} | Ataque físico: {}/{} | Ataque mágico: {}/{} | Chance Crítica: {}%                    
!Preço: {} Souls | Código de compra: {}                                                          
--------------------------------------------------------------------------------------------------'''.format(i.name, i.phyAttack, i.max_phy_attack, i.magAttack, i.max_mag_attack, 
    i.critical_chance, i.price, i.ID))

            print()

            while True:
                buy = int(input('Digite o código de compra ou 0 para voltar: '))

                if buy > 5 or buy < 0:
                    print('Erro! Digite um ID válido ou 0 para voltar!')
                    print('-' * 40)
                    continue
                else:
                    break

            if buy == 0:
                store.weaponStore()

            else:

                while True:
                    check = int(input('''
                    
                    |[1 - CONFIRMAR]| |[2 - CANCELAR]|
                    
                    Escolha uma opção: '''))

                    print()
                    
                    if check > 2 or check < 1:
                        print('Erro! Digite uma opção válida!')
                        print('-' * 40)
                    else:
                        break
                
                if check == 1:

                    if buy == 1:
                        if hero.souls >= flamberge.price:
                            hero.equipWeapon(flamberge)
                            my_weapons.append(flamberge)
                            two_handed_greatsword.remove(flamberge)
                        else:
                            print('-' * 55)
                            print('Você não tem souls suficiente para comprar este item')
                            print('Souls disponíveis: {}'.format(hero.souls))
                            print('Preço do item: {}'.format(flamberge.price))
                            store.weaponStore()

                    elif buy == 2:
                        if hero.souls >= claymore.price:
                            hero.equipWeapon(claymore)
                            my_weapons.append(claymore)
                            two_handed_greatsword.remove(claymore)
                        else:
                            print('-' * 55)
                            print('Você não tem souls suficiente para comprar este item')
                            print('Souls disponíveis: {}'.format(hero.souls))
                            print('Preço do item: {}'.format(claymore.price))
                            store.weaponStore()

                    elif buy == 3:
                        if hero.souls >= stone_greatsword.price:
                            hero.equipWeapon(stone_greatsword)
                            my_weapons.append(stone_greatsword)
                            two_handed_greatsword.remove(stone_greatsword)
                        else:
                            print('-' * 55)
                            print('Você não tem souls suficiente para comprar este item')
                            print('Souls disponíveis: {}'.format(hero.souls))
                            print('Preço do item: {}'.format(stone_greatsword.price))
                            store.weaponStore()

                    elif buy == 4:
                        if hero.souls >= greatlord_greatsword.price:
                            hero.equipWeapon(greatlord_greatsword)
                            my_weapons.append(greatlord_greatsword)
                            two_handed_greatsword.remove(greatlord_greatsword)
                        else:
                            print('-' * 55)
                            print('Você não tem souls suficiente para comprar este item')
                            print('Souls disponíveis: {}'.format(hero.souls))
                            print('Preço do item: {}'.format(greatlord_greatsword.price))
                            store.weaponStore()

                else:
                    store.weaponStore()

        elif option == 3:

            print('''


                          ██████  ██▓███  ▓█████  ██▓     ██▓      ██████ 
                        ▒██    ▒ ▓██░  ██▒▓█   ▀ ▓██▒    ▓██▒    ▒██    ▒ 
                        ░ ▓██▄   ▓██░ ██▓▒▒███   ▒██░    ▒██░    ░ ▓██▄   
                          ▒   ██▒▒██▄█▓▒ ▒▒▓█  ▄ ▒██░    ▒██░      ▒   ██▒
                        ▒██████▒▒▒██▒ ░  ░░▒████▒░██████▒░██████▒▒██████▒▒
                        ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░▒ ▒▓▒ ▒ ░
                        ░ ░▒  ░ ░░▒ ░      ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░░ ░▒  ░ ░
                        ░  ░  ░  ░░          ░     ░ ░     ░ ░   ░  ░  ░  
                              ░              ░  ░    ░  ░    ░  ░      ░  
                                                                          

                                .-~~~~~~~~~-._       _.-~~~~~~~~~-.
                            __.'              ~.   .~              `.__
                          .'//                  \\./                  \\`.
                        .'//                     |                     \\`.
                      .'// .-~"""""""~~~~-._     |     _,-~~~~"""""""~-. \\`.
                    .'//.-"                 `-.  |  .-'                 "-.\\`.
                  .'//______.============-..   \\ | /   ..-============.______\\`.
                .'______________________________\\|/______________________________`.
    ''')

            print('-=' * 49)
            print('FEITIÇOS\n'.center(98))
            print('Perfeito para magos e Pyromantes ou guereiros que também querem focar em dano mágico'.center(98))
            print('-=' * 49)

            for i in self.spells_list:
                print('''
--------------------------------------------------------------------------------------------------
!Nome: {} | Ataque mágico: {}/{} | Custo de mana: {} | Preço: {} Souls | Código de compra: {}                                                          
--------------------------------------------------------------------------------------------------'''.format(i.name, i.magic_power, i.max_magic_power, i.mp_cost, i.price, i.ID))

            print()
            buy = int(input('Digite o código de compra ou 0 para voltar: '))
            if buy == 0:
                pass
            else:
                check = int(input('''
                    
                    |[1 - CONFIRMAR]| |[2 - CANCELAR]|
                    
                    Escolha uma opção: '''))
                
                if check == 1:

                    if buy == 1:
                        if hero.souls >= soul_arrow.price:
                            hero.learnSpell(soul_arrow)
                            my_spells.append(soul_arrow)
                            spells_list.remove(soul_arrow)
                        else:
                            print('-' * 55)
                            print('Você não tem souls suficiente para comprar este item')
                            print('Souls disponíveis: {}'.format(hero.souls))
                            print('Preço do item: {}'.format(soul_arrow.price))
                            store.weaponStore()

                    elif buy == 2:
                        if hero.souls >= great_soul_arrow.price:
                            hero.learnSpell(great_soul_arrow)
                            my_spells.append(great_soul_arrow)
                            spells_list.remove(great_soul_arrow)
                        else:
                            print('-' * 55)
                            print('Você não tem souls suficiente para comprar este item')
                            print('Souls disponíveis: {}'.format(hero.souls))
                            print('Preço do item: {}'.format(great_soul_arrow.price))
                            store.weaponStore()

                    elif buy == 3:
                        if hero.souls >= soul_spear.price:
                            hero.learnSpell(soul_spear)
                            my_spells.append(soul_spear)
                            spells_list.remove(soul_spear)
                        else:
                            print('-' * 55)
                            print('Você não tem souls suficiente para comprar este item')
                            print('Souls disponíveis: {}'.format(hero.souls))
                            print('Preço do item: {}'.format(soul_spear.price))
                            store.weaponStore()

                    elif buy == 4:
                        if hero.souls >= black_orb.price:
                            hero.learnSpell(black_orb)
                            my_spells.append(black_orb)
                            spells_list.remove(black_orb)
                        else:
                            print('-' * 55)
                            print('Você não tem souls suficiente para comprar este item')
                            print('Souls disponíveis: {}'.format(hero.souls))
                            print('Preço do item: {}'.format(black_orb.price))
                            store.weaponStore()
                    
                else:
                    store.weaponStore()

        elif option == 0:
            pass


# Menu de batalha
def battle_interface(enemy):
    global max_hp, battle_result 
    battle_result = None

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
 *[ 3 ] FEITIÇOS        *
 *[ 4 ] FUGIR           *
 -======================-

Escolha uma opção: """.format(hero.hp, hero.mp, hero.estus_flask)))
        print('-' * 50)

        if choice == 1:
            hero.attack(enemy)
            if enemy.hp <= 0:
                battle_result = True

                return battle_result

        elif choice == 2:
            hero.estusFlask()
            if hero.estus_flask == 0:
                continue

        elif choice == 3:

            for s in spells_list:
                print('''
------------------------------------------------------------------------------------------
!Nome: {} | Ataque Mágico: {}/{} | Custo de Mana: {} | Código de Conjuração: {}                                                                     
------------------------------------------------------------------------------------------'''.format(s.name, s.magic_power, s.max_magic_power, s.mp_cost, s.ID))

            casting_code = int(input('Digite o código de conjuração ou 0 para retornar: '))
            if casting_code == 0:
                pass
            else:
                if casting_code == 1:
                    hero.cast_spells(enemy, soul_arrow)

                elif casting_code == 2:
                    hero.cast_spells(enemy, great_soul_arrow)

                elif casting_code == 3:
                    hero.cast_spells(enemy, soul_spear)

                elif casting_code == 4:
                    hero.cast_spells(enemy, black_orb)


        elif choice == 4:
            print('Você fugiu!')
            break

        enemy.attack(hero)

        if hero.hp <= 0:
            sleep(1)
            print('''

   ___                      ___                 
  / __| __ _  _ __   ___   / _ \\ __ __ ___  _ _ 
 | (_ |/ _` || '  \\ / -_) | (_) |\\ V // -_)| '_|
  \\___|\\__,_||_|_|_|\\___|  \\___/  \\_/ \\___||_|  
                                                


          ,-=-.       ______     _
         /  +  \\     />----->  _|D|_
         | ~~~ |    // -/- /  |_ S _|
         |R.I.P|   //  /  /     |S|
    \\vV,,|_____|V,//_____/VvV,v,|_|/,,vV/,
    ''')
            battle_result = False

            return battle_result


def bonfire():
    print('''

  ___            __ _         
 | _ ) ___ _ _  / _(_)_ _ ___ 
 | _ \\/ _ \\ ' \\|  _| | '_/ -_)
 |___/\\___/_||_|_| |_|_| \\___|
                              

       (                 
        )            [ 01 ] PRÓXIMA FASE   
       (  (              
           )         [ 02 ] SUBIR DE NÍVEL   
     (    (        
      ) /\\ -(        [ 03 ] ACESSAR A LOJA
    (  // | (`'   
  _ -.;_/ \\--._      [ 04 ] HELP
 (_;-// | \\ \\-'.\\   
 ( `.__ _  ___,')      
  `'(_ )_)(_)_)'

        ''')

    while True:
        menu = int(input('Escolha uma opção: '))
        if menu < 1 or menu > 5:
            print('ERRO! Escolha uma opção válida!')
        else:
            break

    if menu == 1:
        pass

    elif menu == 2:
        hero.setLevelPoints(points)

    elif menu == 3:
        store.weaponStore()




#-------------------------------------------------------------------------------------------
#Objects: WEAPONS |
#_________________|

#Swords:
#ID, name='', phyAttack=0, max_phy_attack=0, magAttack=0, max_mag_attack=0, critical_chance=0, price=0)
broken_straight_sword = Equips(1, 'Broken Straight Sword', 200, 300, 0, 0, 0, 200)
straight_sword = Equips(2, 'Straight Sword', 20, 25, 0, 0, 5, 500)
bastard_sword = Equips(3, 'Bastard Sword', 30, 37, 0, 0, 5, 1500)
straight_sword_hilt = Equips(4, 'Straight Sword Hilt', 40, 50, 0, 0, 10, 2000)
#Lista dos objetos swords que suprirá a loja
one_handed_swords = [broken_straight_sword, straight_sword, bastard_sword, straight_sword_hilt]

#Greatswords:
flamberge = Equips(1, 'Flamberge', 18, 23, 0, 0, 0, 500)
claymore = Equips(2, 'Claymore', 27, 33, 0, 0, 5, 1000)
stone_greatsword = Equips(3, 'Stone Greatsword', 35, 45, 0, 0, 0, 1750)
greatlord_greatsword = Equips(4, 'Great Lord Greatsword', 50, 60, 0, 0, 5, 3000)
#Lista dos objetos greatswords que suprirá a loja
two_handed_greatsword = [flamberge, claymore, stone_greatsword, greatlord_greatsword]

#Magic Weapons:


#-------------------------------------------------------------------------------------------
#Objects: SPELLS  |
#_________________|
# name, magic_power, mp_cost
#Sorceres
soul_arrow = Spells(1, 'Soul Arrow', 25, 35, 25, 500)
great_soul_arrow = Spells(2, 'Great Soul Arrow', 35, 45, 35, 1200)
soul_spear = Spells(3, 'Soul Spear', 45, 55, 40, 2000)
black_orb = Spells(4, 'Black Orb', 55, 65, 50, 3000)
#Lista dos objetos Spells que suprirá a loja
spells_list = [soul_arrow, great_soul_arrow, soul_spear, black_orb]

#-------------------------------------------------------------------------------------------
#Objects: BOSSES  |
#_________________|
#name='', phyAttack=50, max_phy_attack=60, magAttack=65, max_mag_attack=75, phyDef=40, 
#magDef=35, hp=500, mp=100, souls=50, xp

asylum_demon = Monster('Asylum Demon', 25, 35, 0, 0, 15, 30, 300, 100, 500, 500)
bell_gargoyle = Monster('Bell Gargoyle', 30, 40, 25, 35, 35, 40, 500, 100, 750, 1000)


#-------------------------------------------------------------------------------------------
#Listas de itens do jogador  |
#____________________________|

my_weapons = []
my_spells = []


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

print('''

██████╗  █████╗ ██████╗ ██╗  ██╗    ███████╗ ██████╗ ██╗   ██╗██╗     ███████╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝██╔═══██╗██║   ██║██║     ██╔════╝
██║  ██║███████║██████╔╝█████╔╝     ███████╗██║   ██║██║   ██║██║     ███████╗
██║  ██║██╔══██║██╔══██╗██╔═██╗     ╚════██║██║   ██║██║   ██║██║     ╚════██║
██████╔╝██║  ██║██║  ██║██║  ██╗    ███████║╚██████╔╝╚██████╔╝███████╗███████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                                              
    ''')


hero = Hero()
store = Store(one_handed_swords, two_handed_greatsword, spells_list)

#Escolher o nome do personagem
hero.createCharacter()

#Escolher a classe do personagem
hero.chooseClass()

store.weaponStore()


battle_interface(asylum_demon)

print('-=' * 20)
if battle_result:
    print('Parabéns você derrotou o primeiro Boss')

bonfire()

battle_interface(bell_gargoyle)

bonfire()





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







