from function import *
# from data_game import Player, Map

def start_game(): 
  current_position = Map['B1']
  move( Player, current_position)
  return
 
    
    
  #le debut du jeu --> entree en B1
  #reset la position de player a B1 --> voir dico de map
  #appeler la fonction direction
  #besoin d'une boucle pour que le jeu ne s'arrete pas?
  #va initialiser de toutes les données
  #return toutes les dictionnaires et position = B1
#   '''while player ne pas mort and player ne pas arrive dans la case finale and
#   player ne decide pas de quitter le jeu --> le jeu continue
#   '''

start_game()
