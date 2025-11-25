Player = {
    "name" :"input",
    "life" : 30,
     "Inventory" : {"Objects" : {"sign": 0,
                                "decath_chair": 0,
                                "fan": 0,
                                "empty_water_bottle":0,
                                },
                   "Potions" : {"water": 0,
                                "beer": 0,
                                "sweet_treat":0,
                                },
                   "cashless": 0,
                   "cup":0,
                  },
    "Attacks" : {
        "push": [5,95],
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
    "B1" : {
          "room_name" :"Entrance",
          "coordinates":(2,1),
          "object" : [ True, "fan", False ,"cup" ],
          "possible_box_directions":["A1","C1","to heal","quit"],
          "print_possible_answers" :["left","crowd","to heal","quit"],
          "fight" : [False],
          "direction_print" : 
              """
              Bienvenue au J.M.J FESTIVAL, 
              
              Ici, il n'y a qu'un mot d'ordre faire la fête, ta mission grillée 
              la place des autres festivaliers afin d'arriver à la Scène principale.
              Tu devras donc te battre contre certains festivaliers qui ne voudront pas te laisser passer.
              Durant tes déplacements, tu trouveras des objets qui pourront éventuellement t'aider à te battre ou te soigner.
              
              La sécurité est présente sur le site et elle n'est pas vraiment sympa.
              """,
      },
    "A1" : {
        "room_name" :"secret_room_1",
        "coordinates":(1,1),
        "object" :[True, "sign","beer","cup"],
        "possible_box_directions":["B1","to heal","quit"],
        "print_possible_answers" :["right","to heal","quit"],
        "fight" : [False],
        "direction_print" : "",
        },
    "C1" : {
        "room_name" :"crowd_1",
        "coordinates":(3,1),
        "object" : [False,False,False,False],
        "possible_box_directions":["C2","to heal","quit"],
        "print_possible_answers" :["go further in the crowd","to heal","quit"],
        "fight" : [True, "Drunk_crowd"], #100%
        "direction_print" : "",
        },
    "C2" : {
        "room_name" :"hallway_1",
        "coordinates":(3,2),
        "object" :[True,False,False,"cup"],
        "possible_box_directions":["D2","C3","to heal","quit"],
        "print_possible_answers" :["yes","no","to heal","quit"],#input == no -> C3 else D2
        "fight" : [False],
        "direction_print" : "Do you need a break?",
        },
    "D2" : {
        "room_name" :"safer_zone",
        "coordinates":(4,2),
        "object" : [True,False,"water",False],
        "possible_box_directions":["C2","to heal","quit"],
        "print_possible_answers" :["return to crowd","to heal","quit"],
        "fight" : [False],
        "direction_print" : "",
        },
    "C3" : {
        "room_name" :"crowd_2",
        "coordinates":(3,3),
        "object" :[True,"decat_chair",False,False],
        "possible_box_directions":["B3","C4","to heal","quit"],
        "print_possible_answers" :["direction to the bar","go further in the crowd","to heal","quit"],
        "fight" : [False, "Drunk_crowd"], # 30%
        "direction_print" : "",#qqn a attirer ton attention a gauche et tu vois la buvette un peu plus loin a gauche
        },
    "B3" : {
        "room_name" :"hallway_2",
        "coordinates":(2,3),
        "object" : [True, False,"sweet_treat",False],
        "possible_box_directions":["A3","C3","to heal","quit"],
        "print_possible_answers" :["bar","return to the crowd","to heal","quit"],
        "fight" : [False],
        "direction_print" : "",
        },
    "A3" : {
        "room_name" :"bar",
        "coordinates" : (1,3),
        "object" :[True, False, False ,"cashless"], #if casheless == ou > beer price : 15
        "possible_box_directions":["B3","to heal","quit"],
        "print_possible_answers" :["return to the crowd","to heal","quit"],
        "fight" : [False],
        "direction_print" : "",
        },
    "C4" : {
        "room_name" :"hallway3",
        "coordinates" : (3,4),
        "object" :[False, False, False ,False],
        "possible_box_directions":["C5","to heal","quit"],
        "print_possible_answers" :["go further into the music","to heal","quit"],
        "fight" : [False],
        "direction_print" : "",#Tu entends la musique de plus en plus tu the rapproches de la mainstage
        },
    "C5" : {
        "room_name" :"hallway4",
        "coordinates" : (3,5),
        "object" : [False, False, False ,False],
        "possible_box_directions":["B5","D5","to heal","quit"],
        "print_possible_answers" :["go to security","right","to heal","quit"],
        "direction_print" : "",#a droit secret room en allemand et a gauche les lumieres de la secu
        "fight" : [False],
        #rassure toi que tu as le plus d objet possible avant d avancer vers la secu
        },
    "D5" : {
        "room_name" :"secret_room_2",
        "coordinates" : (4,5),
        "object" : [True, "decat_chair"," sweet_treat" ,False],
        "possible_box_directions":["C5","to heal","quit"],
        "print_possible_answers" :["go back to the music","to heal","quit"],
        "fight" : [False],
        "direction_print" : "Nur Deutsche hier. Du verstehst nichts aber du sprichst mit jemanden der nett aussieht. Nach der Unterhaltung verabschieddet er sich und gibt dir ein Geschenk",
        },
    "B5" : {
        "room_name" :"security",
        "coordinates" : (2,5),
        "object" : [False, False, False ,False],
        "possible_box_directions":["B6","to heal","quit"],
        "print_possible_answers" :["go main","to heal","quit"],
        "fight" : [True, "Security"], #90%
        "direction_print" : "Le mec de la secu t as vu et tu a l air trop suspect. Il t interroge",
        },
    "B6" : {
        "room_name" :"main_stage",
        "coordinates" : (2,6),
        "object" : [False, False, False ,False],
        "possible_box_directions":["to heal","quit"],
        "print_possible_answers" :["to heal","quit"],
        "fight" : [False],
        "direction_print" : "Enfin tu es arrive a la mainstage Profite bien de ton festival",
        },
}
start_position = "B1"