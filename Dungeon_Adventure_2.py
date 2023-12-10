#enemy format:
#['Name']
#[Attack, Poison, Water, Lightning] - brain
#[Health, Attack Range, Attack Power, Armor, Regeneration] - weights
#[Health, Attack Range, Attack Power, Armor, Regeneration]
#[Poison, Water, Lightning, Mana, Mana Gain, Aura] - weights
#[Poison, Water, Lightning, Mana, Mana Gain, Aura]
#[Average Damage, Attacks Survived, Turns Survived]
#[] - active effects
import time
import random
import copy

with open('data.txt', 'a') as data_file:
    data_file.write('beginning of game \n')

#functions to display info
def enemy_lister(opponent):
    print('Name: ' + str(opponent[0][0]))
    print('Health: ' + str(opponent[3][0]) + ' | Attack Range: ' + str(opponent[3][1]) + ' | Attack Power: ' + str(opponent[3][2]) + ' | Armor: ' + str(opponent[3][3]) + ' | Regeneration: ' + str(opponent[3][4]))
    print('Poison: ' + str(opponent[5][0]) + ' | Water: ' + str(opponent[5][1]) + ' | Lightning: ' + str(opponent[5][2]) + ' | Mana: ' + str(opponent[5][3]) + ' | Mana Gain: ' + str(opponent[5][4]) + ' | Aura: ' + str(opponent[5][5]))
    print('\n')

def player_lister(person):
    print('Max Health / Health: '+ str(person[0][5]) + '/' + str(person[0][0]) + '| Attack Range: ' + str(person[0][1]) + '| Attack Power: ' + str(person[0][2]) + '| Armor: ' + str(person[0][3]) + '| Regeneration: ' + str(person[0][4]))
    print('Fire: ' + str(person[1][0]) + '| Poison: ' + str(person[1][1]) + '| Water: ' + str(person[1][2]) + '| Lightning: ' + str(person[1][3]) + '| Max Mana / Mana: '+ str(person[1][7]) + '/' + str(person[1][4]) + '| Mana Gain: ' + str(person[1][5]) + '| Aura: ' + str(person[1][6]))
    print('\n')

#Functions to create enemies
brain = [10, 10, 7, 10]
pstats = [20, 10, 10, 10, 10]
mstats = [10, 10, 10, 20, 10, 10]
enemy_names = [
    'Jim', 
    'Jimmy', 
    'Tummy TIME', 
    'Lysol Whip',
    "Bumblethorn Wobblebottom",
    "Giggledorf Snickerbottom",
    "Whizzlefluff Puddlewick",
    "Snickerdoodle McSparkle",
    "Fluffernutter Quibblesnatch",
    "Muffinflame Fizzlepop",
    "Wobblegum Bumblebreeze",
    "Fizzlenoodle Crumblecakes",
    "Squigglepuff Gigglesnort",
    "Twinkletoes Snickerdust",
    "Snugglekins Bumblebloom",
    "Puddlewhisker Tickletoe",
    "Fluffypaws Snickerwhirl",
    "Whiskerwhizzle Snickerdoodle",
    "Bumbleberry Fuzzletop",
    "Glimmerdust Snickerdazzle",
    "Muffinflame Quizzlequack",
    "Giggledust Wobblewomp",
    "Whiskerwhizzle Snuggleflame",
     "Snickerplume Fizzlewhisk",
    "Quibblequack Wobblegum",
    "Bumblebubble Gigglesnort",
    "Dazzlefluff Snugglewomp",
    "Fizzlequack Wobblewhisk",
    "Quibblebloom Snickerdoodle",
    "Fluttergiggle Snuggleplume",
    "Doodlewhizzle Glimmerbloom",
    "Quizzlewhirl Snickerplume",
    "Glimmerbubble Whizzlewhisk",
    "Fluttertoe Bumblebloom",
    "Quizzleflame Giggledust",
    "Twinklequack Snickerbreeze",
    "Fuzzletop Snugglewhisk",
    "Flamewhisk Bumblefizzle",
    "Quibbletoes Glimmerplume",
    "Fizzlewhizzle Snickerflame",
    "Puddlewhisk Glimmerwhisk",
    "Wobblequack Snickerbubble",
    "Quizzlewhirl Snickerplume",
    "Fizzlewhisk Glimmerplume",
    "Bumblegum Snickerwhirl",
    "Gigglebreeze Wobblebubble",
    "Flutterwhisk Quibblegiggle",
    "Snickerdust Whizzlewhisk",
    "Muffinwhisk Snickerplume",
    "Fizzlebubble Snickerquack",
    "Glimmerwhirl Snickerdust",
    "Snickerwhirl Fizzlequack",
    "Quibbleplume Snugglewhizzle",
    "Bumblewhiskle Glimmerplume",
    "Fizzleflame Snickerwhizzle",
    "Quibbleplume Bumblewhisk",
    "Giggledust Snickerbubble",
    "Snugglewhisk Snickerwhizzle",
    "Bumblequack Whizzlefluff",
    "Quibblewhiskle Snickerflame",
    "Snickerwhisk Quizzlewhirl",
    "Flutterwhiskle Snickerbubble",
    "Bumblewhirl Snugglewhizzle",
    "Fizzlebubble Quibblewhisk",
    "Snickerwhiskle Quizzlewhisk",
    "Glimmerwhiskle Fizzlewhizzle",
    "Flutterbubble Snugglewhizzle",
    "Quibbleflame Snickerwhirl",
    "Snickerwhizzle Whizzlewhisk",
    "Glimmerwhirl Snickerwhiskle",
    "Bumblewhizz Snickerwhirl",
    "Quizzlewhisk Snickerbubble"
               ]

def enemy_namer(names):
    return names[random.randint(0, int(len(names) - 1))]

def data_shifter(list1):
    list2 = []
    list2 += list1
    for x in range(int(len(list2))):
        coin_sides = [1, 2]
        coin_flip = random.choice(coin_sides)
        if coin_flip == 1:
            list2[x] -= 2
        else:
            list2[x] += 2
    return list2

