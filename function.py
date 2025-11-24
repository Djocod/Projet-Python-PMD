from data_game import Player, Map, Objects, Drunk_crowd, Security, current_position
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
# Function to handle player movement
def move(current_position):
    # While the player is alive, hasn't reached "B6", and hasn't quit
    while Player["life"] > 0 and current_position != "B6" and quit == False:
        # ---------------------------------------------
        # Display the description of the current room
        print(Map[current_position]["direction_print"])
        # ---------------------------------------------
        if Map[current_position]["fight"] == True:
          print("okk")
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