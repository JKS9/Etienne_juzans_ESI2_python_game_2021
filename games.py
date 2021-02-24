## import packages
import random

## variables AND players
    ## Players 
joueur_1 = {
    "name": None,
    "life": 50,
    "attack": {
        "mins": 5,
        "maxs": 10
    },
    "potion": {
        "nb": 5,
        "mins": 15,
        "maxs": 50
    }
}

enemy = {
    "name": "Balkany",
    "life": 50,
    "attack": {
        "mins": 5,
        "maxs": 15
    }
}
    ## variables
print("")
print("STARTED GAME !")
print("------------------------------------------")
print(" ")

name = input("Choose your Pseudo : ")
joueur_1["name"] = name
i = 0
print("-----------------")
print(" ")

## Function create space in console / terminal
def createSpaceInConsole(number):
    if number == 1:
        print(" ")
        print(" ")
    else: 
        print(" ")

## Function use potion for player 1
def usePotion(mins, maxs):
    if joueur_1["potion"]["nb"] > 0:
        moreLife = random.randint(mins,maxs)

        print("     "+joueur_1["name"]+" à gagnez "+ str(moreLife)+ " HP en plus")

        joueur_1["potion"]["nb"] -= 1
        joueur_1["life"] += moreLife
    else:
        print("     VOUS N'AVEZ PLUS DE POTION DE SOIN")

## Function attack player 1 or enemy
def attack(userAttack, userDefense, whoAttack):
    attack = random.randint(userAttack["attack"]["mins"],userAttack["attack"]["maxs"])

    if whoAttack == "me":
        print("     Votre attaque à fais "+ str(attack)+ " DMG à votre enemy")
        enemy["life"] = enemy["life"] - attack
        print(enemy["life"])

    else:
        print("     Son attaque vous à fais "+ str(attack)+ " DMG")
        joueur_1["life"] = joueur_1["life"] - attack
        print(joueur_1["life"])

## Fontion started script "Games"
while i <= 345:
    actionByLoop = None

    ## If enenmy win
    if joueur_1["life"] <= 0:
        print("Fin de la partie")
        print(enemy["name"] +" win la partie")
        break
    ## If player 1 win
    if enemy["life"] <= 0:
        print("Fin de la partie")
        print(name +" win la partie")
        break
    
    ## Displays player statistics
    createSpaceInConsole(2)
    print("Vos HP : "+ str(joueur_1["life"])+ " HP")
    print("enemy HP : "+ str(enemy["life"]))
    createSpaceInConsole(1)

    ## If the number is not even, it is up to player 1 to play
    if i % 2 == 0:
        print("- "+joueur_1["name"]+ " à vous de jouez")
        ## Asks for the future action of player 1
        actionByLoop = int(input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?"))

        if actionByLoop == 1:
            print("     "+name+" attaque "+ enemy["name"])
            ## Attack enemy player
            attack(joueur_1, enemy, "me")
        else:
            print("     "+name+" utilise une potion de vie")
            ## Use a healing potion
            potion = usePotion(joueur_1["potion"]["mins"],joueur_1["potion"]["maxs"])
            print("     "+name+ " à "+ str(joueur_1["life"]) +" HP")
    ## If the number is even, it's the enemy's turn to play
    else:
        print("- "+enemy["name"]+ " est en train de jouer")
        print("     "+enemy["name"]+" attaque "+ name)
        ## Attack player 1
        attack(enemy, joueur_1, "enemy")
    i += 1