import re
from functions_briefmenow import *

def extraction_answers(txt_source,txt_cible, patterns_to_remove):
    f = open(txt_source, "r", encoding="utf8")
    linelist = f.readlines()
    f.close
    f2 = open(txt_cible, "w", encoding="utf8")
    i = 0
    for line in linelist:
        i += 1
        line = re.sub(r'(^[1-9][0-9]?\.)', r'£\1', line)
        line = re.sub(r'\"', r'\\"', line)
        for patternos in range(0,len(patterns_to_remove)): 
            pattern = patterns_to_remove[int(patternos)]
            for johnny in range(0, len(linelist)):
                linelist[int(johnny)] = re.sub(pattern, ' ', linelist[int(johnny)])
        f2.write(line)
        print(f"Ligne numéro : {i}")
    f2.close()


def formattage_insertion(clean_txt,noms_questionnaires, warning="RAS"):
    f3 = open(clean_txt, "r", encoding="utf8")
    linelist = f3.readlines()
    f3.close
    kek = ' '.join(linelist)
    kek1 = kek.split("£")
    i = 0
    chapitre_actuel = -1
    for x in range(0,len(kek1)) :
        try: 
            templist=[]
            templist = (kek1[int(x)].split(".", 2))
            templist[1] = templist[1].lstrip()
            for johnny in range(0, len(templist)):
                templist[int(johnny)] = re.sub("\\n ? ?", ' ', templist[int(johnny)])
                templist[int(johnny)] = re.sub(r"\\x0c", " ", templist[int(johnny)])
                templist[int(johnny)] = re.sub(r"  [ ]*", " ", templist[int(johnny)])
            templist[2] = str(templist[2])+" \n"
            i += 1
            if templist[0]== "1":
                chapitre_actuel += 1
                i = 1
            y = {
                    "id": str(i),
                    "question":" ",
                    "answer": str(templist[1]),
                    "explanation": str(templist[2])
                }
            insertion_json(y, 'auto_christine.json', str(noms_questionnaires[chapitre_actuel]))
            print(f"Procédure numéro : {i}")
        except Exception as e : 
            print(str(e))
            pass

################## QUESTIONS
def extraction_questions(txt_source,txt_cible, patterns_to_remove=[r"(.+)?Assessment Test(.+)?", r"  [ ]*", r"^(.+)?flast.+$", r"(\n)|(\\n)"]):
    f = open(txt_source, "r", encoding="utf8")
    linelist = f.readlines()
    f.close
    f2 = open(txt_cible, "w", encoding="utf8")
    i = 0
    for line in linelist:
        i += 1
        line = re.sub(r'([A-B-C-D-E]\.)', r"§\1", line)
        line = re.sub(r'^([ ]+)?([1-9][0-9]?\. )', r"£\2", line)
        line = re.sub(r'\"', r'\\"', line)
        for patternos in range(0,len(patterns_to_remove)): 
            pattern = patterns_to_remove[int(patternos)]
            for johnny in range(0, len(linelist)):
                linelist[int(johnny)] = re.sub(pattern, ' ', linelist[int(johnny)])
        f2.write(line)
        print(f"Ligne numéro : {i}")
    f2.close()

def formattage_1ststep(clean_txt):
    f3 = open(clean_txt, "r", encoding="utf8")
    linelist = [line for line in f3.readlines() if line.strip()]
    f3.close
    kek = ' '.join(linelist)
    kek1 = kek.split("£")
    kek1.pop(0)
    templist=[]
    for anything in range(0,len(kek1)):
        templist.append(re.sub(r'\n', r'', kek1[int(anything)]))
    return templist

def formattage_2ndstep_answer(liste,x) : 
    templist=[]
    templist = (liste[int(x)].split(". ", 2))
    templist[2] = str(templist[2])+" \n"
    return templist

def formattage_2nd_questions(liste,x):
    bob = re.sub("§", r"\n ", liste[int(x)])
    bob = re.sub(r"(^[0-9]?[0-9]\.[ ]+)", r"", liste[int(x)])
    return bob

def formattage_3_questions(clean_text_questions):
    liste = formattage_1ststep(clean_text_questions)
    x = 0
    templist_questions = []
    for x in range(0,len(liste)):
        templist_questions.append(formattage_2nd_questions(liste,x))
    return templist_questions

def pre_insertion(liste_questions, templist_answers, x, nom_questionnaire):
    y = {
                "id": str(templist_answers[0]),
                "question": str(re.sub("§", r"\n ", liste_questions[int(x)])),
                "answer": str(templist_answers[1]),
                "explanation": str(templist_answers[2]),
            }
    insertion_json(y, 'auto_christine.json', nom_questionnaire)

def tous_ensemble_assessment(clean_text_questions, clean_text_answers, nom_questionnaire="questionnairetest"):
    liste_questions = formattage_3_questions(clean_text_questions)
    liste_answers = formattage_1ststep(clean_text_answers)
    x = 0
    for x in range(0,len(liste_answers)) :
        templist_answers = formattage_2ndstep_answer(liste_answers,x)
        pre_insertion(liste_questions, templist_answers, x, nom_questionnaire)
    print("finito")

def tous_ensemble_general(clean_text_questions, clean_text_answers, noms_questionnaires):
    liste_questions = formattage_3_questions(clean_text_questions)
    liste_answers = formattage_1ststep(clean_text_answers)
    x = 0
    chapitre_actuel = -1
    for x in range(0,len(liste_answers)) :
        templist_answers = formattage_2ndstep_answer(liste_answers,x)
        if templist_answers[0]== "1":
                chapitre_actuel += 1
        pre_insertion(liste_questions, templist_answers, x, noms_questionnaires[int(chapitre_actuel)])
    print("finito")

    def formattage_insertion(clean_txt,noms_questionnaires, warning="RAS"):
        f3 = open(clean_txt, "r", encoding="utf8")
        linelist = f3.readlines()
        f3.close
        kek = ' '.join(linelist)
        kek1 = kek.split("£")
        i = 0
        chapitre_actuel = -1
        for x in range(0,len(kek1)) :
            try: 
                templist=[]
                templist = (kek1[int(x)].split(".", 2))
                templist[1] = templist[1].lstrip()
                for johnny in range(0, len(templist)):
                    templist[int(johnny)] = re.sub("\n ? ?", ' ', templist[int(johnny)])
                    templist[int(johnny)] = re.sub(r"\\x0c", " ", templist[int(johnny)])
                    templist[int(johnny)] = re.sub(r"  [ ]*", " ", templist[int(johnny)])
                templist[2] = str(templist[2])+" \n"
                i += 1
                if templist[0]== "1":
                    chapitre_actuel += 1
                    i = 1
                y = {
                        "id": str(i),
                        "question":" ",
                        "answer": str(templist[1]),
                        "explanation": str(templist[2])
                    }
                insertion_json(y, 'auto_christine.json', str(noms_questionnaires[chapitre_actuel]))
                print(f"Procédure numéro : {i}")
            except Exception as e : 
                print(str(e))
                pass