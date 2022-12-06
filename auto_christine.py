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

