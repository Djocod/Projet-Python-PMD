import webbrowser 
from data_game import Player, Map, Objects, Drunk_crowd, Security # player_path
from random import randint
import matplotlib.pyplot as plt

# ================================================

def stage_display(nb):

    stages= [
    f""" 6
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
    ------------------------------------------------
    |Life : {Player["life"]}  Position : {Map[current_position]["room_name"]}
    |Objects:                    | Potions :       |
    ------------------------------------------------
    |Sign         : {Player["Inventory"]["Objects"]["sign"]}            |Water       : {Player["Inventory"]["Potions"]["water"]}  |
    |Decat_chair  : {Player["Inventory"]["Objects"]["decath_chair"]}            |Beer        : {Player["Inventory"]["Potions"]["beer"]}  |
    |Fan          : {Player["Inventory"]["Objects"]["fan"]}            |sweet treat : {Player["Inventory"]["Potions"]["sweet_treat"]}  |
    |Empty_water_bottle : {Player["Inventory"]["Objects"]["empty_water_bottle"]}      |                 | 
    ------------------------------------------------
    |Exchange : Cashless : {Player["Inventory"]["cashless"]} / Cup : {Player["Inventory"]["cup"]}             |
    
    """,
    f"""3
    =============================================
    Texte: {Map[current_position]["direction_print"]}
    """,
    f""" 2
    |Drunk crowd attacks | life : {Drunk_crowd["life"]}                                     |Your attacks | Life : {Player["life"]}
    |sweaty_contact  : {Drunk_crowd["Attacks"]["sweaty_contact"][0]} dommage  | Chance of Hit:{Drunk_crowd["Attacks"]["sweaty_contact"][1]}%      |Push      : {Player["Attacks"]["push"][0]} dommage  | Chance of Hit : {Player["Attacks"]["push"][1]}%
    |step_on_the_feet: {Drunk_crowd["Attacks"]["step_on_the_feet"][0]} dommage  | Chance of Hit:{Drunk_crowd["Attacks"]["step_on_the_feet"][1]}%      |Love dance: {Player["Attacks"]["love_dance"][0]} dommage  | Chance of Hit : {Player["Attacks"]["love_dance"][1]}%
    
    
                    |Sign               : {Player["Inventory"]["Objects"]["sign"]} |Dommage : {Objects["sign"]} |Water       : {Player["Inventory"]["Potions"]["water"]} | + {Objects["water"]} HP
                    |Decat chair        : {Player["Inventory"]["Objects"]["decath_chair"]} |Dommage : {Objects["decath_chair"]} |Beer        : {Player["Inventory"]["Potions"]["beer"]} | + {Objects["beer"]} HP
                    |Fan                : {Player["Inventory"]["Objects"]["fan"]} |Dommage : {Objects["fan"]} |sweet treat : {Player["Inventory"]["Potions"]["sweet_treat"]} | + {Objects["sweet_treat"]} HP
                    |Empty water bottle : {Player["Inventory"]["Objects"]["empty_water_bottle"]} |Dommage : {Objects["empty_water_bottle"]} | + {Objects["empty_water_bottle"]} HP
                                          
    """,
    f"""  1
    |{Security["name" ]} |   {Security["life"]}                            |Your attacks | Life : {Player["life"]}
    |Death_stare  : {Security["Attacks"]["death_stare"][0]} dommage  | Chance of Hit:{Security["Attacks"]["death_stare"][1]}%       |Push      : {Player["Attacks"]["push"][0]} dommage  | Chance of Hit : {Player["Attacks"]["push"][1]}%
    |Body_search  : {Security["Attacks"]["body_search"][0]} dommage  | Chance of Hit :{Security["Attacks"]["body_search"][1]}%      |Love dance: {Player["Attacks"]["love_dance"][0]} dommage  | Chance of Hit : {Player["Attacks"]["love_dance"][1]}%
    |Teargas      : {Security["Attacks"]["teargas"][0]} dommage  | Chance of Hit:{Security["Attacks"]["teargas"][1]}%
    

                    |Sign               : {Player["Inventory"]["Objects"]["sign"]} |Dommage : {Objects["sign"]} |Water       : {Player["Inventory"]["Potions"]["water"]} | + {Objects["water"]} HP
                    |Decat chair        : {Player["Inventory"]["Objects"]["decath_chair"]} |Dommage : {Objects["decath_chair"]} |Beer        : {Player["Inventory"]["Potions"]["beer"]} | + {Objects["beer"]} HP
                    |Fan                : {Player["Inventory"]["Objects"]["fan"]} |Dommage : {Objects["fan"]} |sweet treat : {Player["Inventory"]["Potions"]["sweet_treat"]} | + {Objects["sweet_treat"]} HP
                    |Empty water bottle : {Player["Inventory"]["Objects"]["empty_water_bottle"]} |Dommage : {Objects["empty_water_bottle"]} | + {Objects["empty_water_bottle"]} HP
    """
    ]

    print(stages[6 - nb])

