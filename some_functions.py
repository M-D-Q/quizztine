import re
import json
###liste_patterns2 =['<br>','<font color="#333333">', '</font>', '<span.+span>']
#kek1 = "A.<br> /proc/keys"
#kek2 = """B.<br><font color="#333333"> /etc/inittab</font>"""
#kek3 = "C.<br> /proc/inittab font color"
#kek4 = "D.<br> /etc/reboot"
#liste_occurences2 = [kek1, kek2, kek3, kek4]
#liste_answers = {}

def nettoyage_regex(liste_patterns,liste_occurences):
    for chocolat in range(0, len(liste_patterns)):
        pattern = liste_patterns[int(chocolat)]
        for johnny in range(0, len(liste_occurences)):
            liste_occurences[int(johnny)] = re.sub(pattern, '', liste_occurences[int(johnny)])
        #print("Nettoyage numero "+str(johnny)+" avec pattern numéro "+str(chocolat))

def gardage_premiere_lettre(liste_occurences):
    for john in range(0, len(liste_occurences)):
        liste_occurences[int(john)] = str(liste_occurences[int(john)])[:1]
 
def elimination_premierelettre(liste_occurences):
    for john in range(0, len(liste_occurences)):
        liste_occurences[int(john)] = str(liste_occurences[int(john)])[2:]

def mettage_answers(liste_occurences, liste_answers, nbquestion,liste_patterns): ###
    templist1=[]
    for chocolat in range(0, len(liste_occurences)):
        if "font color" in liste_occurences[int(chocolat)]:
            templist1.append(liste_occurences[int(chocolat)])
    nettoyage_regex(liste_patterns, templist1)
    gardage_premiere_lettre(templist1)
    liste_answers[nbquestion] = templist1   

def by_splitting(liste_occurences):
    for chocolat in range(0, len(liste_occurences)):
        liste_occurences = liste_occurences[int(chocolat)].split(", ")

def mettage_answers_libre(liste_occurences, liste_answers, nbquestion,liste_patterns): ###
    templist1=[]
    for chocolat in range(0, len(liste_occurences)):
        if "font color" in liste_occurences[int(chocolat)]:
            templist1.append(liste_occurences[int(chocolat)])
    nettoyage_regex(liste_patterns, templist1)
    elimination_premierelettre(templist1)
    by_splitting(templist1)
    liste_answers[nbquestion] = templist1 

def ajout_sautligne(liste_occurences):
    for chocolat in range(0, len(liste_occurences)):
        liste_occurences[int(chocolat)] = str(liste_occurences[int(chocolat)])+" \n"

def insertion_json(new_data, nom_fichier,nom_questionnaire):
        with open(nom_fichier,'r+', encoding="utf8") as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data[nom_questionnaire].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)


def wrapping_normal(liste_occurences, dict_answers, nbquestion, liste_patterns): 
    mettage_answers_libre(liste_occurences, dict_answers, nbquestion, liste_patterns)
    print(dict_answers)
    nettoyage_regex(liste_patterns, liste_occurences)
    ajout_sautligne(liste_occurences)
    print(liste_occurences)
    y = {
              "id":nbquestion,
              "question":(' '.join(liste_occurences)),
              "answer":(','.join(dict_answers[nbquestion])),
              "explanation":" "
          }
    insertion_json(y, 'auto_christine.json',"questionnaire2018")

def wrapping_input(liste_occurences, dict_answers, nbquestion, liste_patterns): 
    mettage_answers(liste_occurences, dict_answers, nbquestion, liste_patterns)
    print(dict_answers)
    nettoyage_regex(liste_patterns, liste_occurences)
    ajout_sautligne(liste_occurences)
    print(liste_occurences)
    y = {
              "id":nbquestion,
              "question":(' '.join(liste_occurences)),
              "answer":(','.join(dict_answers[nbquestion])),
              "explanation":" "
          }
    insertion_json(y, 'auto_christine.json',"questionnairelibre")

#mettage_answers(liste_occurences2, liste_answers, nbquestion)
#print(liste_answers)
#nettoyage_regex(liste_patterns2, liste_occurences2)
#print(liste_occurences2)