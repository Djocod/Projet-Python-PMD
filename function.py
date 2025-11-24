from data_game import Player, Map, Objects, Drunk_crowd, Security, current_position
from random import randint
# ================================================

def stage_display(nb):

    stages= [
    f"""6
    -----------------------------------
    |Exchange : Cashless : {Player["Inventory"]["cashless"]} / Cup : {Player["Inventory"]["cup"]} |
    """,
    f""" 5
    -------------------------
    name : {Player["name"]}
    Life : {Player["life"]}
    -------------------------
    """,
    f""" 4
    Objects:          | Potions :
    -----------------------------------
    |Sign         : {Player["Inventory"]["Objects"]["sign"]} |Water       : {Player["Inventory"]["Potions"]["water"]} |
    |Decat_chair  : {Player["Inventory"]["Objects"]["decath_chair"]} |Beer        : {Player["Inventory"]["Potions"]["beer"]} |
    |Fan          : {Player["Inventory"]["Objects"]["fan"]} |sweet treat : {Player["Inventory"]["Potions"]["sweet_treat"]} |
    -----------------------------------
    |Exchange : Cashless : {Player["Inventory"]["cashless"]} / Cup : {Player["Inventory"]["cup"]} |
    Position = {Map[current_position]["room_name"]}
    """,
    f"""3
    =============================================
    Texte: {Map[current_position]["direction_print"]}
    """,
    f""" 2
    Crowd Attacks | Life : {Drunk_crowd["life"]}
    sweaty_contact  : {Drunk_crowd["Attacks"]["sweaty_contact"][0]} dommage  | Chance of Hit:{Drunk_crowd["Attacks"]["sweaty_contact"][1]}%
    step_on_the_feet: {Drunk_crowd["Attacks"]["step_on_the_feet"][0]} dommage  | Chance of Hit :{Drunk_crowd["Attacks"]["step_on_the_feet"][1]}%
    """,
    f""" 1
   {Security["name" ]} | Life : {Security["life"]}
    death_stare  : {Security["Attacks"]["death_stare"][0]} dommage  | Chance of Hit:{Security["Attacks"]["death_stare"][1]}%
    body_search  : Chance of Hit :{Security["Attacks"]["body_search"][1]}%
    teargas      : {Security["Attacks"]["teargas"][0]} dommage  | Chance of Hit :{Security["Attacks"]["teargas"][1]}%
    """
    ]

    print(stages[6 - nb])

# ================================================
# Functions for the fights

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