# ================================================
# Functions for the fights

def select_attack(Player):

  #deals with the case where the Inventory is empty
  if Player["Inventory"]["Objects"]["sign"]+Player["Inventory"]["Objects"]["decath_chair"]+ Player["Inventory"]["Objects"]["empty_water_bottle"]+Player["Inventory"]["Objects"]["fan"]+  Player["Inventory"]["Potions"]["water"]+Player["Inventory"]["Potions"]["beer"]+Player["Inventory"]["Potions"]["sweet_treat"]==0:
    print("You do not have found any items yet. Select a basic attack : Push or love_dance ")
    choice = input().lower()
    while choice not in ["push","love_dance"]:
        choice = input("You miss typed your attack. Select a basic attack : push or love_dance  ")
    return ("Attacks",choice) #returns type and the choice of player attacks
  
  elif Player["Inventory"]["Objects"]["sign"]+Player["Inventory"]["Objects"]["decath_chair"]+ Player["Inventory"]["Objects"]["empty_water_bottle"]+Player["Inventory"]["Objects"]["fan"]==0:
    #deals with the case where there is no objects in the inventory
    print("You do not have found any objects yet. Do you want to use potions or basic attacks ?  ")
    choice = input().lower()

    while choice not in ["potions","basic attacks"]:
      choice = input("You miss typed your answer. Do you want to use potions or basic attacks ?  ").lower()

    if choice == "potions":
      print("Choose one of the objects of the following list"," ",Player["Inventory"]["Potions"])
      selected_item = input()

      #deals with typing errors or invalid answers
      while selected_item not in ["water","beer","sweet_treat"] or Player["Inventory"]["Potions"][selected_item]==0 :
        selected_item = input("please select a valid item  ").lower()

      if Player["Inventory"]["Potions"][selected_item] > 0:
        #drink water --> empty bottle as an attack object
        if selected_item == "water":
          print(Player["Inventory"]["Potions"][selected_item])
          Player["Inventory"]["Objects"]["empty_water_bottle"] += 1
        Player["Inventory"]["Potions"][selected_item] -= 1
        return ("Potions",selected_item)
      
    elif choice == "basic attacks":
      choice = input("Select a basic attack : 'push' or 'love_dance' ")
      #deals with typing errors or invalid answers
      while choice not in ["push","love_dance"]:
        choice = input("You miss typed your attack. Select a basic attack : push or love_dance  ")
      return ("Attacks",choice)

  # deals with the case where there is no potions in the inventory 
  elif Player["Inventory"]["Potions"]["water"]+Player["Inventory"]["Potions"]["beer"]+Player["Inventory"]["Potions"]["sweet_treat"]==0:
    print("You do not have found any potions yet. Do you want to use objects or basic attacks ?  ")
    choice = input().lower()
    while choice not in ["objects","basic attacks"]:
      choice = input("You miss typed your answer. Do you want to use objects or basic attacks ?  ").lower()

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


    elif choice == "basic attacks":
      choice = input("Select a basic attack : 'push' or 'love_dance' ")
      #deals with typing errors or invalid answers
      while choice not in ["push","love_dance"]:
        choice = input("You miss typed your attack. Select a basic attack : push or love_dance  ")
      return ("Attacks",choice)
    
  # Ask what action the player wants to do
  else:
    choice = input("Do you want to use 'objects' , 'potions' or 'basic attacks' ?  ").lower()
    while choice not in ["objects","potions","basic attacks"]:
      choice = input("You miss typed your answer. Do you want to use objects , 'potions' or 'basic attacks' ?  ").lower()


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
      choice = input("Select a basic attack : 'push' or 'love_dance' ")
      #deals with typing errors or invalid answers
      while choice not in ["push","love_dance"]:
        choice = input("You miss typed your attack. Select a basic attack : push or love_dance  ")
      return ("Attacks",choice)


