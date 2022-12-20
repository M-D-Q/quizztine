import json
import os
import random
def insertion_json(new_data, nom_fichier,nom_questionnaire):
        with open(nom_fichier,'r+', encoding="utf8") as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data[nom_questionnaire]= new_data[nom_questionnaire]
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
def update_user_score(questionnaire_name, score, datajson):
    found = False
    i = 0
    cles = datajson["score"].keys()
    cles = list(cles)
    while not found and i < len(cles):
        found = cles[i] == questionnaire_name
        if found :
            datajson["score"][cles[i]] = score
        i+=1
    if not found:
        datajson["score"][questionnaire_name] = score
    insertion_json(datajson,"auto_christine.json","score" )
def show_it(liste_quest, data):
    clefs = list(data['score'].keys())
    for x in range(0, len(liste_quest)):
        if liste_quest[x] in clefs :
            print(f"{x} - {liste_quest[x]} =^_^= Score actuel : {data['score'][liste_quest[x]]}%")
        else : 
            print(f"{x} - {liste_quest[x]} =^_^= Score actuel : Nothing yet..")



#choix questionnaire entier ou shuffle de 25 questions (avec un timer ?)
def shuffle_oupas(data, liste_quest, choix_second):
    choix_shuffle = input("""
    1 - Dump entier (randomisé)
    2 - 25 questions randoms provenant du dump
    --> """)
    if choix_shuffle == 1:
        liste_utilisee = data[liste_quest[int(choix_second)]]
        random.shuffle(liste_utilisee)
        liste_utilisee.append(str(liste_quest[int(choix_second)]))
        return liste_utilisee
    else:
        liste_utilisee = data[liste_quest[int(choix_second)]]
        random.shuffle(liste_utilisee)
        liste_utilisee = liste_utilisee[:25]
        liste_utilisee.append("Questionnaire_Shuffle")
        return liste_utilisee

def deroulement_questionnaire(liste_quest, data):
    print("What dump do you want to study :")
    show_it(liste_quest, data)
    choix_second = input("Enter chosen number here -> ")
    score = 0
    i = 0
    liste_utilisee = shuffle_oupas(data, liste_quest, choix_second)
    nom_questionnaire_k = liste_utilisee[-1]
    liste_utilisee.pop()
    print(len(liste_utilisee))
    for john in liste_utilisee:
        print(f"Question # {liste_utilisee.index(john)}/{len(liste_utilisee)}")
        print(john['question'])
        response = str(input("""
Your answer is (no spaces, no commas, only capital letters) :
--> """)).upper()
        if response != john['answer'].upper():
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
        current_score = int((score/i)*100)
        print(f"Current score : {current_score}%")
        osef = input("Press enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
    print(f"impression du famoso score final de {current_score}% ")
    update_user_score(nom_questionnaire_k,current_score, data)
