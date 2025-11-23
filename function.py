from data_game import Player, Map, Objects

# ================================================
# Function to buy drinks at a specific location
def buy_drink(Player, current_position):
    # Display the player's inventory for potions and currency
    print(Player["Inventory"]["Potions"]["beer"], Player["Inventory"]["cashless"])
    print(Player["Inventory"]["Potions"]["water"], Player["Inventory"]["cup"])
    
    # While the player has life and is at position "A3"
    while Player["life"] > 0 and current_position == "A3":
        # Ask the player what they want to buy
        choiceBuyDrink = input("What can I get you? 'beer' = 1 cashless, 'water' = 3 cups, nope")
        
        # If the player chooses "beer" and has enough cashless currency
        if choiceBuyDrink == "beer" and Player["Inventory"]["cashless"] >= 1:
            Player["Inventory"]["cashless"] -= 1
            Player["Inventory"]["Potions"]["beer"] += 1
            print(Player["Inventory"]["Potions"]["beer"], Player["Inventory"]["cashless"])
        
        # If the player chooses "water" and has at least 3 cups
        elif choiceBuyDrink == "water" and Player["Inventory"]["cup"] == 3:
            Player["Inventory"]["cup"] -= 3
            Player["Inventory"]["Potions"]["water"] += 1
            print(Player["Inventory"]["Potions"]["water"], Player["Inventory"]["cup"])
        
        # If no valid choice is made, call the move function
        else:
            move(current_position)

# ================================================
# Function to collect objects in the current room
def objects_in_the_room(current_position):
    # Check if there is a "fan" in the room
    if Map[current_position]["object"][1] == "fan":
        Player["Inventory"]["Objects"]["fan"] += 1
        Map[current_position]["object"][1] = False
    
    # Check if there is a "decat_chair" in the room
    elif Map[current_position]["object"][1] == "decat_chair":
        Player["Inventory"]["Objects"]["decat_chair"] += 1
        Map[current_position]["object"][1] = False
    
    # Check if there is a "sign" in the room
    elif Map[current_position]["object"][1] == "sign":
        Player["Inventory"]["Objects"]["sign"] += 1
        Map[current_position]["object"][1] = False

    # Check for potions in the room
    if Map[current_position]["object"][2] == "water":
        Player["Inventory"]["Potions"]["water"] += 1
        Map[current_position]["object"][2] = False
    elif Map[current_position]["object"][2] == "beer":
        Player["Inventory"]["Potions"]["beer"] += 1
        Map[current_position]["object"][2] = False
    elif Map[current_position]["object"][2] == "super_beer":
        Player["Inventory"]["Potions"]["super_beer"] += 1
        Map[current_position]["object"][2] = False

    # Check for other items like "cashless" or "cup"
    if Map[current_position]["object"][3] == "cashless":
        Player["Inventory"]["cashless"] += 1
        Map[current_position]["object"][3] = False
    elif Map[current_position]["object"][3] == "cup":
        Player["Inventory"]["cup"] += 1
        Map[current_position]["object"][3] = False

# ================================================
# Function to handle player movement
def move(current_position):
    # While the player is alive, hasn't reached "B6", and hasn't quit
    while Player["life"] > 0 or current_position != "B6" or quit == False:
        # ---------------------------------------------
        # Display the description of the current room
        print(Map[current_position]["direction_print"])

        # ---------------------------------------------
        # Check if the room contains objects and collect them
        if Map[current_position]["object"][0] == True:
            objects_in_the_room(current_position)
        
        # If the player is at "B3" and has enough resources, offer drinks
        if current_position == "B3" and Player["Inventory"]["cashless"] > 0 or current_position == "B3" and Player["Inventory"]["cup"] >= 3:
            choice = input("What can I get you, troubadour? [cashless, cup]")
            
            if choice == "cashless":
                Player["Inventory"]["cashless"] -= 1
                Player["Inventory"]["Potions"]["beer"] += 1
            elif choice == "cup":
                Player["Inventory"]["cup"] -= 3
                Player["Inventory"]["Potions"]["water"] += 1

        # If the player is at "B3" or "D5" and there are objects in the room
        if current_position == "B3" and Map[current_position]["object"][0] == True or current_position == "D5" and Map[current_position]["object"][0] == True:
            print(f"Would you like a {Map[current_position]['object'][2]}?")
            choice = input("yes or no ").lower()
            if choice == "yes":
                Player["Inventory"]["Potions"]["sweet_treat"] += 1
                Map[current_position]["object"][2] = False
                Map[current_position]["object"][0] = False

        # ---------------------------------------------
        # Ask the player for the next direction
        choice = input("Which direction do you want to take?" + str(Map[current_position]["print_possible_answers"]) + "\n")
        
        # ---------------------------------------------
        # If the player is at "A3", offer drinks
        if current_position == "A3" and Player["Inventory"]["cashless"] > 0 or current_position == "A3" and Player["Inventory"]["cup"] >= 3:
            buy_drink(Player, current_position)
        
        # ---------------------------------------------
        # Allow the player to heal using potions
        if choice == "to heal":
            choicePotion = input("Take a potion: " + str(Player["Inventory"]["Potions"]))
            if choicePotion == "water" and Player["Inventory"]["Potions"]["water"] > 0:
                Player["life"] += Objects["water"][1]
                Player["Inventory"]["Potions"]["water"] -= 1
            elif choicePotion == "beer" and Player["Inventory"]["Potions"]["beer"] > 0:
                Player["life"] += Objects["beer"][1]
                Player["Inventory"]["Potions"]["beer"] -= 1
            elif choicePotion == "super_beer" and Player["Inventory"]["Potions"]["super_beer"] > 0:
                Player["life"] += Objects["super_beer"][1]
                Player["Inventory"]["Potions"]["super_beer"] -= 1
            elif choicePotion == "sweet_treat" and Player["Inventory"]["Potions"]["sweet_treat"] > 0:
                Player["life"] += Objects["sweet_treat"][1]
                Player["Inventory"]["Potions"]["sweet_treat"] -= 1
        else:
            # By default, move the player to the next position
            index = Map[current_position]["print_possible_answers"].index(choice)
            current_position = Map[current_position]["possible_box_directions"][index]