def mstat_maker(list1, stage):
    list2 = []
    list3 = []
    list4 = [0, 0, 0, 0, 0, 0]
    picker = []
    list2 += list1
    iteration = 0
    for x in list2:
        iteration += 1
        if x > 0:
            for y in range(0, int(x + 1)):
                if iteration == 1: list3.append('poison')
                if iteration == 2: list3.append('water')
                if iteration == 3: list3.append('lightning')
                if iteration == 4: list3.append('mana')
                if iteration == 5: list3.append('mana gain')
                if iteration == 6: list3.append('aura')
    for z in range(0, int(stage + 10)):
        picker = random.choice(list3)
        if picker == 'poison':
            list4[0] += 1
        if picker == 'water':
            list4[1] += 2
        if picker == 'lightning':
            list4[2] += 1
        if picker == 'mana':
            list4[3] += 3
        if picker == 'mana gain':
            list4[4] += 1
        if picker == 'aura':
            list4[5] += 2
    return list4
        
def pstat_maker(list1, stage):
    list2 = []
    list3 = []
    list4 = [0, 0, 0, 0, 0]
    picker = []
    list2 += list1
    iteration = 0
    for x in list2:
        iteration += 1
        if x > 0:
            for y in range(0, int(x + 1)):
                if iteration == 1: list3.append('health')
                if iteration == 2: list3.append('attack range')
                if iteration == 3: list3.append('attack power')
                if iteration == 4: list3.append('armor')
                if iteration == 5: list3.append('regeneration')
    for z in range(0, int(stage + 8)):
        picker = random.choice(list3)
        if picker == 'health':
            list4[0] += 3
        if picker == 'attack range':
            list4[1] += 2
        if picker == 'attack power':
            list4[2] += 1
        if picker == 'armor':
            list4[3] += 2
        if picker == 'regeneration':
            list4[4] += 1
    return list4

def fitness_tester(e1, e2, e3, e4):
    if e2 == []:
        e2 = [[],[],[],[],[],[],[1, 1, 1]]
    if e3 == []:
        e3 = [[],[],[],[],[],[],[1, 1, 1]]
    if e4 == []:
        e4 = [[],[],[],[],[],[],[1, 1, 1]]
    e1_score = 0
    e1_score = e1[6][0] / e1[6][2]
    e1_score += e1[6][1]
    e2_score = 0
    e2_score = e2[6][0] / e2[6][2]
    e2_score += e2[6][1]
    e3_score = 0
    e3_score = e3[6][0] / e3[6][2]
    e3_score += e3[6][1]
    e4_score = 0
    e4_score = e4[6][0] / e4[6][2]
    e4_score += e4[6][1]
    if e2_score > e1_score and e2_score > e3_score and e2_score > e4_score:
        weights = []
        weights.append(e2[1])
        weights.append(e2[2])
        weights.append(e2[4])
        return weights
    if e3_score > e2_score and e3_score > e1_score and e3_score > e4_score:
        weights = []
        weights.append(e3[1])
        weights.append(e3[2])
        weights.append(e3[4])
        return weights
    if e4_score > e2_score and e4_score > e3_score and e4_score > e1_score:
        weights = []
        weights.append(e4[1])
        weights.append(e4[2])
        weights.append(e4[4])
        return weights
    else:
        weights = []
        weights.append(e1[1])
        weights.append(e1[2])
        weights.append(e1[4])
        return weights

#combat functions
def combat_decider(hero, villain, choice, initiator, enemy_num):
    if villain == []:
        return []
    villain2 = copy.deepcopy(villain)
    hero2 = copy.deepcopy(hero)
    if initiator == 'p':
        if choice == 1:
            villain2[3][0] -= hero2[0][2]
            roll = random.randint(1, hero[0][1])
            print('You rolled ' + str(roll) + '\n')
            villain2[3][0] -= roll
            villain2[3][0] += villain2[3][3]
            if villain2[3][0] >= villain[3][0]:
               print('No damage\n')
               return villain
            else: 
               print(str(villain[3][0] - villain2[3][0]) + ' damage done\n')
               return villain2
        if choice == 2:
            villain2[3][0] -= hero2[1][0]
            villain2[3][0] += villain2[5][5]
            if villain2[3][0] >= villain[3][0]:
               print('Was not effective\n')
               return villain
            else:
               print(str(villain[3][0] - villain2[3][0]) + ' damage done\n')
               return villain2
        if choice == 3:
            for z in range(0, hero2[1][1]):
              villain2[7] += ['poison']
            return villain2
        if choice == 5:
            villain2[3][0] -= hero2[1][3]
            villain2[3][0] += villain2[5][5]
            if villain2[3][0] >= villain[3][0]:
               print('Was not effective\n')
               return villain
            else:
               print(str(villain[3][0] - villain2[3][0]) + ' damage done\n')
               return villain2
    if initiator == 'e':
        if choice == 1:
           hero2[0][0] -= villain2[3][2]
           hero2[0][0] -= random.randint(1, villain2[3][1])
           hero2[0][0] += hero2[0][3]
           if hero2[0][0] >= hero[0][0]:
               print('No damage\n')
               return hero
           else: 
               print(str(hero[0][0] - hero2[0][0]) + ' damage done\n')
               return hero2
        if choice == 2:
            for v in range(0, villain2[5][0]):
                hero2[2] += ['poison', enemy_num]
            return hero2
        if choice == 4:
            hero2[0][0] -= villain2[5][2]
            hero2[0][0] += hero2[1][6]
            if hero2[0][0] >= hero[0][0]:
               print('Was not effective\n')
               return hero
            else:
                print(str(hero[0][0] - hero2[0][0]) + ' damage done\n')
                return hero2
        
def thinker(list):
    list2 = copy.deepcopy(list)
    list3 = []
    choice = []
    iteration = 0
    for x in list2:
        iteration += 1
        for y in range(0, x):
            if iteration == 1:
                list3 += [1]
            if iteration == 2:
                list3 += [2]
            if iteration == 3:
                list3 += [3]
            if iteration == 4:
                list3 += [4]
    choice = random.choice(list3)
    return choice

#inventory functions
def item_picker(items):
    item_range = []
    for x in items:
        for y in range(0, x[0]):
            item_range.append(x)
    return random.choice(item_range)

