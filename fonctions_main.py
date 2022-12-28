import json
import os
import random
import re
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
    choix_shuffle = str(input("""
    1 - Dump entier (randomisé)
    2 - 25 questions randoms provenant du dump
    --> """))
    if choix_shuffle == "1":
        liste_utilisee = data[liste_quest[int(choix_second)]]
        random.shuffle(liste_utilisee)
        liste_utilisee.append(str(liste_quest[int(choix_second)]))
        return liste_utilisee
    elif choix_shuffle == "2":
        liste_utilisee = data[liste_quest[int(choix_second)]]
        random.shuffle(liste_utilisee)
        liste_utilisee = liste_utilisee[:25]
        liste_utilisee.append("Questionnaire_Shuffle")
        return liste_utilisee
    else : 
        print("Entre un chiffre valide stp")
        exit

def get_response(pattern):
    user_input = str(input("""
Your answer is (no spaces, no commas, only capital letters) :
--> """))
    match = re.fullmatch(pattern,user_input)
    while match is None:
        print("Invalid answer format, please try again.")
        user_input = str(input("""
Your answer is (no spaces, no commas, only capital letters) :
--> """))
        match = re.fullmatch(pattern, user_input)
    return user_input

def question_result_string(john, response, score):
    if response.upper() != john['answer'] :
        print(f"""
Incorrect, the answer was {john['answer']} !
            """)
        if john['explanation'] != "":
            print(f"""
Some explanation : {john['explanation']}
""")
    elif response.upper() == john['answer'] : 
        print(f"""
Well done ! {response} is correct ! 
            """)
        if john['explanation'] != "":
            print(f"""
Some explanation :
{john['explanation']}
""")
        return True

def question_result_list(john, response, score):
    if response not in john['answer'] :
        print(f"""
Incorrect, the answer was {" OR ".join(john['answer'])} !
            """)
        if john['explanation'] != "":
            print(f"""
Some explanation : {john['explanation']}
""")
    elif response in john['answer'] :   
        print(f"""
Well done ! {response} is correct ! 
""")
        if len(john['answer']) > 1 :
                print(f"""
All possible answers were : {" || ".join(john['answer'])}""")
        if john['explanation'] != "":
                print(f"""
Some explanation :
{john['explanation']}
""")
        return True

def deroulement_questionnaire(liste_quest, data):
    print("What dump do you want to study :")
    show_it(liste_quest, data)
    choix_second = input("Enter chosen number here -> ")
    score = 0
    i = 0
    liste_utilisee = shuffle_oupas(data, liste_quest, choix_second)
    nom_questionnaire_k = liste_utilisee[-1]
    liste_utilisee.pop()
    for john in liste_utilisee:
        print(f"Question # {liste_utilisee.index(john)}/{len(liste_utilisee)}")
        print(john['question'])
        if type(john['answer']) != list:
            response = get_response("[A-E][A-E]?[A-E]?")
            if question_result_string(john, response, score):
                score += 1
        elif type(john['answer']) == list :
            response = get_response(".+")
            if question_result_list(john, response, score) :
                score += 1 
        i += 1
        current_score = int((score/i)*100)
        print(f"Current score : {current_score}%")
        mark_or_pass = input("Press enter to continue...")
        if mark_or_pass == "X" or "x" : 
            #mettre l'id de la question/explication à revoir dans une liste ou un dico dans un fichier txt ou autre.
            print("placeholder")
        os.system('cls' if os.name == 'nt' else 'clear')
    print(f"impression du famoso score final de {current_score}% ")
    update_user_score(nom_questionnaire_k,current_score, data)
