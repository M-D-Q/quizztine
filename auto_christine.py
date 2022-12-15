import json
import os
import time

#TO DO : ajouter ascii art, sound "lets get started"
# ajouter score dans le json
# ajouter menu choix du chapitre avec score atteint par chapitre aussi


with open ("auto_christine.json", "r", encoding='utf-8') as dico:
    dataset = dico.read()
    data = json.loads(dataset)

liste_questionnaires_book = ["Assessment Test", "Chapter 1: Exploring Linux Command-Line Tools", "Chapter 2: Managing Software", "Chapter 3: Configuring Hardware", "Chapter 4: Managing Files",
"Chapter 5: Booting Linux and Editing Files", "Chapter 6: Configuring the X Window System, Localization, and Printing", "Chapter 7: Administering the System"]
# WORKING ON IT "Chapter 8: Configuring Basic Networking", "Chapter 9: Writing Scripts, Configuring Email, and Using Databases", "Chapter 10: Securing Your System"

liste_questionnaires_dumps = ["LX0-103(v.1)", "101-400(v.2)", "101-350", "Exam-Topics 101 - Paywall breached (w/ explanations)", "Exam-Topics 101 - Paywall breached - Version Large (w/ explanations)"]

def show_it(liste_quest):
    for x in range(0, len(liste_quest)):
        print(f"{x} - {liste_quest[x]}")

choix = str(input("""
What do you want to study ?
0 - Assessment Test & Chapters w/ explanations from LPIC-1 Study Guide book ?
1 - Dumps questionnaires - Choice answers

Enter chosen number here ->"""))

if choix == "0" :
    print("What Chapter  do you want to study :")
    show_it(liste_questionnaires_book)
    choix = str(input("Enter chosen number here -> "))
    score = 0
    i = 0
    for john in data[liste_questionnaires_book[int(choix)]]:
        print(f"Question #{john['id']}/{len(data[liste_questionnaires_book[int(choix)]])}")
        print(john['question'])
        response = str(input("Your answer is (only capital letters, no commas, no spaces) :"))
        if response != john['answer']:
            print(f""" 
            
    Incorrect, the answer was {john['answer']} ! 
            
    Here are some explanations : 
            
    {john['explanation']} """)
        else : 
            print(f"""Well done ! {response} is correct ! 

    =============================================== Explanations : 

    {john['explanation']} """)
            score += 1
        i += 1
        print(f"Current score : {int((score/i)*100)}%")
        osef = input("Press enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')


elif choix == "1":
    print("What dump do you want to study :")
    show_it(liste_questionnaires_dumps)
    choix = str(input("Enter chosen number here -> "))
    score = 0
    i = 0
    for john in data[liste_questionnaires_dumps[int(choix)]]:
        print(f"Question #{john['id']}/{len(data[liste_questionnaires_dumps[int(choix)]])}")
        print(john['question'])
        response = str(input("""
Your answer is (no spaces, no commas, only capital letters) :
--> """))
        if response != john['answer']:
            print(f"""
Incorrect, the answer was {john['answer']} !
             """)
            if john ['explanation'] != "":
                print(f"""
Some explanation : {john['explanation']}
""")
            try : 
                print(f"""
    
Fiabilité de la réponse : {john['warning']}
URL : {john['url']})
            """)
            except : 
                pass
        else : 
            print(f"""
Well done ! {response} is correct ! 
            """)
            if john ['explanation'] != "":
                print(f"""
Some explanation : {john['explanation']}
""")
            try : 
                print(f"""
                
Fiabilité de la réponse : {john['warning']}
URL : {john['url']})
            """)
            except : 
                pass
            score += 1
        i += 1
        print(f"Current score : {int((score/i)*100)}%")
        osef = input("Press enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

#elif choix == "2000":
#   score = 0
 #   i = 0
  #  
#elif choix == "3000":
  #  score = 0
   # i = 0
   # for john in data['questionnairelibre']:
      #  print(f"Question #{john['id']}/{len(data['questionnairelibre'])}")
      #  print(john['question'])
      #  response = str(input("Input answer : "))
      #  if response in john['answer'].split(", "):
       #     print(f"""Well done ! {response} is correct !
        #    You could have answered any of these : {john['answer']}""")
       # else : 
      #      print(f" Incorrect, the answer was any of these : {john['answer']}")
     #       score += 1
     #   i += 1
       # print(f"Current score : {int((score/i)*100)}%")
       # osef = input("Press enter to continue...")
       # os.system('cls' if os.name == 'nt' else 'clear')


    #ICI faire une variante pour le questionnaire à input, en mettant une liste des réponses possibles via un split à la virgule des trucs avec plusieurs variantes, puis un if response in liste_answers

    # AUSSI , Variante shuffle avec 20 fois un chiffre random qui fetch l'id du même chiffre et on évite que ça se répète.

    # Et de l'esthétique bien sur.

    

