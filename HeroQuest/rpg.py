import random


class Character:
    def __init__(self, name, health, stats, power, gil, inv):
        self.name = name
        self.health = health
        self.stats = stats
        self.power = power + (stats["Strength"] * .5)
        self.gil = gil
        self.inv = inv

    def attack(self, power, enemy):
        if enemy == medic:
            recover_health = random.random()
            if recover_health <= .20:
                enemy.health -= power - 2
                print("The Medic injects herself with a syringe, which is definitely not usually a good idea, and recovered 2 health!")
            else:
                enemy.health -= power
        elif enemy == shadow:
            null_damage = random.random()
            if null_damage <= .10:
                enemy.health -= power
                print(f"{shadow.name} took no damage from that attack!")
            else:
                enemy.health -= power
        else:    
            enemy.health -= power
    
    def alive(self, health):
        if self.health <= 0:
            return True
    
    def print_status(self, name, health, power):
        print(f"{name} has {health} health and {power} power.")

class Hero(Character):
    def attack(self, power, enemy):
        double_damage = random.random()

        if double_damage <= .20:
            self.power = power * 2
            enemy.health -= self.power           
            print("CRITICAL HIT!")
        if double_damage > .20:
            enemy.health -= power

        if enemy == medic:
            recover_health = random.random()
            if recover_health <= .20:
                enemy.health -= power - 2
                print("The Medic injects herself with a syringe, which is definitely not usually a good idea, and recovered 2 health!")

        if enemy == shadow:
            null_damage = random.random()
            if null_damage <= .10:
                enemy.health -= power
                print(f"{shadow.name} took no damage from that attack!")
            else:
                enemy.health -= power

class Berserker(Character):
    def attack(self, power, enemy):
        if berserker.health < 15:
            print("Sweet lord the Berserker has gone nuts and is doing double damage!")
            enemy.health -= power * 2
            self.power = power * 2
        else:
            enemy.health -= power

options = ["1","2","3","4","5"]
decicion = input("")

            
Humans = {"Strength" : 7, "Agility" : 7, "Constitution" : 7}
Goblins = {"Strength" : 3, "Agility" : 7, "Constitution": 5 }
Demons = {"Strength" : 5, "Agility" : 5, "Constitution" : 0}
Centaurs = {"Strength" : 8, "Agility" : 8, "Constitution" : 5}
Undead = {"Strength" : 2, "Agility" : 5, "Constitution" : 0}
Amorphous = {"Strength" : 5, "Agility" : 10, "Constitution" : 5}
Ogre = {"Strength" : 10, "Agility" : 3, "Constitution" : 8}

hero = Hero("Maximo", 100, Humans, 5, 9999, [])
goblin = Character("Goblin", 20, Goblins, 2, 5,[])
medic = Character("Medic", 25, Humans, 3, 20, [])
zombie = Character("Zombie", 10, Undead, 1, 40, [])
berserker = Berserker("Berserker", 30, Humans, 10,  70, [])
shadow = Character("Ryu", 1, Humans, 10, 125, [])

