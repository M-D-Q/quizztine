import json
import os
import time

#TO DO : ajouter ascii art, sound "lets get started"
# ajouter score dans le json
# ajouter menu choix du chapitre avec score atteint par chapitre aussi
# 

with open ("auto_christine.json", "r", encoding='utf-8') as dico:
    dataset = dico.read()
    data = json.loads(dataset)

choix = str(input("""What do you you want to study ?
1 = Chapitre 1
2 = Dump de 2018"""))

if choix == "1" :
    score = 0
    i = 0
    for john in data['chapitre1']:
        print(f"Question #{john['id']}/{len(data['chapitre1'])}")
        print(john['question'])
        response = str(input("Your answer is (no spaces, only capital letters. Ex : 'B' or 'B,C,D') :"))
        if response != john['answer']:
            print(f" Incorrect, the answer was {john['answer']} ! Here are some explanations : {john['explanation']} ")
        else : 
            print(f"""Well done ! {response} is correct ! Still, here are some explanations : 
    {john['explanation']} """)
            score += 1
        i += 1
        print(f"Current score : {int((score/i)*100)}%")
        osef = input("Press enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
elif choix == "2":
    score = 0
    i = 0
    for john in data['questionnaire2018']:
        print(f"Question #{john['id']}/{len(data['questionnaire2018'])}")
        print(john['question'])
        response = str(input("Your answer is (no spaces, only capital letters. :"))
        if response != john['answer']:
            print(f" Incorrect, the answer was {john['answer']} !")
        else : 
            print(f"""Well done ! {response} is correct ! """)
            score += 1
        i += 1
        print(f"Current score : {int((score/i)*100)}%")
        osef = input("Press enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

    #ICI faire une variante pour le questionnaire à input, en mettant une liste des réponses possibles via un split à la virgule des trucs avec plusieurs variantes, puis un if response in liste_answers

    # AUSSI , Variante shuffle avec 20 fois un chiffre random qui fetch l'id du même chiffre et on évite que ça se répète.

    # Et de l'esthétique bien sur.

    