def fight(Player,enemy_type):
    
  #innitialise les stats de l'opponent en fonction du type d'adversaire
  if enemy_type == "Drunk_crowd":
    enemy_name = Drunk_crowd["name"][randint(0,len(Drunk_crowd["name"])-1)]
    enemy_life = Drunk_crowd['life']
    enemy_attacks = Drunk_crowd['Attacks']

  else:
    enemy_name = Security["name"]
    enemy_life = Security['life']
    enemy_attacks = Security['Attacks']

  #print(enemy_name,enemy_life,enemy_attacks)
  print("A confrontation has been declared between you and "+ str(enemy_name )
        + "... You'll have to fight to reach your ultimate goal : enjoy the music on the main stage."+ "\n" 
        + "Your opponent has " + str(enemy_life) + " points of life" + "\n"
        + " Use your attacks, items and potions wisely... Some items and potions can only be found once in this wonderful adventure. They can only be used once. ")
  
  if enemy_type == "Security":
    print("You've encounter your last confrontation. Fight well lill troubadour")

  while  Player["life"] > 0 and enemy_life > 0 :

    choice_player = select_attack(Player) #ie , choice_player("Attacks","push")
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
          print(enemy_name + " has now " + str(enemy_life) + " points of life")
        else : 
          print(enemy_name + " has now 0 points of life ")
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
      chances_of_hit = randint(0,100) #emulate a dice throw to see if your attack reached the opponent
      if chances_of_hit < Player["Attacks"][choice_player[1]][1]:
        enemy_life -= Player["Attacks"][choice_player[1]][0]
        print("You used " + choice_player[1] + " attack")
        print(enemy_name + " lost " + str(Player["Attacks"][choice_player[1]][0]) + " points of life")
        if enemy_life > 0 :
          print(">> " + enemy_name + " has now " + str(enemy_life) + " points of life")
        else : 
          print(">> " + enemy_name + " has now 0 points of life ")
      else :
        print("you missed your shot")
        print(">> " + enemy_name + " has still " + str(enemy_life) + " points of life")



    #PARTIE DU COMBAT DE L'OPPOSANT

    #security has 3 attacks
    if enemy_type == "Security":
      enemy_choice = list(enemy_attacks.keys())[randint(0,2)]
    else:
      enemy_choice = list(enemy_attacks.keys())[randint(0,1)] # enemy_choice = string de l'attack
    print(enemy_choice)

    #skip enemy's turn if sign used
    if choice_player == ("Objects","sign"):
      print("The sign skips the " + enemy_name + "'s turn")

    else : 
      chances_of_hit = randint(0,100) # simulate a dice throw to see if the attack succeeds 
      
      if chances_of_hit < enemy_attacks[enemy_choice][1] and enemy_life > 0: 
        print(chances_of_hit)
        if enemy_choice == "body_search":
          if Player["Inventory"]["Potions"]["sweet_treat"] > 0:
            Player["Inventory"]["Potions"]["sweet_treat"] = 0
            print("Breit took all your sweet candies")
          else:
            Player["life"] -= enemy_attacks[enemy_choice][0] #retire 3 pv
            print("Breit hasn't found any sweet substance on you, but he shook you very well so you loose 3 points of life")
            print(">> You have " + str(Player["life"])+ " points of life remaining")
        else : 
          Player["life"] -= enemy_attacks[enemy_choice][0] #attack dammages
          print(enemy_name + " successfully used "+ enemy_choice + " on you")
          print("You lost " + str( enemy_attacks[enemy_choice][0])+ " points of life")
          print(">> You have " + str(Player["life"])+ " points of life remaining")
          
      elif enemy_life <= 0 : 
        print(enemy_name + " is exhausted and leave you alone. You are victorious")
        return Player["life"]
      else:
        print(enemy_name + " tried to use " + enemy_choice + " on you but miserably failed :( ")

    if Player["life"] == 0 :
      print("shit you're dead")    
      return "Quit"

# ================================================
# Function to collect objects in the current room
def objects_in_the_room(current_position):
    # Check if there is a "fan" in the room
    if Map[current_position]["object"][1] == "fan":
        Player["Inventory"]["Objects"]["fan"] += 1
        print("You have find a Fan")
        Map[current_position]["object"][1] = False
    
    # Check if there is a "decat_chair" in the room
    elif Map[current_position]["object"][1] == "decat_chair":
        Player["Inventory"]["Objects"]["decath_chair"] += 1
        print("You have find a decat_chair")
        Map[current_position]["object"][1] = False
    
    # Check if there is a "sign" in the room
    elif Map[current_position]["object"][1] == "sign":
        Player["Inventory"]["Objects"]["sign"] += 1
        print("You have find a sign")
        Map[current_position]["object"][1] = False

    # Check for potions in the room
    if Map[current_position]["object"][2] == "water":
        Player["Inventory"]["Potions"]["water"] += 1
        print("You have find a water")
        Map[current_position]["object"][2] = False
    elif Map[current_position]["object"][2] == "beer":
        Player["Inventory"]["Potions"]["beer"] += 1
        print("You have find a beer")
        Map[current_position]["object"][2] = False

    # Check for other items like "cashless" or "cup"
    if Map[current_position]["object"][3] == "cashless":
        Player["Inventory"]["cashless"] += 1
        print("You have find a cashless")
        Map[current_position]["object"][3] = False
    elif Map[current_position]["object"][3] == "cup":
        Player["Inventory"]["cup"] += 1
        print("You have find a cup")
        Map[current_position]["object"][3] = False

# ================================================
# Function to run the game - more specifically his movements on the maps and the events that follow