def fight(Player,enemy_type):
    
  # Initialisation of enemy's characteristics
  if enemy_type == "Drunk_crowd":
    enemy_name = Drunk_crowd["name"][randint(0,len(Drunk_crowd["name"])-1)]
    enemy_life = Drunk_crowd['life']
    enemy_attacks = Drunk_crowd['Attacks']
    nb = 2

  else:
    enemy_name = Security["name"]
    enemy_life = Security['life']
    enemy_attacks = Security['Attacks']
    nb = 1

  #print(enemy_name,enemy_life,enemy_attacks)
  print("A confrontation has been declared between you and "+ str(enemy_name )
        + "... You'll have to fight to reach your ultimate goal : enjoy the music on the main stage."+ "\n" 
        + "Your opponent has " + str(enemy_life) + " points of life" + "\n"
        + """ Use your attacks, items and potions wisely... Some items and potions can only be found once in this wonderful adventure.

        About the objects, the stop sign ('sign') is used as a defense item. It skips the opponent's turn. The other are attack objects.

        You just have on action per round. 
          """)
  
  if enemy_type == "Security":
    print("You've encounter your last confrontation. Fight well lill troubadour")

  while  Player["life"] > 0 and enemy_life > 0 :
    
    stage_display(nb)
    
    choice_player = select_attack(Player) #ie , choice_player("Attacks","push")


    # player's turn
    if choice_player[0]== "Potions":
      Player["life"] += Objects[choice_player[1]] #
      print("You used " + choice_player[1])
      print("You regain " + str(Objects[choice_player[1]])+ " points of life")
      print(" >> You have now  " + str(Player["life"])+ " points of life")
      print("In your inventory there is  " + str(Player["Inventory"]["Potions"][choice_player[1]])+ " "+ choice_player[1]+ " remaining")


    elif choice_player[0]== "Objects":
      if choice_player[1]== "sign":
        enemy_life -= Objects[choice_player[1]] # skips enemy turn + causes him 2 points of damage
        print("You used " + choice_player[1] + " defense")
        print(enemy_name + " lost " + str(Objects[choice_player[1]]) + " points of life")
        if enemy_life > 0 :
          print(enemy_name + " has now " + str(enemy_life) + " points of life")
        else : 
          print(enemy_name + " has now 0 points of life ")
        print(enemy_name + " wont be able to attack next turn")

      else :
        enemy_life -= Objects[choice_player[1]] # inflicts attack damage to the enemy
        print("\n"+"You used " + choice_player[1] + " as an attack object")
        print("\n"+str(enemy_name) + " lost " + str(Objects[choice_player[1]]) + " points of life")
        if enemy_life > 0 :
          print("\n"+">> " +enemy_name + " has now " + str(enemy_life) + " points of life")
        else : 
          print("\n"+">> " + enemy_name + " has now 0 points of life ")
        print("\n"+"In your inventory there is  " + str(Player["Inventory"]["Objects"][choice_player[1]])+ " "+ choice_player[1]+ " remaining")



    elif choice_player[0] == "Attacks":
      chances_of_hit = randint(0,100) #emulate a dice throw to see if your attack reached the opponent
      if chances_of_hit < Player["Attacks"][choice_player[1]][1]:
        enemy_life -= Player["Attacks"][choice_player[1]][0]
        print("\n"+"You used " + choice_player[1] + " attack")
        print("\n"+enemy_name + " lost " + str(Player["Attacks"][choice_player[1]][0]) + " points of life")
        if enemy_life > 0 :
          print("\n"+">> " + enemy_name + " has now " + str(enemy_life) + " points of life")
          if enemy_type == "Drunk_crowd":
            Drunk_crowd['life'] = enemy_life
          else:
            Security['life'] = enemy_life
        else : 
          print("\n"+">> " + enemy_name + " has now 0 points of life ")
      else :
        print("\n"+"you missed your shot")
        print("\n"+">> " + enemy_name + " has still " + str(enemy_life) + " points of life")


    # enemy's turn

    #security has 3 attacks
    if enemy_type == "Security":
      enemy_choice = list(enemy_attacks.keys())[randint(0,2)]
    else:
      enemy_choice = list(enemy_attacks.keys())[randint(0,1)] # enemy_choice = string of the attack
  

    #skip enemy's turn if sign used
    if choice_player == ("Objects","sign"):
      print("\n"+"The sign skips the " + enemy_name + "'s turn") 

    else : 
      chances_of_hit = randint(0,100) # emulate a dice throw to see if the attack succeeds 
      
      if chances_of_hit < enemy_attacks[enemy_choice][1] and enemy_life > 0: 
        print(chances_of_hit)
        if enemy_choice == "body_search":
          if Player["Inventory"]["Potions"]["sweet_treat"] > 0:
            Player["Inventory"]["Potions"]["sweet_treat"] = 0
            print("Breit took all your sweet candies")
          else:
            Player["life"] -= enemy_attacks[enemy_choice][0] # removes 3 life points
            print("\n"+"Breit hasn't found any sweet substance on you, but he shook you very well so you loose 3 points of life")
            print("\n"+">> You have " + str(Player["life"])+ " points of life remaining")
        else : 
          Player["life"] -= enemy_attacks[enemy_choice][0] #attack dammages
          print(enemy_name + " successfully used "+ enemy_choice + " on you")
          print("\n"+"You lost " + str( enemy_attacks[enemy_choice][0])+ " points of life")
          print("\n"+">> You have " + str(Player["life"])+ " points of life remaining")
          
      elif enemy_life <= 0 : 
        print(enemy_name + " is exhausted and leave you alone. You are victorious")
        return Player["life"]
      else:
        print(enemy_name + " tried to use " + enemy_choice + " on you but miserably failed :( ")

    if Player["life"] <= 0 :
      print("shit you're dead")    
      return Player["life"]

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
        print("You spot a lonely Decathlon chair abandoned right. You loot the chair.")
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
# Function to run the game - more specifically Player movements on the maps and the events that follow

