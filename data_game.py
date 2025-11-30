Player = {
    "name" :"input",
    "life" : 30,
     "Inventory" : {"Objects" : {"sign": 0,
                                "decath_chair": 0,
                                "fan": 0,
                                "empty_water_bottle":10, #POUR LE DEBUG A MODIFIER
                                },
                   "Potions" : {"water": 0,
                                "beer": 0,
                                "sweet_treat":0,
                                },
                   "cashless": 0,
                   "cup":0,
                  },
    "Attacks" : {
        "push": [1,95], #POUR LE DEBUG A MODIFIER = 5
        "love_dance": [8,60],
    }
    }
Drunk_crowd = {
    "name" : ["Corto","Geoffrey","Fadil","Lysianna","Florine"],
    "life" : 20,
    "Attacks" : {
        "sweaty_contact": [6,95],
        "step_on_the_feet": [8,60]
    },
    "dropped_object" : ["cashless_bracelet","beer"],
    }
Security = {
    "name" : "Breit from security",
    "life" : 50,
    "Attacks" : {
        "death_stare": [7,95],
        "body_search": [3,30], # prend bonbon et si pas de bonbon, il prend la bière
        "teargas": [8,60],
    },
    }


Objects = {"sign":2,
           "decath_chair": 8,
           "fan":6,
           "empty_water_bottle": 3,
           "water":5,
           "beer": 8,
           "sweet_treat": 10
           }


