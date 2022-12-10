import re
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver import *
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.options import Options

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
        liste_occurences[int(john)] = str(liste_occurences[int(john)])[3:]

def mettage_answers(liste_occurences, liste_answers, nbquestion,liste_patterns): ###
    templist1=[]
    for chocolat in range(0, len(liste_occurences)):
        if "font color" in liste_occurences[int(chocolat)]:
            templist1.append(liste_occurences[int(chocolat)])
    nettoyage_regex(liste_patterns, templist1)
    gardage_premiere_lettre(templist1)
    liste_answers[nbquestion] = templist1

def by_splitting(liste_occurences):
    liste_occurences = str(liste_occurences[0]).split(", ")

def mettage_answers_libre(liste_occurences, liste_answers, nbquestion,liste_patterns): ###
    templist1=[]
    for chocolat in range(0, len(liste_occurences)):
        if "font color" in liste_occurences[int(chocolat)]:
            templist1.append(liste_occurences[int(chocolat)])
    nettoyage_regex(liste_patterns, templist1)
    elimination_premierelettre(templist1)
    #by_splitting(templist1)
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

def pop_derniere_occurence(liste_occurences): 
    liste_occurences.pop()

def check_if_comments(browser):
    browser.implicitly_wait(0)
    if len(browser.find_elements(By.XPATH, value="/html/body/div/div/section/div[2]/div[1]/h2")) != 0 :
        browser.implicitly_wait(3)
        return True
    else : 
        browser.implicitly_wait(3)
        return False

def wrapping_normal(liste_occurences, dict_answers, nbquestion, liste_patterns, browser, nom_questionnaire, explanation="", typedequestion="choix"): 
    mettage_answers(liste_occurences, dict_answers, nbquestion, liste_patterns)
    print(dict_answers)
    nettoyage_regex(liste_patterns, liste_occurences)
    ajout_sautligne(liste_occurences)
    print(liste_occurences)
    if check_if_comments(browser) == True : 
        warning = "COMMENTS ON THE WEBSITE, PLEASE REVIEW MANUALLY"
    else :
        warning = "All appears to be good"
    y = {
              "id":nbquestion,
              "question":(' '.join(liste_occurences)),
              "answer":(','.join(dict_answers[nbquestion])),
              "explanation":str(explanation),
              "url":str(browser.current_url),
              "warning":str(warning),
              "type":str(typedequestion)
          }
    insertion_json(y, 'auto_christine.json', nom_questionnaire)

def wrapping_input(liste_occurences, dict_answers, nbquestion, liste_patterns, browser, nom_questionnaire, explanation="", typedequestion="input"): 
    mettage_answers_libre(liste_occurences, dict_answers, nbquestion, liste_patterns)
    print(dict_answers)
    nettoyage_regex(liste_patterns, liste_occurences)
    ajout_sautligne(liste_occurences)
    pop_derniere_occurence(liste_occurences)
    print(liste_occurences)
    if check_if_comments(browser) == True : 
        warning = "COMMENTS ON THE WEBSITE, PLEASE REVIEW MANUALLY"
    else :
        warning = "All appears to be good"

    y = {
              "id":nbquestion,
              "question":(' '.join(liste_occurences)),
              "answer":(','.join(dict_answers[nbquestion])),
              "explanation":str(explanation),
              "url":str(browser.current_url),
              "warning":str(warning),
              "type":str(typedequestion)
          }
    insertion_json(y, 'auto_christine.json',nom_questionnaire)

#mettage_answers(liste_occurences2, liste_answers, nbquestion)
#print(liste_answers)
#nettoyage_regex(liste_patterns2, liste_occurences2)
#print(liste_occurences2)