def move():
  global current_position
  current_position = "B0"
  player_path = []
  game_on = True

  plot_map(current_position,player_path) # initial plot of the map

  while Player["life"]> 0 and current_position != "B7" and game_on != False: # main game loop

    if Map[current_position]["fight"][0] == True:
      dice = randint(0,100) #some fights don't appear all the time
 

      if dice <= Map[current_position]["fight"][2] : 
        
        Player["life"] = fight(Player,str(Map[current_position]["fight"][1])) #take enemy type as an argument

        Map[current_position]["fight"][0] = False # fight has occured, so we set it to false

      elif current_position == "B5" and dice > Map[current_position]["fight"][2]and Player["life"]> 0: # bribe security
        print("For some strange reason, Breit is moved by your story and let himself be corrubted. Breit let you through to enjoy the concert.")

        #loot the drunk crowd dropped objects   
      if Map[current_position]["fight"][1] == "Drunk_crowd" and Player["life"]> 0:
        print("""After plenty of dodging and squeezin through, you finally managed to get past festival-goer who was blocking your way. You decide to snatch their cashless wristband and their beer as payback.""")
        Player["Inventory"]["Potions"]["beer"]+=1
        Player["Inventory"]["cashless"]+=1 

        #We check if the player is still alive; if so, we ask them to choose between 
        #restarting the game or returning to the main menu.
      if Player["life"] <= 0 : 
        choice = input("Do you want play again ? yes or no." + "\n")
        # If yes, his inventory returns to 0, the fight boxes are reset to 
        #True, and the same applies to objects.
        if choice == "yes": #reset the player inventory and game state
          Player["life"] = 30
          for key in Player["Inventory"]["Objects"]:
            Player["Inventory"]["Objects"][key] = 0
          for key in Player["Inventory"]["Potions"]:
            Player["Inventory"]["Potions"][key] = 0
          Player["Inventory"]["cashless"] = 0
          Player["Inventory"]["cup"] = 0
            
            #I request that the visited properties be set to False.
          list_room_visited_true =["B1","A1","C1","C2","D2","C3","B3","A3","C4","C5","D5","B5","B6"]        
          for room in list_room_visited_true:
            Map[room]["visited"] = False #reset visited to false
            
            #list of object cases that must be reset to true
          list_room_objet_true =["B1","A1","C2","D2","C3","B3","A3","D5"]
          for room in list_room_objet_true:
            Map[room]["object"][0]= True #reset object to true
              
            #list of fight boxes that must be re-entered true
          list_room_fight = ["C1","C3","B5"]
          for room in list_room_fight:
            Map[room]["fight"][0]= True #reset fight to true
            # Come back to the start 
          current_position = "B0"
          return move()
        elif choice == "no": # exit the game
          print("Thank you for your participation !")
          return

    #Display stat:
    stage_display(4)
    
    print(Map[current_position]["direction_print"]) # display the description of the room


      # Check if the room contains objects and collect them
    if Map[current_position]["object"][0] == True:
      objects_in_the_room(current_position)
      
      # If the player is at the bar and has enough resources, offer drinks
      choiceBuyDrink = 0

      if current_position == "A3":
        print("""
              
          After chatting with a beautiful stranger, she generously
          offers you a cashless payment to help you drown your sorrows.
          As a bonus, you get her discord ID.
         ErwinTheCat ;)
        """)
        Map[current_position]["object"][3]= False  #cashless has been picked up

        while choiceBuyDrink!= "no":
          choiceBuyDrink = input("What can I get you, troubadour? Exchange your 'cashless'for a beer or your 3 'cup' for a water drink or type 'no' to move on" + "\n").lower()
          while choiceBuyDrink not in ["cashless", "cup","no"]: #validate input
            choiceBuyDrink = input("You made a typo. What can I get you, troubadour? Exchange your 'cashless' for a beer or your 3 'cup' for a water drink or type 'no' to move on" + "\n").lower()
        
          # If the player chooses "beer" and has enough cashless currency
          if choiceBuyDrink == "cashless" and Player["Inventory"]["cashless"] >= 1:
              Player["Inventory"]["cashless"] -= 1
              Player["Inventory"]["Potions"]["beer"] += 1
              stage_display(6)
          
          # If the player chooses "water" and has at least 3 cups
          elif choiceBuyDrink == "cup":
              if Player["Inventory"]["cup"] == 3:
                  Player["Inventory"]["cup"] -= 3
                  Player["Inventory"]["Potions"]["water"] += 1
                  stage_display(6)
              else : 
                  print("You don't have enough cups!")
        
      # ---------------------------------------------
      # If the player is at "B3" or "D5" and there are objects in the room
    if current_position == "B3" and Map[current_position]["object"][0] == True or current_position == "D5" and Map[current_position]["object"][0] == True:
          
          # Offer the player to take the "sweet_treat" potion
          print(f"Psst psst. Someone offers you a {Map[current_position]['object'][2]}, would you like to take it ?")
          choice = input("yes or no "+ "\n").lower()
          while choice not in ["yes", "no"]:
              choice = input("You made a typo. yes or no ").lower()
          
          if choice == "yes":
              Player["Inventory"]["Potions"]["sweet_treat"] += 1
              Map[current_position]["object"][2] = False
              Map[current_position]["object"][0] = False

    if current_position =="C3" and Map[current_position]["visited"]== False:
          print(" Someone catches your attention to the left.")
  
    # Enjoy the surprise !!!
    if current_position == "B6": 
      print("You've made it to the main stage, enjoy the festival!")
      webbrowser.open("https://urlr.me/vbfGyk") 
      return

      # ---------------------------------------------
      # Ask the player for the next direction
    choice = input(" Which direction do you want to take ?" + str(Map[current_position]["print_possible_answers"]) + "\n").lower() 
    while choice not in Map[current_position]["print_possible_answers"]:
      choice = input("You made a typo. Which direction do you want to take?" + str(Map[current_position]["print_possible_answers"])+ "\n").lower()
      
      
    if choice == "quit": 
      answer = input("You are quitting the game, type yes to continue"+ "\n").lower()
      while answer != "yes":
        answer = input("Please answer yes. Are you sure you want to quit ?"+ "\n").lower()
      game_on = False # exit the game loop

      # ---------------------------------------------
      # Allow the player to heal using potions !!
    elif choice == "to heal":
      choicePotion = input("Take a potion: " + str(Player["Inventory"]["Potions"])+ " or no" + "\n").lower()
      while choicePotion not in Player["Inventory"]["Potions"] and choicePotion != "no"  :
            choicePotion = input("You made a typo. Take a potion: " + str(Player["Inventory"]["Potions"]) + " or no"  + "\n").lower()
          
      if choicePotion == "water" and Player["Inventory"]["Potions"]["water"] > 0:
        Player["life"] += Objects["water"]
        Player["Inventory"]["Potions"]["water"] -= 1
        Player["Inventory"]["Objects"]["empty_water_bottle"] += 1
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
      index = Map[current_position]["print_possible_answers"].index(choice) #print de direction
      previous_position = current_position #save previous position
      Map[current_position]["visited"] = True
      current_position = Map[current_position]["possible_box_directions"][index] #update current position
      #update player path for plotting
      if current_position in Map:
        player_path.append((previous_position,current_position))
      plot_map(current_position,player_path)

      # ---------------------------------------------


