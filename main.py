import webbrowser 
from function import move


def about():
  print("This game was developped by Julie DANDRIMONT, Jordan FRANCOUAL and Melanie GASSER")
  print("Do you want to return to the main menu? Yes or no?")
  user_choice = input().lower()
  if user_choice == "yes":
    return menu()
  else:
    print("Choose one of the three editors of the project for more information : Julie DANDRIMONT, Jordan FRANCOUAL, Melanie GASSER")
    user_choice = input().lower()
    if user_choice == "julie dandrimont":
      webbrowser.open("https://www.linkedin.com/in/julie-dandrimont-a87402292/") #check if link goes to public profile or if you click this link it logs into my linkedin
    elif user_choice == "jordan francoual":
     webbrowser.open("https://www.linkedin.com/in/jordan-francoual-a41b9728b/") #check if link goes to public profile or if you click this link it logs into my linkedin
    elif user_choice == "melanie gasser":
      webbrowser.open("https://www.linkedin.com/in/melanie-gasser-11b9bb1aa") #check if link goes to public profile or if you click this link it logs into my linkedin
      
def menu():
  print("Welcome on the Game JMJ FESTIVAL")
  choice = input(
  """
  ---------------- JMJ FESTIVAL ------------------
                    Main menu
  -------------------------------------------------
                    Start Game
                      About
                      Quit
  """)
  if choice == "Start Game":
    move()
  elif choice == "About":
    about()
  elif choice == "Quit":
    return
menu()
