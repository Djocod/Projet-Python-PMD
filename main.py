import webbrowser 
from function import move


#function that presents the team and allows the user to go back to the main_menu and let user choose another editor after having choosen one and the link opened
import webbrowser
def about():
  print("This game was developped by Julie DANDRIMONT, Jordan FRANCOUAL and Melanie GASSER")
  #start the main loop and controls when the function is running
  stay_in_about_menu = True
  while stay_in_about_menu:
    print("Do you want to return to the main menu? Yes or no?")
    user_choice = input().lower()
    #---- return to the main menu ---
    if user_choice == "yes":
      #change the variable to false so the loop stops running
      stay_in_about_menu = False
      return menu()
    elif user_choice =="no":
      #inner loop for editor's choice
      choosing_editor = True
      while choosing_editor:
        print("Choose one of the three editors of the project for more information : Julie DANDRIMONT, Jordan FRANCOUAL, Melanie GASSER. If you want to go back to the previous menu type : back")
        user_choice= input().lower()
        #--- checks if the user wants to go back to the previous menu, previous menu --> menu where the player is asked if he wants to return to the main menu
        if user_choice =="back":
            choosing_editor = False # ends the loop and user will be redirected to previous menu where he will be asked if he wants to go back to main menu
        elif user_choice == "julie dandrimont":
          print("Opening Julie Dandrimont's LinkedIn :")
          webbrowser.open("https://www.linkedin.com/in/julie-dandrimont-a87402292/") #check if link goes to public profile or if you click this link it logs into my linkedin
        elif user_choice == "jordan francoual":
          print("Opening Jordan Francoual's LinkedIn")
          webbrowser.open("https://www.linkedin.com/in/jordan-francoual-a41b9728b/") #check if link goes to public profile or if you click this link it logs into my linkedin
        elif user_choice == "melanie gasser":
          print("Opening Melanie Gasser's LinkedIn")
          webbrowser.open("https://www.linkedin.com/in/melanie-gasser-11b9bb1aa") #check if link goes to public profile or if you click this link it logs into my linkedin --> OK PUBLIC PAGE
    else:
      print("Invalid input. Type yes or no")

def menu():
  print("Welcome on the Game JMJ FESTIVAL")
  choice = input(
  """
  ---------------- JMJ FESTIVAL ------------------
                    Main menu
  -------------------------------------------------
                    start game
                      about
                      quit
  """).lower()
  while choice not in ["start game","about","quit"]:
    print("Invalid input. Please choose one of the three options.")
    choice = input(
    """
    ---------------- JMJ FESTIVAL ------------------
                      Main menu
    -------------------------------------------------
                      start game
                        about
                        quit
    """).lower()

  if choice == "start game":
    move()
  elif choice == "about":
    about()
  elif choice == "quit":
    return
menu()