#DEF PLOT MAP OF THE GAME

def plot_map(current_position,player_path):

  coordinates_of_the_rooms = [Map[room]["coordinates"]for room in Map]

  x = [coordinates_of_x[0] for coordinates_of_x in coordinates_of_the_rooms]
  y = [coordinates_of_y[1] for coordinates_of_y in coordinates_of_the_rooms]

  plt.figure(figsize=(8,6))
  plt.scatter(x,y, c="b", s=10)
  plt.scatter(Map[current_position]["coordinates"][0],Map[current_position]["coordinates"][1],c="r",s=50)

  #plot lines to show the player's path
  for room_a, room_b in player_path:
    x1,y1 = Map[room_a]["coordinates"]
    x2,y2 = Map[room_b]["coordinates"]
    plt.plot([x1,x2],[y1,y2],linewidth=0.5,color="gray")

  #plot names of the visited rooms
  for room in Map:
    if Map[room]["visited"]:
      x,y = Map[room]["coordinates"]
      room_name = Map[room]["room_name"]
      plt.text(x+0.05, y+0.1,room_name,fontsize=10,color="black")

  #plot title of the graph
  plt.title("J.M.J.Festival", color="black")

  #remove the numbers next to x and y axes
  plt.xticks([])
  plt.yticks([])

  plt.show()