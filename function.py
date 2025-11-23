

# ================================================
def display_maps():
  import matplotlib.pyplot as plt
  import matplotlib.image as mpimg

  # --- 1️⃣ Charger une image locale ---
  # Remplace 'mon_image.png' par le chemin de ton image
  img = mpimg.imread("mon_image.png")

  # --- 2️⃣ Créer la figure et définir les limites des axes ---
  fig, ax = plt.subplots()
  ax.set_xlim(0, 4)
  ax.set_ylim(0, 6)

  # --- 3️⃣ Afficher une grille pour mieux visualiser ---
  ax.grid(True)

  # --- 4️⃣ Afficher l'image dans le repère ---
  # extent = [x_min, x_max, y_min, y_max]
  # Cela positionne et redimensionne ton image selon le système de coordonnées
  ax.imshow(img, extent=[1, 3, 2, 4])  # exemple : l’image occupe de x=1→3 et y=2→4

  # --- 5️⃣ Afficher le résultat ---
  plt.show()
display_maps()
# ================================================

### FONCTION SEARCH ATTACK AND FIGHT ----- KING JULIAAAAAAN , L'ÉLU DES LÉMURIENS ---

#fonction fonctionnelle - fantastique
from random import randint
print(" A fight has been")
def select_attack(Player):

  #will serve later for the tuto, deals with the case where the Inventory is empty
  if Player["Inventory"]["Objects"]["sign"]+Player["Inventory"]["Objects"]["decath_chair"]+ Player["Inventory"]["Objects"]["empty_water_bottle"]+Player["Inventory"]["Objects"]["fan"]+  Player["Inventory"]["Potions"]["water"]+Player["Inventory"]["Potions"]["beer"]+Player["Inventory"]["Potions"]["sweet_treat"]==0:
    print("You do not have found any items yet. Select a basic attack : Push or Love_dance ")
    choice = input().lower()
    while choice not in ["push","love_dance"]:
        choice = input("You miss typed your attack. Select a basic attack : push or love_dance  ")
    return ("Attacks",choice) #type and the choice

  # Ask what action the player wants to do
  else:
    choice = input("Do you want to use objects (defence or attack), potions or basic attacks?  ").lower()
    while choice not in ["objects","potions","basic attacks"]:
      choice = input("You miss typed your answer. Do you want to use objects , potions or basic attacks?  ").lower()


    if choice == "objects":
      print("Choose one of the objects of the following list", Player["Inventory"]["Objects"])
      selected_item = input().lower()

      #deals with typing errors or invalid answers
      while selected_item not in ["sign","decath_chair","fan","empty_water_bottle"] or Player["Inventory"]["Objects"][selected_item]== 0 :
        selected_item = input("please select a valid object  ").lower()

      #valid answer
      if Player["Inventory"]["Objects"][selected_item] > 0:
        Player["Inventory"]["Objects"][selected_item] -= 1
        return ("Objects",selected_item)


    elif choice == "potions":
      print("Choose one of the objects of the following list"," ",Player["Inventory"]["Potions"])
      selected_item = input()

      #deals with typing errors or invalid answers
      while selected_item not in ["water","beer","sweet_treat"] or Player["Inventory"]["Potions"][selected_item]==0 :
        selected_item = input("please select a valid item  ")


      if Player["Inventory"]["Potions"][selected_item] > 0:
        #drink water --> empty bottle as an attack object
        if selected_item == "water":
          print(Player["Inventory"]["Potions"][selected_item])
          Player["Inventory"]["Objects"]["empty_water_bottle"] += 1
        Player["Inventory"]["Potions"][selected_item] -= 1
        return ("Potions",selected_item)

    elif choice == "basic attacks":
      choice = input("Select a basic attack : push or love_dance ")
      #deals with typing errors or invalid answers
      while choice not in ["push","love_dance"]:
        choice = input("You miss typed your attack. Select a basic attack : push or love_dance  ")
      return ("Attacks",choice)



