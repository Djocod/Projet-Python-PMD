from data_game import *
from random import randint 
# ================================================
# ================================================

# Fonction de déplacement.
def buy_drink(Player,current_position):
  print(Player["Inventory"]["potion"]["beer"],Player["Inventory"]["cashless"] )
  print(Player["Inventory"]["potion"]["water"],Player["Inventory"]["cup"] )
  while Player["life"] > 0 and current_position == "A3":
    choiceBuyDrink = input("What can I get you ? 'beer' = 1cashless, 'water' = 3cup, nope")
    if choiceBuyDrink == "beer" and Player["Inventory"]["cashless"] >= 1:
      Player["Inventory"]["cashless"]-=1
      Player["Inventory"]["potion"]["beer"]+=1
      print(Player["Inventory"]["potion"]["beer"],Player["Inventory"]["cashless"] )
    elif choiceBuyDrink == "water" and Player["Inventory"]["cup"] == 3:
      Player["Inventory"]["cup"]-=3
      Player["Inventory"]["potion"]["water"]+=1
      print(Player["Inventory"]["potion"]["water"],Player["Inventory"]["cup"] )
    else:
      move(current_position)

def objects_in_the_room(current_position):
  if Map[current_position]["object"][1] == "fan":
    Player["Inventory"]["objects"]["fan"]+=1
    Map[current_position]["object"][1] = False
  elif Map[current_position]["object"][1] == "decat_chair":
    Player["Inventory"]["objects"]["decat_chair"]+=1
    Map[current_position]["object"][1] = False
  elif Map[current_position]["object"][1] == "sign":
    Player["Inventory"]["objects"]["sign"]+=1
    Map[current_position]["object"][1] = False

  if Map[current_position]["object"][2] == "water":
    Player["Inventory"]["potion"]["water"]+=1
    Map[current_position]["object"][2] = False
  elif Map[current_position]["object"][2] == "beer":
    Player["Inventory"]["potion"]["beer"]+=1
    Map[current_position]["object"][2] = False
  elif Map[current_position]["object"][2] == "super_beer":
    Player["Inventory"]["potion"]["super_beer"]+=1
    Map[current_position]["object"][2] = False

  if Map[current_position]["object"][3] == "cashless":
    Player["Inventory"]["cashless"]+=1
    Map[current_position]["object"][3] = False
  elif Map[current_position]["object"][3] == "cup":
    Player["Inventory"]["cup"]+=1
    Map[current_position]["object"][3] = False


# ================================================

def move(current_position):
  while Player["life"] > 0 or current_position != "B6" or quit == False:
    # ---------------------------------------------
    # récupérer le discours associés
    print(Map[current_position]["direction_print"])

    # ---------------------------------------------
    # savoir si ma room contient un combat
    # if Map[current_position]["fight"] == True:
      # fight_enemy(player,enemy_type)

    # ---------------------------------------------
    # récupérer les objets associés à ma room
    if Map[current_position]["object"][0] == True:
      objects_in_the_room(current_position)

    if current_position == "B3" and Player["Inventory"]["cashless"] > 0 or current_position == "B3" and  Player["Inventory"]["cup"] >= 3 :
      choice = input("Qu'est ce que je te sers troubadour ?[cashless, cup] ")
      if choice == "cashless":
        Player["Inventory"]["cashless"]-=1
        Player["Inventory"]["potion"]["beer"]+=1
      elif choice == "cup":
        Player["Inventory"]["cup"]-=3
        Player["Inventory"]["potion"]["water"]+=1


    if current_position == "B3"and Map[current_position]["object"][0] == True or current_position == "D5" and Map[current_position]["object"][0] == True:
      print(f"Would you like a {Map[current_position]["object"][2]}?")
      choice = input("yes or no ").lower()
      if choice == "yes" :
        Player["Inventory"]["potion"]["sweet_treat"]+=1
        Map[current_position]["object"][2] = False
        Map[current_position]["object"][0] = False


    # ---------------------------------------------
    # récupérer le choix de direction = By Julie
    choice = input("quelle direction" + str(Map[current_position]["print_possible_answers"]))
    # ---------------------------------------------
    # Quand tu te trouves au bar tu peux acheter de quoi te soigner
    if current_position == "A3" and Player["Inventory"]["cashless"] > 0 or current_position == "A3" and  Player["Inventory"]["cup"] >= 3:
      buy_drink(Player,current_position)
    # ---------------------------------------------
    # Demande pour se soigner.
    if choice == "to heal":
      choicePotion = input("prend une potion" + str(Player["Inventory"]["potion"]))
      if choicePotion == "water" and Player["Inventory"]["potion"]["water"] > 0:
        Player["life"] += Objects["water"][1]
        Player["Inventory"]["potion"]["water"]-=1
      elif choicePotion == "beer" and Player["Inventory"]["potion"]["beer"] > 0:
        Player["life"] += Objects["beer"][1]
        Player["Inventory"]["potion"]["beer"]-=1
      elif choicePotion == "super_beer" and Player["Inventory"]["potion"]["super_beer"] > 0:
        Player["life"] += Objects["super_beer"][1]
        Player["Inventory"]["potion"]["super_beer"]-=1
      elif choicePotion == "sweet_treat" and Player["Inventory"]["potion"]["sweet_treat"] > 0:
        Player["life"] += Objects["sweet_treat"][1]
        Player["Inventory"]["potion"]["sweet_treat"]-=1
    else:
      index = Map[current_position]["print_possible_answers"].index(choice)
      current_position = Map[current_position]["possible_box_directions"][index]



