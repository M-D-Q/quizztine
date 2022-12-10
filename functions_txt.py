import re
import json
from functions_briefmenow import *

def extraction_assessment(txt_source,txt_cible, patterns_to_remove):
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

def formattage_insertion_assessment(clean_txt,nom_questionnaire="Assessment Test"):
    f3 = open(clean_txt, "r", encoding="utf8")
    linelist = f3.readlines()
    f3.close
    kek = ' '.join(linelist)
    kek1 = kek.split("£")
    i = 0
    for x in range(0,len(kek1)) :
        try: 
            templist=[]
            templist = (kek1[int(x)].split(". ", 2))
            templist[2] = str(templist[2])+" \n"
            i += 1
            print(templist)
            y = {
                    "id": str(templist[0]),
                    "question":" ",
                    "answer": str(templist[1]),
                    "explanation": str(templist[2]),
                }
            insertion_json(y, 'auto_christine.json', nom_questionnaire)
        except Exception as e : 
            print(e)
            pass

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



