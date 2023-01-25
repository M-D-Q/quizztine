from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import *
from selenium.webdriver.chrome.options import Options
from functions_briefmenow import *
from time import sleep 
#setup webdriver
chrome_options = Options()

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.implicitly_wait(3)
browser.maximize_window()

#get l'url de base :
base_url = "https://www.examtopics.com/exams/microsoft/az-104/custom-view/"
browser.get(base_url)

#login
username = "sliman.derrouiche@hotmail.fr"
password = "CAP2023"
#browser.find_element(By.NAME, "email").send_keys("sliman.derrouiche@hotmail.fr")
#browser.find_element(By.NAME, "password").send_keys("CAP2023")
browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/div/input").send_keys(username)
browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/div[1]/input").send_keys(password)
browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/button").click()

#cheminement pour activer la vue en 455 (apparement ça met 228, good enough)
browser.find_element(By.ID, "QuestionCount").send_keys("455")
browser.find_element(By.ID, "QuestionCount").click()
browser.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(1)").click()

#maintenant, recup le texte d'une question
def recup_question_inputable(card_exam_question_card):
    titre_question = card_exam_question_card.find_element(By.CLASS_NAME,value="card-header").text
    text_question = card_exam_question_card.find_element(By.CLASS_NAME,value="card-text").get_attribute('innerHTML')
    options_question = card_exam_question_card.find_element(By.CLASS_NAME,value="question-choices-container").get_attribute('innerHTML')
    inputable_answer = card_exam_question_card.find_element(By.CLASS_NAME,value="correct-answer").text
    answer_and_explanation = card_exam_question_card.find_element(By.CLASS_NAME,value="correct-answer").get_attribute('innerHTML')+" \n <br>"+card_exam_question_card.find_element(By.CLASS_NAME,value="answer-description").get_attribute('innerHTML')
    liste_html = [titre_question, text_question, options_question, inputable_answer, answer_and_explanation]
    return liste_html
    #WARNING DES FOIS YA RIEN QUI SORT POUR LE INPUTABLE ANSWER : visiblement le '.text' ne fait pas toujours le taf, faudra peut etre juste prendre le inner html et laver ça au regex.

def recup_question_non_inputable(card_exam_question_card):
    pass

# En fait il faut commencer par itérer par toute les questions. 
all_questions = browser.find_elements(By.CLASS_NAME, value="exam-question-card")
liste_contenu_inputables = [] #ce sera une liste de liste contenants tt les colonnes
for element_miaou in all_questions :
    je_check_juste_un_truc = element_miaou.find_element(By.CLASS_NAME,value="correct-answer")

    if je_check_juste_un_truc.find_elements(By.TAG_NAME,value="img"):
        print("voici une où la réponse est une image")
        recup_question_non_inputable(element_miaou)
    else :
        print("et là c'est une lettre")
        liste_contenu_inputables.append(recup_question_inputable(element_miaou))
        print(liste_contenu_inputables)

#trouver un moyen d'exporter la liste au cas où ça merde
####Miaou

#insérer dans la ddb : bon exemple d'insertion toute faite
"""
questionnaire_name = "AZ-104 Everything"
new_questionnaire = Questionnaires(name=questionnaire_name)
db.session.add(new_questionnaire)
db.session.commit()
    # Iterate through the questions in the list
for item in liste_contenu_inputables :
    # Create a new instance of the Questions model and add it to the session
    new_question = QuestionsHTML(question_name=item[1],
                                question_html=item[2],
                                options_html=item[3],
                                answer=item[4],
                                answer_html=item[5],
                                master_questionnaire=new_questionnaire.id)
    db.session.add(new_question)
db.session.commit()
"""





#nom du questionnaire pour ajout dans le JSON (string)


#Liste des patterns regex à supprimer des textes extraits (list)

#chemin vers le conteneur à question
#body > div.sec-spacer > div > div:nth-child(3) > div > div.questions-container