def main():
    print("Welcome to the world of...Frank. Yeah, just Frank. He's some guy. I guess he owns the world or something? Wild.\n")
    print("Anyway. Your name is Maximo. I don't care what it was before, you're 'Maximo' now. Hello, Maximo!\n")
    print("Oh no! A goblin is minding his own business somewhere. ASSAULT IT!!!\n")
            
    def goblin_battle():    
        while hero.health > 0 and goblin.health > 0:
            goblin.print_status(goblin.name, goblin.health, goblin.power)
            hero.print_status(hero.name, hero.health, hero.power)
            print("")
            print("Type the number of the action you wish to take.")
            print("1. Attack")
            print("2. Wait")
            print("3. Flee")
            print(">")
            user_input = input("")
        
            if user_input == "1":
                hero.attack(hero.power, goblin)
                print(f"You've dealt {hero.power} damage to the {goblin.name}.")
                if goblin.alive(goblin.health):
                    print("The goblin has been murdered. His only crime was being a goblin.")
            
            elif user_input == "2":
                print(f"You stare at the goblin. Menacingly. You even throw up a gang sign or two. He freaks the fudge out and attacks you out of sheer terror.")
            
            elif user_input == "3":
                print(f"Seriously? You're just going to run away? Coward. COWAAAAAAAAAAAAAAAAARD!!!")
                break
            
            else:
                print("Hey bud. That wasn't one of the options you were given. Learn the rules!")

            if goblin.health > 0:
                goblin.attack(goblin.power, hero)
                print(f"The goblin does {goblin.power} damage to you!")

    goblin_battle()

    print("-" * 10)
    print("Phew that was a close one. Great job viciously murdering that innocent goblin. He might have a family around here somewhere so let's go tie up loose ends. OH SWEET LORD THERE'S A BERSERKER OVER THERE!")
    print("")
    print("Like...he's not really 'Berserking' right now, but...you know...what if he does? Like yeah, he's gardening *right now*, but when he's finished gardening, then what? You know what I mean? Better kill him to make sure, right? Yeah...yeah...")
    print("")

    def berserker_battle():
        while hero.health > 0 and berserker.health > 0:
            berserker.print_status(berserker.name, berserker.health, berserker.power)
            hero.print_status(hero.name, hero.health, hero.power)
            print("")
            print("Type the number of the action you wish to take.")
            print("1. Attack")
            print("2. Wait")
            print("3. Flee")
            print(">")
            user_input = input("")

            if user_input == "1":
                hero.attack(hero.power, berserker)
                print(f"You've dealt {hero.power} damage to the {berserker.name}.")
                if berserker.alive(berserker.health):
                    print("The berserker has been slain!")
            elif user_input == "2":
                print("You insult the Berserker's mother and start stomping on his flowers while, for some reason, throwing up gang signs. Unprovoked, the Berserker attacks!")

            elif user_input == "3":
                print("Oh, oh, what?! You murder a goblin in cold blood without a problem but now all of a sudden you have a problem -DEFENDING YOURSELF- against a Berserker? Seriously? What are you, racist against goblins? I don't have time for bigots. Get out of here.")
                break
            
            else:
                print("Oh boy. That's not one of the options you were given and yet you did it anyway. So uh...don't do that.")

            if berserker.health > 0:
                berserker.attack(berserker.power, hero)
                print(f"The {berserker.name} deals {berserker.power} damage to you. ")

    berserker_battle()
    
    print("-" * 10)
    print("Oh man that got really scary in the end, huh? Like you could have died, man. I wonder what his problem was, attacking you like that. Good thing you defended yourself and did nothing wrong!\n")
    print("Hey, look. A medic.\n")
    print("...\n")
    print("...I -SAID- : \"HEY, LOOK. A MEDIC\"\n.")

    def medic_battle():
        while hero.health > 0 and medic.health > 0:
            medic.print_status(medic.name, medic.health, medic.power)
            hero.print_status(hero.name, hero.health, hero.power)
            print("")
            print("Type the number of the action you wish to take.")
            print("1. Attack")
            print("2. Wait")
            print("3. Flee")
            print(">")
            user_input = input("")

            if user_input == "1":
                hero.attack(hero.power, medic)
                print(f"You've dealt {hero.power} damage to the {medic.name}.")
                if medic.alive(medic.health):
                    print("Oh wow you killed her.")
            elif user_input == "2":
                print("Your eyes roll to the back of your head, you start foaming at the mouth and making demonic screeches while walking like a crab and snapping your imaginary claws. The Medic tries to exorcise you, horrified, which is interesting because medics don't typically do exorcism.")

            elif user_input == "3":
                print("You try to flee like a small, worthless child but the medic tranquilizes you with...a tranquilizer...gun? What time period is this game set in? Let's say it was a dart. Anyway, she hits you with it and then you go to jail or something. Lawyer up, my man.")
                break
            
            else:
                print("Nah don't do that. Press 1, 2, or 3.")

            if medic.health > 0:
                medic.attack(medic.power, hero)
                print(f"The {medic.name} deals {medic.power} damage to you.")

    medic_battle()
    
    print("-" *10)
    print("Oh man! What did you do?! No one told you to do that! She's dead, bro! You're a monster! Oh sweet she has some healing potions on her.\n")
    print("You've stolen...well, can it really be called stealing if it's a corpse? Legally, I think the answer is no. Anywho, 3 healing potions acquired!")
    
    def town():#The currently broken structure of which to access the town interface
        print("You can see familliar structures in the distance and start off toward them.")
        input("Press \'Return'")
        exploration = 0

        while exploration < 99:
            print("You\'re at Rie.")
            print("1. Meander for a while.")
            print("2. Visit Bender\'s Tavern.")
            print("3. Visit The Jester\'s Emporium.")
            print("4. Visit inn.")
            print("5. leave this place")
            print("\n")
            print("Now, what would you like to do?")
            decicion = input("")
            
            if decicion == options[0]:#Option to speak with villagers| hopefully also, events to get items and gil
                input("You arrive at the Rie Square! There is a boy on a soap-box that\'s grabbed your attention. \n1. Interact\n Return. Continue strolling\n ")
                if decicion == "1":
                    exploration +=1
                    print("You argue passionately until a crowd forms. Then knock over the box and in the confusion \'borrowed\' some loose change.") # {name.gil} += 21 print("you now have %s gil!")
                else:
                    exploration +=1
                    return town()#Should return to town
            
            if decicion == "2":#Second option to interact with townspeople| maybe also, play Blackjack cardgame for gil??
                print("You arrive at the tavern of which sign depicts some strange grid-mouthed wooden man only having a barrel-like torso with ribbed appendages, \nonly 3 digets on each hand, hooves and some manner of sprout on his head..\n")
                print("Inside you spot a table of people playing a card game while one suddenly jumps up and exclaims \"BLACKJACK!! \nIll clad individuals beckon passersby in a seedy corner and at the far end the Barkeep. ")
                input("You shrug and head inside. \n1.Approach Barkeep \nReturn. Sit and play cards\n ")
                if decicion == "1":
                    exploration +=1
                    print("You have a seat and chat with the Barkeep a while.")
                else:
                    exploration +=1
                    town()#Should return to town
            
            if decicion == "3":#Shop choice
                print("You wander inside where you see a varied pathora of items adorning the shelves when burly man adorned in a Jester\'s costume with a strange momochrome palette calls you to the counter.")
                print("He looks you up and down and proceeds to flip the open/closed sign and draws the blinds. He then states \"I may be a fool but, business is business.\" as he pulls out a rather large chest from under the counter")
                input("Now, what're ya buyin?\n 1. Potion\n Return. Leave shop\n ")
                if decicion == "1":#and gil > item price
                    print("Is that all, Stanger?\n") #item += inv| print("obtained {name.item} you now have %s of them") need dictionary of items to add
                elif decicion == "1": #and gil < item price
                    print("Not enough gil, Stranger!\n") # stops item from being perchased| allows more item selection
                else:
                    print("Heh, heh, heh... Thank you!!\n")
                    exploration +=1
                    town()#Should return to town
            
            if decicion == "4":
                exploration +=1
                print("Closed for revnovations\n")#Could be used for save feature| try: f = open("sav.txt") print(f.(write()) finally: f.close()
            
            if decicion == "5":
                exploration += 99
                print("You decide to head back out.")
            
    town()#Calls town to open up and be interacted with
                
main()