item_list =[
    [10, 'hp_increase', 10, 'Fitness Potion', 'Increase max health by 10'],
    [25, 'hp_boost', 15, 'Health Potion', 'Heal fifteen health'],
    [15, 'regen_boost', 1, 'Health Routine', 'Increase regeneration by one'],
    [12, 'armor_boost', 1, 'Heavy Gauntlets', 'Increase Armor by one'],
    [10, 'power_boost', 1, 'Katana', 'Increase attack power by one'],
    [15, 'range_boost', 2, 'Training Manual', 'Increase attack range by two'],
    [15, 'fire_boost', 2, 'Fire Token', 'Increase fire ability by two'],
    [15, 'poison_boost', 1, 'Poison Fang', 'Increase poison ability by one'],
    [15, 'water_boost', 3, 'Water Jug', 'Increase water ability by 3'],
    [15, 'lightning_boost', 2, 'Lightning Rod', 'Increase lightning ability by two'],
    [15, 'mana_boost', 10, 'Divine Almonds', 'Regain ten mana'],
    [11, 'mana_increase', 10, 'Wisdom of Sages', 'Increase max mana by ten'],
    [8, 'aura_boost', 1, 'Spiritual Strength', ' Increase aura by one'],
    [17, 'pistol', 6, 'Flintlock', 'Deal six damage to an enemy'],
    [6, 'hp_increase', 30, 'Legendary Fitness Potion', 'Increase max health by thirty'],
    [8, 'hp_boost', 30, 'Legendary Health Potion', 'Heal forty health'],
    [3, 'regen_boost', 3, 'Legendary Health Routine', 'Increase regeneration by three'],
    [3, 'armor_boost', 3, 'Legendary Heavy Gauntlets', 'Increase Armor by three'],
    [3, 'power_boost', 4, 'Legendary Katana', 'Increase attack power by four'],
    [4, 'range_boost', 7, 'Legendary Training Manual', 'Increase attack range by seven'],
    [4, 'fire_boost', 5, 'Legendary Fire Token', 'Increase fire ability by five'],
    [4, 'poison_boost', 3, 'Legendary Poison Fang', 'Increase poison ability by three'],
    [4, 'water_boost', 7, 'Legendary Water Jug', 'Increase water ability by seven'],
    [4, 'lightning_boost', 5, 'Legendary Lightning Rod', 'Increase lightning ability by five'],
    [4, 'mana_boost', 20, 'Legendary Divine Almonds', 'Regain twenty mana'],
    [3, 'mana_increase', 10, 'Legendary Wisdom of Sages', 'Increase max mana by ten'],
    [3, 'aura_boost', 3, 'Legendary Spiritual Strength', ' Increase aura by three'],
    [7, 'pistol', 18, 'Legendary Flintlock', 'Deal eighteen damage to an enemy']
    ]

#player stats [hp, attack range, attack power, armor, regeneration, max hp], [fire, posion, water, lightning, mana, mana gain, aura, max mana] [status effects]
player_stats = [[50, 5, 0, 0, 0, 50], [2, 2, 3, 4, 20, 1, 0, 20], ['active effects']]
inventory = []