#self explanatory mais du coup here it is, la fonction de combat quoi
def fight(Player,enemy_type):

  #innitialise les stats de l'opponent en fonction du type d'adversaire
  if enemy_type == "Drunk_crowd":
    enemy_name = Drunk_crowd["name"][randint(0,len(Drunk_crowd["name"])-1)]
    enemy_life = Drunk_crowd['life']
    enemy_attacks = Drunk_crowd['Attacks']
    enemy_drop = ["casheless","beer"]

  else:
    enemy_name = Security["name"]
    enemy_life = Security['life']
    enemy_attacks = Security['Attacks']
    # enemy_drop = =================

  #print(enemy_name,enemy_life,enemy_attacks)

  while  Player["life"] > 0 and enemy_life > 0 :  #the fight continues as long as one of the two opponent is alive

    choice_player = select_attack(Player)
    #print(choice_player)


    # PARTIE DU COMBAT DU JOUEUR - fonctionnelle avec les prints et tout
    if choice_player[0]== "Potions":
      Player["life"] += Objects[choice_player[1]] #rajoute l'effet de la potion à la vie du joueur
      print("You used " + choice_player[1])
      print("You regain " + str(Objects[choice_player[1]])+ " points of life")
      print(" >> You have now  " + str(Player["life"])+ " points of life")
      print("In your inventory there is  " + str(Player["Inventory"]["Potions"][choice_player[1]])+ " "+ choice_player[1]+ " remaining")


    elif choice_player[0]== "Objects":
      if choice_player[1]== "sign":
        enemy_life -= Objects[choice_player[1]] #fait passer un tour à l'ennemi + lui cause 2 de degats
        print("You used " + choice_player[1] + " defense")
        print(enemy_name + " lost " + str(Objects[choice_player[1]]) + " points of life")
        if enemy_life > 0 :
          print(" >>" + enemy_name + " has now " + str(enemy_life) + " points of life") # chunk of code bcz I think it's silly to display negative hitpoints

        else :
          print(" >>" + enemy_name + " has now 0 points of life ")
        print(enemy_name + " wont be able to attack next turn")

      else :
        enemy_life -= Objects[choice_player[1]] # inflige des déagats d'attaques à l'ennemi
        print("You used " + choice_player[1] + " as an attack object")
        print(str(enemy_name) + " lost " + str(Objects[choice_player[1]]) + " points of life")
        if enemy_life > 0 :
          print(">> " +enemy_name + " has now " + str(enemy_life) + " points of life")

        else :
          print(">> " + enemy_name + " has now 0 points of life ")
        print("In your inventory there is  " + str(Player["Inventory"]["Objects"][choice_player[1]])+ " "+ choice_player[1]+ " remaining")



    elif choice_player[0] == "Attacks":
      chances_of_hit = randint(0,100)
      if chances_of_hit < Player["Attacks"][choice_player[1]][1]:
        enemy_life -= Player["Attacks"][choice_player[1]][0]
        print("You used " + choice_player[1] + " attack")
        print(enemy_name + " lost " + str(Player["Attacks"][choice_player[1]][0]) + " points of life")
        if enemy_life > 0 :
          print(">> " + enemy_name + " has now " + str(enemy_life) + " points of life") # chunk of code bcz I think it's silly to display negative hitpoints

        else :
          print(">> " + enemy_name + " has now 0 points of life ")
      else :
        print("you missed your shot")
        print(">> " + enemy_name + " has still " + str(enemy_life) + " points of life")


    #PARTIE DU COMBAT DE L'OPPOSANT

    enemy_choice = list(enemy_attacks.keys())[randint(0,1)]
    if choice_player == ("Objects","sign"):
      print("The sign skips the " + enemy_name + "'s turn")

    else :
      chances_of_hit = randint(0,100)
      if chances_of_hit < enemy_attacks[enemy_choice][1] and enemy_life > 0:
        Player["life"] -= enemy_attacks[enemy_choice][0] #attack dammages
        print(enemy_name + " successfully used "+ enemy_choice + " on you")
        print("You lost " + str( enemy_attacks[enemy_choice][0])+ " points of life")
        print(">> You have " + str(Player["life"])+ " points of life remaining")

      elif enemy_life <= 0 :
        print(enemy_name + " is exhausted and leave you alone. You are victorious")
        return

      else:
        print(enemy_name + " tried to use " + enemy_choice + " on you but miserably failed :( ")

    if Player["life"] == 0 :
      print("shit you're dead")
      return


enemy_type = "Drunk_crowd" #given by the map --¨> to be modified

print(fight(Player,enemy_type))



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


def move(current_position):
  while Player["life"] > 0 or current_position != "B6" or quit == False:
    # ---------------------------------------------
    # récupérer le discours associés
    print(Map[current_position]["direction_print"])

    # ---------------------------------------------
    # savoir si ma room contient un combat
    if Map[current_position]["fight"] == True:
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
      buy_drink(Player,position)
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
move(position)

# ================================================


