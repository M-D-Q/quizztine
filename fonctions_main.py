import json
import os
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
    print(cles)
    while not found and i < len(cles):
        found = cles[i] == questionnaire_name
        if found :
            datajson["score"][cles[i]] = score
        i+=1
    if not found:
        print("not found")
        datajson["score"][questionnaire_name] = score
    insertion_json(datajson,"auto_christine.json","score" )
def show_it(liste_quest, data):
    clefs = list(data['score'].keys())
    for x in range(0, len(liste_quest)):
        if liste_quest[x] in clefs :
            print(f"{x} - {liste_quest[x]} =^_^= Score actuel : {data['score'][liste_quest[x]]}%")
        else : 
            print(f"{x} - {liste_quest[x]} =^_^= Score actuel : Nothing yet..")
def deroulement_questionnaire(liste_quest, data):
    print("What dump do you want to study :")
    show_it(liste_quest, data)
    choix_second = input("Enter chosen number here -> ")
    score = 0
    i = 0
    for john in data[liste_quest[int(choix_second)]]:
        print(f"Question # {data[liste_quest[int(choix_second)]].index(john)}/{len(data[liste_quest[int(choix_second)]])}")
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
    update_user_score(liste_quest[int(choix_second)],current_score, data)