def move(current_position):
    
    # While the player is alive, hasn't reached "B6", and hasn't quit
    while Player["life"] > 0 or current_position != "B6" or quit == False:
        # ---------------------------------------------
        # Display the description of the current room
        print(Map[current_position]["direction_print"])
        # ---------------------------------------------
        if Map[current_position]["fight"][0] == True:
           Player["life"] = fight(Player,str(Map[current_position]["fight"][1]))
        # ---------------------------------------------
        # Check if the room contains objects and collect them
        if Map[current_position]["object"][0] == True:
            objects_in_the_room(current_position)
        # ---------------------------------------------
        #Display stat:
        stage_display(4)
        # ---------------------------------------------
        # If the player is at "A3" and has enough resources, offer drinks
        while Player["life"] > 0 and current_position == "A3":
        # Ask the player what they want to buy      
            choiceBuyDrink = input("What can I get you, troubadour? Exchange your 'cashless'for a beer or your 'cup' for a water drink or type 'no' to move on" + "\n").lower()
            while choiceBuyDrink not in ["cashless", "cup","no"]:
                choiceBuyDrink = input("You made a typo. What can I get you, troubadour? Exchange your 'cashless'for a beer or your 'cup' for a water drink or type 'no' to move on" + "\n").lower()
            
            # If the player chooses "beer" and has enough cashless currency
            if choiceBuyDrink == "cashless" and Player["Inventory"]["cashless"] >= 1:
                Player["Inventory"]["cashless"] -= 1
                Player["Inventory"]["Potions"]["beer"] += 1
                stage_display(6)
            
            # If the player chooses "water" and has at least 3 cups
            elif choiceBuyDrink == "cup" and Player["Inventory"]["cup"] == 3:
                Player["Inventory"]["cup"] -= 3
                Player["Inventory"]["Potions"]["water"] += 1
                stage_display(6)
            
            # If no valid choice is made, call the move function
            elif choiceBuyDrink == "no":
                break
        # ---------------------------------------------
        # If the player is at "B3" or "D5" and there are objects in the room
        if current_position == "B3" and Map[current_position]["object"][0] == True or current_position == "D5" and Map[current_position]["object"][0] == True:
            print(f"Would you like a {Map[current_position]['object'][2]}?")
            choice = input("yes or no ").lower()
            while choice not in ["yes", "no"]:
                choice = input("You made a typo. yes or no ").lower()
            
            if choice == "yes":
                Player["Inventory"]["Potions"]["sweet_treat"] += 1
                Map[current_position]["object"][2] = False
                Map[current_position]["object"][0] = False

        # ---------------------------------------------
        # Ask the player for the next direction
        choice = input("Which direction do you want to take?" + str(Map[current_position]["print_possible_answers"]) + "\n").lower()
        while choice not in Map[current_position]["print_possible_answers"]:
                choice = input("You made a typo. Which direction do you want to take?" + str(Map[current_position]["print_possible_answers"])+ "\n").lower()
        
        # ---------------------------------------------
        # Allow the player to heal using potions: OK!!!
        if choice == "to heal":
          choicePotion = input("Take a potion: " + str(Player["Inventory"]["Potions"])+ " or no" + "\n").lower()
          while choicePotion not in Player["Inventory"]["Potions"] and choicePotion != "no"  :
              choicePotion = input("You made a typo. Take a potion: " + str(Player["Inventory"]["Potions"]) + " or no"  + "\n").lower()
            
          if choicePotion == "water" and Player["Inventory"]["Potions"]["water"] > 0:
            Player["life"] += Objects["water"]
            Player["Inventory"]["Potions"]["water"] -= 1
            stage_display(5)
          elif choicePotion == "beer" and Player["Inventory"]["Potions"]["beer"] > 0:
            Player["life"] += Objects["beer"]
            Player["Inventory"]["Potions"]["beer"] -= 1
            stage_display(5)
          elif choicePotion == "sweet_treat" and Player["Inventory"]["Potions"]["sweet_treat"] > 0:
            Player["life"] += Objects["sweet_treat"]
            Player["Inventory"]["Potions"]["sweet_treat"] -= 1
            stage_display(5)
        else:
            # By default, move the player to the next position
            index = Map[current_position]["print_possible_answers"].index(choice)
            current_position = Map[current_position]["possible_box_directions"][index]
        # ---------------------------------------------