Map = {
    "B0" : {
          "room_name" :"Tuto",
          "coordinates":(1,1),
          "object" : [False, False, False ,False],
          "possible_box_directions":["B1","C1","quit"],
          "print_possible_answers" :["enter the festival"],
          "fight" : [False],
          "visited" :True,
          "direction_print" : 
              """
            
            Welcome to the world-renowned J.M.J FESTIVAL, 
              
              Here, there's only one rule: party hard.

              In the line, you unfortunately ran into a festival-goer who robbed you of all your items — including your ticket :( 
              As a result, you're beyond pissed, and you decide it's payback time: 
              
              >> you're now determined to rob every festival-goer who stands in your way of getting closer to the stage. 
              

              
              While moving around, you'll find items that might help you in a fight or heal you up. 
              Use your attacks, items and potions wisely... 
              Some items and potions can only be found once in this wonderful adventure. 
              Also, cashless bracelets and Empty cups can be exchanged at the bar for beer and water ;)
              
              Regarding your confrontations, you'll have one action per round. You'll be able to choose between using one of your two basic attack or use an item. 

            
              Security is on-site too… and they're not exactly friendly. 
              If you lose a fight, security will catch you and kick you out of the festival for causing public disorder and sneaking in without a valid ticket.

              You can heal yourself in between fights during your direction choice, just write "to heal" in the console

              """,
      },

    "B1" : {
          "room_name" :"Entrance",
          "coordinates":(2,1),
          "object" : [ True, "fan", False ,"cup" ],
          "possible_box_directions":["A1","C1","to heal","quit"],
          "print_possible_answers" :["left","crowd","to heal","quit"],
          "fight" : [False],
          "visited" : False,
          "direction_print" : 
              """
              At your arrival, a member of the staff greets you with a hand fan and a free cold beer (the dream ...).  

              Now the festival vibe has fully taken over, and you're feeling the joy of the moment.
              Still, you're more determined than ever to reach the Main Stage.



              You are at the junction.

              At your left :    In the distance, you can hear the sound of what seems to be a stage 
                               
              At your right : It's the beginning of the crowd.

              """,
      },
    "A1" : {
        "room_name" :"Stage",
        "coordinates":(1,1),
        "object" :[True, "sign","beer","cup"],
        "possible_box_directions":["B1","to heal","quit"],
        "print_possible_answers" :["right","to heal","quit"],
        "fight" : [False],
        "visited" : False,
        "direction_print" : """ 
            
            You're disappointed — it wasn't the Main Stage, and the music is a letdown. You decide to grab some belongings that were left unattended.

            You can now go back to the entrance. 


        """,
        },
    "C1" : {
        "room_name" :"beginning of the crowd",
        "coordinates":(3,1),
        "object" : [False,False,False,False],
        "possible_box_directions":["C2","to heal","quit"],
        "print_possible_answers" :["go further in the crowd","to heal","quit"],
        "fight" : [True, "Drunk_crowd",100], #100% 
        "visited" : False,
        "direction_print" : """

                You're walking in the beginning of the crowd. You pass by stalls full of clothes and jewelry, the festival buzzing with life. 
                It's summer, everything feels alive and chaotic. 

                further in the crowd seems to be only one way to the Main Stage.

""",
        },
    "C2" : {
        "room_name" :"Corridor",
        "coordinates":(3,2),
        "object" :[True,False,False,"cup"],
        "possible_box_directions":["D2","C3","to heal","quit"],
        "print_possible_answers" :["yes","no","to heal","quit"],#input == no -> C3 else D2
        "fight" : [False],
        "visited" : False,
        "direction_print" : """

        
        The risk reduction stand is just at your right and the 'safer staff' seems nice. 
        There's even a lonely cup on the floor waiting to be noticed.

        Do you need a break at the safer zone ? 

        """,
        },
    "D2" : {
        "room_name" :"safer zone",
        "coordinates":(4,2),
        "object" : [True,False,"water",False],
        "possible_box_directions":["C2","to heal","quit"],
        "print_possible_answers" :["return to crowd","to heal","quit"],
        "fight" : [False],
        "visited" : False,
        "direction_print" : """

                You've chatted with the staff and they gave you a bottle of water ! 

                Now that you've rested, you can go back to the crowd and finish you quest.

                From Here, you can only return to the crowd.
""",
        },
    "C3" : {
        "room_name" :"moving sculpture",
        "coordinates":(3,3),
        "object" :[True,"decath_chair",False,False],
        "possible_box_directions":["B3","C4","to heal","quit"],
        "print_possible_answers" :["to the bar","divination tent","to heal","quit"],
        "fight" : [False, "Drunk_crowd",30], # 30% chances to have this fight
        "visited" : False,
        "direction_print" : """

             You're facing a strange moving sculpture.

             Further in your left, you see the drink stand (bar)
             or you can head straight, even further in the crowd to the divination tent.


""",
        },
    "B3" : {
        "room_name" :"mini funfair",
        "coordinates":(2,3),
        "object" : [True, False,"sweet_treat",False],
        "possible_box_directions":["A3","C3","to heal","quit"],
        "print_possible_answers" :["bar","return to the moving statue","to heal","quit"],
        "fight" : [False],
        "visited" : False,
        "direction_print" : """

            You walk past the tiny funfair. 

            You can either You can go left toward the bar 
            or right to return to the moving statue.

""",
        },
    "A3" : {
        "room_name" :"bar",
        "coordinates" : (1,3),
        "object" :[True, False, False ,"cashless"], #if casheless == ou > beer price : 15
        "possible_box_directions":["B3","to heal","quit"],
        "print_possible_answers" :["return to the mini funfair","to heal","quit"],
        "fight" : [False],
        "visited" : False,
        "direction_print" : """
        
                Congrats, you've reached the bar. Unfortunately, this is not the end of your quest.
                However you can still stop by to refresh yourself with a cold beer or fresh water.

                From here, you can only retrace your steps and return to the mini funfair.
""",
        },
    "C4" : {
        "room_name" :"divination tent",
        "coordinates" : (3,4),
        "object" :[False, False, False ,False],
        "possible_box_directions":["C5","to heal","quit"],
        "print_possible_answers" :["go further into the music","to heal","quit"],
        "fight" : [False],
        "visited" : False,
        "direction_print" : """

                Out of curiousity, you ask the fortune teller to give you a prediction. 
                
                    ' When the gatewardens root themselves like ancient trees, let your tale drift toward them.
                    Once in a fleeting moment, the hard stone of duty may crack just enough for compassion to slip through.'


                But it's just gibberish to you.
                
                You begin to hear the music in the far, the goal is near. The main stage is definitely forward !
""",
        },
    "C5" : {
        "room_name" :"banner crossroad",
        "coordinates" : (3,5),
        "object" : [False, False, False ,False],
        "possible_box_directions":["B5","D5","to heal","quit"],
        "print_possible_answers" :["go to security","right","to heal","quit"],
        "visited" : False,
        "direction_print" : """

                You've reached a crossroad marked by a banner. 

                To your right, people are gathered around a camp fire. 
                To your left, you see security's light. You're just about to have your final fight.
                Make sure you've got as many items as possible before moving toward security.
""",
        "fight" : [False],
        
        },
    "D5" : {
        "room_name" :"camp fire",
        "coordinates" : (4,5),
        "object" : [True, "decath_chair"," sweet_treat" ,False],
        "possible_box_directions":["C5","to heal","quit"],
        "print_possible_answers" :["go back to the banner crossroad","to heal","quit"],
        "fight" : [False],
        "visited" : False,
        "direction_print" : """
        
        Nur Deutsche hier. Du verstehst nichts aber du sprichst mit jemanden der nett aussieht.
        Nach der Unterhaltung verabschieddet er sich und gibt dir ein Geschenk.

        From here you can only go back to the banner crossroad.
        """,
        },
    "B5" : {
        "room_name" :"security",
        "coordinates" : (2,5),
        "object" : [False, False, False ,False],
        "possible_box_directions":["B6","to heal","quit"],
        "print_possible_answers" :["go main","to heal","quit"],
        "fight" : [True, "Security",90], #A MODIFIER C'EST POUR LE DEBUG
        "visited" : False,
        "direction_print" :"""

        
        Bye Bye Breit, love you !
        
        """, 
        },
    "B6" : {
        "room_name" :"main_stage",
        "coordinates" : (2,6),
        "object" : [False, False, False ,False],
        "possible_box_directions":["to heal","quit"],
        "print_possible_answers" :["to heal","quit"],
        "fight" : [False],
        "visited" : False,
        "direction_print" : """
        
        At last, you stand before the Main Stage — massive, loud, and brighter than anything you've seen tonight. 
        Your journey ends here. 

        Good job ! You're a very unhethical person ;))
        
        """,
        },
    "B7" : { #End square that is not played!
        },
}
start_position = "B0"