#Main game loop
level = 0
for fishrem in range(99):
    if player_stats[0][0] < 1:
            break
    print('Your stats are..')
    time.sleep(1)
    player_lister(player_stats)
    time.sleep(3)
    for up in range(0, 3):
        print('What would you like to upgrade?')
        print("1. Max health 2. Attack Range, 3. Attack Power, 4. Armor, 5. Regeneration")
        print("6. Fire, 7. Poison, 8. Water, 9. Lightning, 10. Max Mana, 11. Mana Gain, 12. Aura")
        upgrade = input()
        if upgrade.isnumeric() == True:
                upgrade_choice = int(upgrade)
        else: upgrade_choice = 1
        if upgrade_choice == 1:
            player_stats[0][5] += 5
        if upgrade_choice == 2:
            player_stats[0][1] += 2
        if upgrade_choice == 3:
            player_stats[0][2] += 1
        if upgrade_choice == 4:
            player_stats[0][3] += 2
        if upgrade_choice == 5:
            player_stats[0][4] += 1
        if upgrade_choice == 6:
            player_stats[1][0] += 2
        if upgrade_choice == 7:
            player_stats[1][1] += 1
        if upgrade_choice == 8:
            player_stats[1][2] += 1
        if upgrade_choice == 9:
            player_stats[1][3] += 2
        if upgrade_choice == 10:
            player_stats[1][7] += 5
        if upgrade_choice == 11:
            player_stats[1][5] += 1
        if upgrade_choice == 12:
            player_stats[1][6] += 2

    print('Your stats are now..')
    time.sleep(1)
    player_lister(player_stats)
    time.sleep(3)


    inventory.append(item_picker(item_list))
    print('You have found ' + str(inventory[-1][3]) + '\n')
    time.sleep(2)
    level += 1
    print('Level ' + str(level) + '\n')
    time.sleep(1)
    player_stats[2] = []

    #enemy creation loop
    enemy_amount = random.randint(3, 5)
    enemy_one = []
    enemy_two = []
    enemy_three = []
    enemy_four = []
    leveler = level
    leveler -= enemy_amount * 2
    for enemy_loop in range(1, enemy_amount):
        
        enemy_creation1 = []
        enemy_creation2 = []
        
        enemy_creation2.append(enemy_namer(enemy_names))
        enemy_creation1.append(enemy_creation2)
        enemy_creation2 = []
        
        enemy_creation2 += data_shifter(brain)
        enemy_creation1.append(enemy_creation2)
        enemy_creation2 = []
        
        enemy_creation2 += data_shifter(pstats)
        enemy_creation1.append(enemy_creation2)
        enemy_creation1.append(pstat_maker(enemy_creation2, leveler))
        enemy_creation2 = []
       
        enemy_creation2 += data_shifter(mstats)
        enemy_creation1.append(enemy_creation2)
        enemy_creation1.append(mstat_maker(enemy_creation2, leveler))
        enemy_creation2 = []

        enemy_creation1.append([1, 1, 1])
        enemy_creation1.append(['active effects'])
        
        
        
        

        #final product
        if enemy_loop == 1:
            enemy_one = enemy_creation1
            enemy_one[3][1] += 2
            enemy_one[3][0] += 4
            enemy_one[5][0] += 1
            enemy_one[5][1] += 1
            enemy_one[5][2] += 1
            enemy_one[5][3] += 2
            enemy_one[5][4] += 1
            enemy_lister(enemy_one)
            time.sleep(3)
        if enemy_loop == 2:
            enemy_two = enemy_creation1
            enemy_two[3][1] += 2
            enemy_two[3][0] += 4
            enemy_two[5][0] += 1
            enemy_two[5][1] += 1
            enemy_two[5][2] += 1
            enemy_two[5][3] += 4
            enemy_two[5][4] += 1
            enemy_lister(enemy_two)
            time.sleep(3)
        if enemy_loop == 3:
            enemy_three = enemy_creation1
            enemy_three[3][1] += 2
            enemy_three[3][0] += 4
            enemy_three[5][0] += 1
            enemy_three[5][1] += 1
            enemy_three[5][2] += 1
            enemy_three[5][3] += 4
            enemy_three[5][4] += 1
            enemy_lister(enemy_three)
            time.sleep(3)
        if enemy_loop == 4:
           enemy_four = enemy_creation1
           enemy_four[3][1] += 2
           enemy_four[3][0] += 4
           enemy_four[5][0] += 1
           enemy_four[5][1] += 1
           enemy_four[5][2] += 1
           enemy_four[5][3] += 4
           enemy_four[5][4] += 1
           enemy_lister(enemy_four)
           time.sleep(3)
    with open('data.txt', 'a') as data_file:
        data_file.write('\nround beginning\n')
        data_file.write(str(player_stats) + '\n')
        data_file.write(str(enemy_one) + '\n')
        data_file.write(str(enemy_two) + '\n')
        data_file.write(str(enemy_three) + '\n')
        data_file.write(str(enemy_four) + '\n')
       
    #main fight loop
    for battle_loop in range(0, 999):
        if player_stats[0][0] < player_stats[0][5]:
            player_stats[0][0] += player_stats[0][4]
        if player_stats[1][4] < player_stats[1][7]:
            player_stats[1][4] += player_stats[1][5]
        if player_stats[0][0] > player_stats[0][5]:
            player_stats[0][0] -= 2
        if player_stats[1][4] > player_stats[1][7]:
            player_stats[1][4] -= 1
        #end the fight upon deaths
        if enemy_one == [] or enemy_one[3][0] < 1:
            if enemy_two == [] or enemy_two[3][0] < 1:
                if enemy_three == [] or enemy_three[3][0] < 1:
                    if enemy_four == [] or enemy_four[3][0] < 1:
                        data_spread = fitness_tester(enemy_one, enemy_two, enemy_three, enemy_four)
                        with open('data.txt', 'a') as data_file:
                            data_file.write('\nround end\n')
                            data_file.write(str(player_stats) + '\n')
                            data_file.write(str(enemy_one) + '\n')
                            data_file.write(str(enemy_two) + '\n')
                            data_file.write(str(enemy_three) + '\n')
                            data_file.write(str(enemy_four) + '\n')
                            data_file.write(str(data_spread) + ' == weights for next enemies\n')
                            brain = data_spread[0]
                            pstats = data_spread[1]
                            mstats = data_spread[2]
                        break
        if player_stats[0][0] < 1:
            break

        print('Your stats are..')
        time.sleep(1)
        player_lister(player_stats)
        print('\n')
        time.sleep(3)

        print('What would you like to do? \n1. Use an ability | 2. Use an item | 3. Search for an item \n')
        player_choice_str = input()
        if player_choice_str.isnumeric() == True:
            player_choice = int(player_choice_str)
        else: player_choice = 1
        
        if player_choice == 3:
            inventory.append(item_picker(item_list))
            print('You have found ' + str(inventory[-1][3]) + '\n')
            time.sleep(2)

        #inventory control
        elif player_choice == 2 and len(inventory) > 0:
            search1 = 0
            print(' ')
            for search2 in inventory:
                search1 += 1
                print(str(search1) + '. ' + search2[3] + ': ' + search2[4])
            print('\nWhat item number would you like to use?\n')
            pick = input()
            if pick.isnumeric() == True :
                picked = int(pick)
                picked -= 1
                if picked > int(len(inventory) - 1):
                    for reduce in range(99999):
                        picked -= 1
                        if picked == int(len(inventory) - 1):
                            break
                    
                    
                #item effects on player
                if inventory[picked][1] == 'hp_increase':
                    player_stats[0][5] += inventory[picked][2]
                    print('Your health is now: ' + str(player_stats[0][5]) + '/' + str(player_stats[0][0]) + '\n')
                if inventory[picked][1] == 'hp_boost':
                    player_stats[0][0] += inventory[picked][2]
                    print('Your health is now: ' + str(player_stats[0][5]) + '/' + str(player_stats[0][0]) + '\n')
                if inventory[picked][1] == 'regen_boost':
                    player_stats[0][4] += inventory[picked][2]
                    print('Your regeneration is now: ' + str(player_stats[0][4]) + '\n')
                if inventory[picked][1] == 'armor_boost':
                    player_stats[0][3] += inventory[picked][2]
                    print('Your armor is now: ' + str(player_stats[0][3]) + '\n')
                if inventory[picked][1] == 'power_boost':
                    player_stats[0][2] += inventory[picked][2]
                    print('Your attack power is now: ' + str(player_stats[0][2]) + '\n')
                if inventory[picked][1] == 'range_boost':
                    player_stats[0][1] += inventory[picked][2]
                    print('Your attack range is now: ' + str(player_stats[0][1]) + '\n')
                if inventory[picked][1] == 'fire_boost':
                    player_stats[1][0] += inventory[picked][2]
                    print('Your fire ability is now: ' + str(player_stats[1][0]) + '\n')
                if inventory[picked][1] == 'poison_boost':
                    player_stats[1][1] += inventory[picked][2]
                    print('Your poison ability is now: ' + str(player_stats[1][1]) + '\n')
                if inventory[picked][1] == 'water_boost':
                    player_stats[1][2] += inventory[picked][2]
                    print('Your water ability is now: ' + str(player_stats[1][2]) + '\n')
                if inventory[picked][1] == 'lightning_boost':
                    player_stats[1][3] += inventory[picked][2]
                    print('Your lightning ability is now: ' + str(player_stats[1][3]) + '\n')
                if inventory[picked][1] == 'mana_boost':
                    player_stats[1][4] += inventory[picked][2]
                    print('Your mana is now: ' + str(player_stats[1][4]) + '\n')
                if inventory[picked][1] == 'mana_increase':
                    player_stats[1][7] += inventory[picked][2]
                    print('Your max mana is now: ' + str(player_stats[1][7]) + '\n')
                if inventory[picked][1] == 'aura_boost':
                    player_stats[1][6] += inventory[picked][2]
                    print('Your aura is now: ' + str(player_stats[1][6]) + '\n')
                if inventory[picked][1] == 'pistol':
                    pistol_choice = input('Choose an opponent: 1, 2, 3, 4 \n')
                    if pistol_choice == '4' and not enemy_four == []:
                        enemy_four[3][0] -= inventory[picked][2]
                    if pistol_choice == '3' and not enemy_three == []:
                        enemy_three[3][0] -= inventory[picked][2]
                    if pistol_choice == '2' and not enemy_two == []:
                        enemy_two[3][0] -= inventory[picked][2]
                    else: enemy_one[3][0] -= inventory[picked][2]
                inventory.remove(inventory[picked])
                time.sleep(2)
            else:
                print('You have failed to choose\n')
                time.sleep(2)

        else:
            for combat_loop_physical in range(0, 9999):
                    
                print('Who are you targeting? \n1. Enemy #1 \n2. Enemy #2\n3. Enemy #3\n4. Enemy #4\n5. Self')
                player_choice_str = input()
                if player_choice_str.isnumeric() == True:
                    player_choice = int(player_choice_str)
                else: player_choice = 5

                if player_choice == 5:
                    print('You heal with water\n')
                    player_stats[0][0] += player_stats[1][2] * 2
                    player_stats[1][4] -= player_stats[1][2]
                    time.sleep(1)
                    print('Your health is now: ' + str(player_stats[0][5]) + '/' + str(player_stats[0][0]) + '\n')
                    time.sleep(1)
                    print('Your mana is at: ' + str(player_stats[1][7]) + '/' + str(player_stats[1][4]) + '\n')
                    time.sleep(1)


                if player_choice == 1:
                    if enemy_one == [] or enemy_one[3][0] < 1:
                        print('\nThere is no enemy there \n')
                        continue
                    else:
                        print('\nWhat ability do you use? 1. Physical Attack | 2. Fire | 3. Poison | 4. Lightning\n')
                        player_choice_str1 = input()
                        if player_choice_str1.isnumeric() == True:
                            player_choice1 = int(player_choice_str1)
                        else: player_choice1 = 1
                
                        if player_choice1 == 2:
                            player_stats[1][4] -= player_stats[1][0] * 2
                            enemy_one = combat_decider(player_stats, enemy_one, 2, 'p', 0)
                            enemy_one[6][1] += 0.5
                            if not enemy_two == []:
                                if not enemy_two[3][0] < 1:
                                    enemy_two = combat_decider(player_stats, enemy_two, 2, 'p', 0)
                                    enemy_two[6][1] += 0.5
                            if not enemy_three == []:
                                if not enemy_three[3][0] < 1:
                                    enemy_three = combat_decider(player_stats, enemy_three, 2, 'p', 0)
                                    enemy_three[6][1] += 0.5
                            if not enemy_four == []:
                                if not enemy_four[3][0] < 1:
                                    enemy_four = combat_decider(player_stats, enemy_four, 2, 'p', 0)
                                    enemy_four[6][1] += 0.5
                            print('You attacked with fire!\n')
                            time.sleep(1)
                            print('Your mana is at: ' + str(player_stats[1][7]) + '/' + str(player_stats[1][4]) + '\n')
                            time.sleep(1)
                        if player_choice1 == 3:
                            player_stats[1][4] -= player_stats[1][1] * 3
                            enemy_one = combat_decider(player_stats, enemy_one, 3, 'p', 0)
                            print('You attacked with poison!\n')
                            time.sleep(1)
                            print('Your mana is at: ' + str(player_stats[1][7]) + '/' + str(player_stats[1][4]) + '\n')
                            time.sleep(1)
                            enemy_one[6][1] += player_stats[1][1]
                        if player_choice1 == 4:
                            player_stats[1][4] -= player_stats[1][3]
                            enemy_one = combat_decider(player_stats, enemy_one, 5, 'p', 0)
                            print('You attacked with lightning!\n')
                            time.sleep(1)
                            print('Your mana is at: ' + str(player_stats[1][7]) + '/' + str(player_stats[1][4]) + '\n')
                            time.sleep(1)
                            enemy_one[6][1] += 1
                        if player_choice1 == 1:
                            print('You attacked with your weapon!\n')
                            time.sleep(1)
                            enemy_one = combat_decider(player_stats, enemy_one, 1, 'p', 0)
                            enemy_one[6][1] += 1


                if player_choice == 2:
                    if enemy_two == [] or enemy_two[3][0] < 1:
                        print('\nThere is no enemy there \n')
                        continue
                    else:
                        print('\nWhat ability do you use? 1. Physical Attack | 2. Fire | 3. Poison | 4. Lightning\n')
                        player_choice_str1 = input()
                        if player_choice_str1.isnumeric() == True:
                            player_choice1 = int(player_choice_str1)
                        else: player_choice1 = 1
                
                        if player_choice1 == 2:
                            player_stats[1][4] -= player_stats[1][0] * 2
                            enemy_two = combat_decider(player_stats, enemy_two, 2, 'p', 0)
                            enemy_two[6][1] += 0.5
                            if not enemy_one == []:
                                if not enemy_one[3][0] < 1:
                                    enemy_one = combat_decider(player_stats, enemy_one, 2, 'p', 0)
                                    enemy_one[6][1] += 0.5
                            if not enemy_three == []:
                                if not enemy_three[3][0] < 1:
                                    enemy_three = combat_decider(player_stats, enemy_three, 2, 'p', 0)
                                    enemy_three[6][1] += 0.5
                            if not enemy_four == []:
                                if not enemy_four[3][0] < 1:
                                    enemy_four = combat_decider(player_stats, enemy_four, 2, 'p', 0)
                                    enemy_four[6][1] += 0.5
                            print('You attacked with fire!\n')
                            time.sleep(1)
                            print('Your mana is at: ' + str(player_stats[1][7]) + '/' + str(player_stats[1][4]) + '\n')
                            time.sleep(1)
                        if player_choice1 == 3:
                            player_stats[1][4] -= player_stats[1][1] * 3
                            enemy_two = combat_decider(player_stats, enemy_two, 3, 'p', 0)
                            print('You attacked with poison!\n')
                            time.sleep(1)
                            print('Your mana is at: ' + str(player_stats[1][7]) + '/' + str(player_stats[1][4]) + '\n')
                            time.sleep(1)
                            enemy_two[6][1] += player_stats[1][1]
                        if player_choice1 == 4:
                            player_stats[1][4] -= player_stats[1][3]
                            enemy_two = combat_decider(player_stats, enemy_two, 5, 'p', 0)
                            print('You attacked with lightning!\n')
                            time.sleep(1)
                            print('Your mana is at: ' + str(player_stats[1][7]) + '/' + str(player_stats[1][4]) + '\n')
                            time.sleep(1)
                            enemy_two[6][1] += 1
                        if player_choice1 == 1:
                            print('You attacked with your weapon!\n')
                            time.sleep(1)
                            enemy_two = combat_decider(player_stats, enemy_two, 1, 'p', 0)
                            enemy_two[6][1] += 1


                if player_choice == 3:
                    if enemy_three == [] or enemy_three[3][0] < 1:
                        print('\nThere is no enemy there \n')
                        continue
                    else:
                        print('\nWhat ability do you use? 1. Physical Attack | 2. Fire | 3. Poison | 4. Lightning\n')
                        player_choice_str1 = input()
                        if player_choice_str1.isnumeric() == True:
                            player_choice1 = int(player_choice_str1)
                        else: player_choice1 = 1
                
                        if player_choice1 == 2:
                            player_stats[1][4] -= player_stats[1][0] * 2
                            enemy_three = combat_decider(player_stats, enemy_three, 2, 'p', 0)
                            enemy_three[6][1] += 0.5
                            if not enemy_two == []:
                                if not enemy_two[3][0] < 1:
                                    enemy_two = combat_decider(player_stats, enemy_two, 2, 'p', 0)
                                    enemy_two[6][1] += 0.5
                            if not enemy_one == []:
                                if not enemy_one[3][0] < 1:
                                    enemy_one = combat_decider(player_stats, enemy_one, 2, 'p', 0)
                                    enemy_one[6][1] += 0.5
                            if not enemy_four == []:
                                if not enemy_four[3][0] < 1:
                                    enemy_four = combat_decider(player_stats, enemy_four, 2, 'p', 0)
                                    enemy_four[6][1] += 0.5
                            print('You attacked with fire!\n')
                            time.sleep(1)
                            print('Your mana is at: ' + str(player_stats[1][7]) + '/' + str(player_stats[1][4]) + '\n')
                            time.sleep(1)
                        if player_choice1 == 3:
                            player_stats[1][4] -= player_stats[1][1] * 3
                            enemy_three = combat_decider(player_stats, enemy_three, 3, 'p', 0)
                            print('You attacked with poison!\n')
                            time.sleep(1)
                            print('Your mana is at: ' + str(player_stats[1][7]) + '/' + str(player_stats[1][4]) + '\n')
                            time.sleep(1)
                            enemy_three[6][1] += player_stats[1][1]
                        if player_choice1 == 4:
                            player_stats[1][4] -= player_stats[1][3]
                            enemy_three = combat_decider(player_stats, enemy_three, 5, 'p', 0)
                            print('You attacked with lightning!\n')
                            time.sleep(1)
                            print('Your mana is at: ' + str(player_stats[1][7]) + '/' + str(player_stats[1][4]) + '\n')
                            time.sleep(1)
                            enemy_three[6][1] += 1
                        #WHY DOES ELSE NOT WORK HERE? or on the others
                        if player_choice1 == 1:
                            print('You attacked with your weapon!\n')
                            time.sleep(1)
                            enemy_three = combat_decider(player_stats, enemy_three, 1, 'p', 0)
                            enemy_three[6][1] += 1


                if player_choice == 4:
                    if enemy_four == [] or enemy_four[3][0] < 1:
                        print('\nThere is no enemy there \n')
                        continue
                    else:
                        print('\nWhat ability do you use? 1. Physical Attack | 2. Fire | 3. Poison | 4. Lightning\n')
                        player_choice_str1 = input()
                        if player_choice_str1.isnumeric() == True:
                            player_choice1 = int(player_choice_str1)
                        else: player_choice1 = 1
                
                        if player_choice1 == 2:
                            player_stats[1][4] -= player_stats[1][0] * 2
                            enemy_four = combat_decider(player_stats, enemy_four, 2, 'p', 0)
                            enemy_four[6][1] += 0.5
                            if not enemy_two == []:
                                if not enemy_two[3][0] < 1:
                                    enemy_two = combat_decider(player_stats, enemy_two, 2, 'p', 0)
                                    enemy_two[6][1] += 0.5
                            if not enemy_one == []:
                                if not enemy_one[3][0] < 1:
                                    enemy_one = combat_decider(player_stats, enemy_one, 2, 'p', 0)
                                    enemy_one[6][1] += 0.5
                            if not enemy_three == []:
                                if not enemy_three[3][0] < 1:
                                    enemy_three = combat_decider(player_stats, enemy_three, 2, 'p', 0)
                                    enemy_three[6][1] += 0.5
                            print('You attacked with fire!\n')
                            time.sleep(1)
                            print('Your mana is at: ' + str(player_stats[1][7]) + '/' + str(player_stats[1][4]) + '\n')
                            time.sleep(1)
                        if player_choice1 == 3:
                            player_stats[1][4] -= player_stats[1][1] * 3
                            enemy_four = combat_decider(player_stats, enemy_four, 3, 'p', 0)
                            print('You attacked with poison!\n')
                            time.sleep(1)
                            print('Your mana is at: ' + str(player_stats[1][7]) + '/' + str(player_stats[1][4]) + '\n')
                            time.sleep(1)
                            enemy_four[6][1] += player_stats[1][1]
                        if player_choice1 == 4:
                            player_stats[1][4] -= player_stats[1][3]
                            enemy_four = combat_decider(player_stats, enemy_four, 5, 'p', 0)
                            print('You attacked with lightning!\n')
                            time.sleep(1)
                            print('Your mana is at: ' + str(player_stats[1][7]) + '/' + str(player_stats[1][4]) + '\n')
                            time.sleep(1)
                            enemy_four[6][1] += 1        
                        if player_choice1 == 1:
                            print('You attacked with your weapon!\n')
                            time.sleep(1)
                            enemy_four = combat_decider(player_stats, enemy_four, 1, 'p', 0)
                            enemy_four[6][1] += 1
                break
        #enemy attacks on player
        for enemy_loop in range(1, 5):
            time.sleep(2)
            if enemy_loop == 1:
                if not enemy_one == [] and enemy_one[3][0] > 0:
                    decision = thinker(enemy_one[1])
                    if decision == 3:
                        enemy_one[3][0] += enemy_one[5][1]
                        enemy_one[5][3] -= enemy_one[5][1]
                        print(str(enemy_one[0][0]) + ' Uses water to heal!\n')
                    else:
                        if decision == 1:
                            print(str(enemy_one[0][0]) + ' attacks with a weapon!\n')
                            time.sleep(1)
                            player_hp1 = player_stats[0][0]
                            player_stats = combat_decider(player_stats, enemy_one, decision, 'e', 1)
                            player_hp2 = player_stats[0][0]
                            enemy_one[6][0] += player_hp1 - player_hp2
                            time.sleep(1)
                            print('Your health is now: ' + str(player_stats[0][5]) + '/' + str(player_stats[0][0]) + '\n')
                        if decision == 2:
                            enemy_one[5][3] -= enemy_one[5][0] * 3
                            print(str(enemy_one[0][0]) + ' attacks with poison!\n')
                            player_stats = combat_decider(player_stats, enemy_one, decision, 'e', 1)
                            time.sleep(1)
                        if decision == 4:
                            enemy_one[5][3] -= enemy_one[5][2]
                            print(str(enemy_one[0][0]) + ' attacks with lightning!\n')
                            time.sleep(1)
                            player_hp1 = player_stats[0][0]
                            player_stats = combat_decider(player_stats, enemy_one, decision, 'e', 1)
                            player_hp2 = player_stats[0][0]
                            enemy_one[6][0] += player_hp1 - player_hp2
                            time.sleep(1)
                            print('Your health is now: ' + str(player_stats[0][5]) + '/' + str(player_stats[0][0]) + '\n')

            if enemy_loop == 2:
                if not enemy_two == [] and enemy_two[3][0] > 0:
                    decision = thinker(enemy_two[1])
                    if decision == 3:
                        enemy_two[3][0] += enemy_two[5][1]
                        enemy_two[5][3] -= enemy_two[5][1]
                        print(str(enemy_two[0][0]) + ' Uses water to heal!\n')
                    else:
                        if decision == 1:
                            print(str(enemy_two[0][0]) + ' attacks with a weapon!\n')
                            time.sleep(1)
                            player_hp1 = player_stats[0][0]
                            player_stats = combat_decider(player_stats, enemy_two, decision, 'e', 2)
                            time.sleep(1)
                            player_hp2 = player_stats[0][0]
                            enemy_two[6][0] += player_hp1 - player_hp2
                            print('Your health is now: ' + str(player_stats[0][5]) + '/' + str(player_stats[0][0]) + '\n')
                        if decision == 2:
                            enemy_two[5][3] -= enemy_two[5][0] * 3
                            print(str(enemy_two[0][0]) + ' attacks with poison!\n')
                            player_stats = combat_decider(player_stats, enemy_two, decision, 'e', 2)
                            time.sleep(1)
                        if decision == 4:
                            enemy_two[5][3] -= enemy_two[5][2]
                            print(str(enemy_two[0][0]) + ' attacks with lightning!\n')
                            time.sleep(1)
                            player_hp1 = player_stats[0][0]
                            player_stats = combat_decider(player_stats, enemy_two, decision, 'e', 2)
                            player_hp2 = player_stats[0][0]
                            enemy_two[6][0] += player_hp1 - player_hp2
                            time.sleep(1)
                            print('Your health is now: ' + str(player_stats[0][5]) + '/' + str(player_stats[0][0]) + '\n')

            if enemy_loop == 3:
                if not enemy_three == [] and enemy_three[3][0] > 0:
                    decision = thinker(enemy_three[1])
                    if decision == 3:
                        enemy_three[3][0] += enemy_three[5][1]
                        enemy_three[5][3] -= enemy_three[5][1]
                        print(str(enemy_three[0][0]) + ' Uses water to heal!\n')
                    else:
                        if decision == 1:
                            print(str(enemy_three[0][0]) + ' attacks with a weapon!\n')
                            time.sleep(1)
                            player_hp1 = player_stats[0][0]
                            player_stats = combat_decider(player_stats, enemy_three, decision, 'e', 3)
                            player_hp2 = player_stats[0][0]
                            enemy_three[6][0] += player_hp1 - player_hp2
                            time.sleep(1)
                            print('Your health is now: ' + str(player_stats[0][5]) + '/' + str(player_stats[0][0]) + '\n')
                        if decision == 2:
                            enemy_three[5][3] -= enemy_three[5][0] * 3
                            print(str(enemy_three[0][0]) + ' attacks with poison!\n')
                            player_stats = combat_decider(player_stats, enemy_three, decision, 'e', 3)
                            time.sleep(1)
                        if decision == 4:
                            enemy_three[5][3] -= enemy_three[5][2]
                            print(str(enemy_three[0][0]) + ' attacks with lightning!\n')
                            time.sleep(1)
                            player_hp1 = player_stats[0][0]
                            player_stats = combat_decider(player_stats, enemy_three, decision, 'e', 3)
                            player_hp2 = player_stats[0][0]
                            enemy_three[6][0] += player_hp1 - player_hp2
                            time.sleep(1)
                            print('Your health is now: ' + str(player_stats[0][5]) + '/' + str(player_stats[0][0]) + '\n')
            if enemy_loop == 4:
                if not enemy_four == [] and enemy_four[3][0] > 0:
                    decision = thinker(enemy_four[1])
                    if decision == 3:
                        enemy_four[3][0] += enemy_four[5][1]
                        enemy_four[5][3] -= enemy_four[5][1]
                        print(str(enemy_four[0][0]) + ' Uses water to heal!\n')
                    else:
                        if decision == 1:
                            print(str(enemy_four[0][0]) + ' attacks with a weapon!\n')
                            time.sleep(1)
                            player_hp1 = player_stats[0][0]
                            player_stats = combat_decider(player_stats, enemy_four, decision, 'e', 4)
                            player_hp2 = player_stats[0][0]
                            enemy_four[6][0] += player_hp1 - player_hp2
                            time.sleep(1)
                            print('Your health is now: ' + str(player_stats[0][5]) + '/' + str(player_stats[0][0]) + '\n')
                        if decision == 2:
                            enemy_four[5][3] -= enemy_four[5][0] * 3
                            print(str(enemy_four[0][0]) + ' attacks with poison!\n')
                            player_stats = combat_decider(player_stats, enemy_four, decision, 'e', 4)
                            time.sleep(1)
                        if decision == 4:
                            enemy_four[5][3] -= enemy_four[5][2]
                            print(str(enemy_four[0][0]) + ' attacks with lightning!\n')
                            time.sleep(1)
                            player_hp1 = player_stats[0][0]
                            player_stats = combat_decider(player_stats, enemy_four, decision, 'e', 4)
                            player_hp2 = player_stats[0][0]
                            enemy_four[6][0] += player_hp1 - player_hp2
                            time.sleep(1)
                            print('Your health is now: ' + str(player_stats[0][5]) + '/' + str(player_stats[0][0]) + '\n')
                            time.sleep(1)
        poison_counter1 = 0
        poison_counter2 = 0
        poison_counter3 = 0
        poison_counter4 = 0
        for poison_loop in range(1, 6):
            if poison_loop == 1:
                poison_counter = 0
                for a in player_stats[2]:
                    if a == 'poison':
                        player_stats[0][0] -= 1
                        poison_counter += 1
                    if a == 1:
                        enemy_one[6][0] += 1
                    if a == 2: 
                        enemy_two[6][0] += 1
                    if a == 3:
                        enemy_three[6][0] += 1
                    if a == 4:
                        enemy_four[6][0] += 1
            if poison_loop == 2:
                for a in enemy_one[7]:
                    if a == 'poison': 
                        enemy_one[3][0] -= 1
                        poison_counter1 += 1
            if poison_loop == 3 and not enemy_two == []:
                for a in enemy_two[7]:
                    if a == 'poison': 
                        enemy_two[3][0] -= 1
                        poison_counter2 += 1
            if poison_loop == 4 and not enemy_three == []:
                for a in enemy_three[7]:
                    if a == 'poison': 
                        enemy_three[3][0] -= 1
                        poison_counter3 += 1
            if poison_loop == 5 and not enemy_four == []:
                for a in enemy_four[7]:
                    if a == 'poison': 
                        enemy_four[3][0] -= 1
                        poison_counter4 += 1
        if poison_counter > 0:
            print(str(poison_counter) + ' poison damage was done to you\n')
            time.sleep(2)
            print('Your health is now: ' + str(player_stats[0][5]) + '/' + str(player_stats[0][0]) + '\n')
            time.sleep(2)
        if poison_counter1 > 0:
            print(str(poison_counter1) + ' poison damage was done to ' + str(enemy_one[0][0]) + '\n')
            time.sleep(2)
        if poison_counter2 > 0:
            print(str(poison_counter2) + ' poison damage was done to ' + str(enemy_two[0][0]) + '\n')
            time.sleep(2)
        if poison_counter3 > 0:
            print(str(poison_counter3) + ' poison damage was done to ' + str(enemy_three[0][0]) + '\n')
            time.sleep(2)
        if poison_counter4 > 0:
            print(str(poison_counter4) + ' poison damage was done to ' + str(enemy_four[0][0]) + '\n')
            time.sleep(2)

        #mana consquences
        if player_stats[1][4] < 0:
            player_stats[0][0] += player_stats[1][4]
            print('You take ' + str(int(player_stats[1][4] * -1)) + ' damage from overused mana\n')
            time.sleep(2)
        if enemy_one[5][3] < 0:
            enemy_one[3][0] += enemy_one[5][3]
            print(str(enemy_one[0][0]) + ' takes ' + str(int(enemy_one[5][3] * -1)) + ' damage from overused mana\n')
            time.sleep(2)
        if not enemy_two == []:
            if enemy_two[5][3] < 0:
                enemy_two[3][0] += enemy_two[5][3]
                print(str(enemy_two[0][0]) + ' takes ' + str(int(enemy_two[5][3] * -1)) + ' damage from overused mana\n')
                time.sleep(2)
        if not enemy_three == []:
            if enemy_three[5][3] < 0:
                enemy_three[3][0] += enemy_three[5][3]
                print(str(enemy_three[0][0]) + ' takes ' + str(int(enemy_three[5][3] * -1)) + ' damage from overused mana\n')
                time.sleep(2)
        if not enemy_four == []:
            if enemy_four[5][3] < 0:
                enemy_four[3][0] += enemy_four[5][3]
                print(str(enemy_four[0][0]) + ' takes ' + str(int(enemy_four[5][3] * -1)) + ' damage from overused mana\n')
                time.sleep(2)

        #status update to player
        if enemy_one[3][0] < 1:
            print(str(enemy_one[0][0]) + ' is dead\n')
            time.sleep(2)
        else:
            enemy_one[3][0] += enemy_one[3][4]
            enemy_one[5][3] += enemy_one[5][4]
            enemy_one[6][2] += 1
            enemy_lister(enemy_one)
        time.sleep(2)
        if not enemy_two == []:
            if enemy_two[3][0] < 1:
                print(str(enemy_two[0][0]) + ' is dead\n')
            else:
                enemy_two[3][0] += enemy_two[3][4]
                enemy_two[5][3] += enemy_two[5][4]
                enemy_two[6][2] += 1
                enemy_lister(enemy_two)
            time.sleep(2)
        if not enemy_three == []:
            if enemy_three[3][0] < 1:
                print(str(enemy_three[0][0]) + ' is dead\n')
            else:
                enemy_three[3][0] += enemy_three[3][4]
                enemy_three[5][3] += enemy_three[5][4]
                enemy_three[6][2] += 1
                enemy_lister(enemy_three)
            time.sleep(2)
        if not enemy_four == []:
            if enemy_four[3][0] < 1:
                print(str(enemy_four[0][0]) + ' is dead\n')
            else:
                enemy_four[3][0] += enemy_four[3][4]
                enemy_four[5][3] += enemy_four[5][4]
                enemy_four[6][2] += 1
                enemy_lister(enemy_four)
            time.sleep(2)
        

with open('data.txt', 'a') as data_file:
    data_file.write('end of game \n')
            



  