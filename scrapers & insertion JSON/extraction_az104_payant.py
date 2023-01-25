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
def recup_question_noimage(card_exam_question_card):
    text_question = card_exam_question_card.find_element(By.CLASS_NAME,value="card-text").text
    print(text_question)
    options_question = card_exam_question_card.find_element(By.CLASS_NAME,value="question-choices-container")
    options = options_question.find_elements(By.TAG_NAME,value="li")
    for option in options:
        print(option.text)
    right_answer = card_exam_question_card.find_element(By.CLASS_NAME,value="correct-answer").get_attribute('innerHTML')
    print("right answer ====="+right_answer)
    explanation = card_exam_question_card.find_element(By.CLASS_NAME,value="answer-description").get_attribute('innerHTML')
    print("explanation ====="+explanation)

# NO NEED titre sujet 1 : /html/body/div[3]/div/div[3]/div/div[1]/div[1]/div/h2
#numero question + topic : /html/body/div[3]/div/div[3]/div/div[1]/div[2]/div[1]
# txt question /html/body/div[3]/div/div[3]/div/div[1]/div[2]/div[2]/p[1]
# option A /html/body/div[3]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[1] ||| document.querySelector("body > div.sec-spacer > div > div:nth-child(3) > div > div.questions-container > div:nth-child(2) > div.card-body.question-body > div > ul > li:nth-child(1)")
           #/html/body/div[3]/div/div[3]/div/div[1]/div[3]/div[2]/div/ul/li[1]       document.querySelector("body > div.sec-spacer > div > div:nth-child(3) > div > div.questions-container > div:nth-child(3) > div.card-body.question-body > div > ul > li:nth-child(1)")
            #/html/body/div[3]/div/div[3]/div/div[1]/div[359]/div[2]/div/ul/li[1]
            #/html/body/div[3]/div/div[3]/div/div[1]/div[464]/div[2]/div/ul/li[1]
            #/html/body/div[3]/div/div[3]/div/div[1]/div[21]
            #document.querySelector("body > div.sec-spacer > div > div:nth-child(3) > div > div.questions-container > div:nth-child(21)")
#B /html/body/div[3]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[2]
#C /html/body/div[3]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[3]
#D /html/body/div[3]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[4]
#ANSWER : /html/body/div[3]/div/div[3]/div/div[1]/div[2]/div[2]/p[2]/span[1]/span

# En fait il faut commencer par itérer par toute les questions. 
all_questions = browser.find_elements(By.CLASS_NAME, value="exam-question-card")

for element_miaou in all_questions :
    if element_miaou.find_elements(By.TAG_NAME,value="img"):
        print("celle là à une image")
    else :
        print("pas d'image")
        recup_question_noimage(element_miaou)

#putain faut juste recup les text et 

#buttons & shit for custom view:
    
    #BOUTON CUSTOM VIEW# body > div.sec-spacer > div > div:nth-child(2) > div > a OU /html/body/div[3]/div/div[2]/div/a
    #Not needed probably # CHECK show range 1-455 # #question-range-checkbox OU /html/body/div[3]/div/div/div[2]/div/div/div[2]/form/div[2]/input ||CLICK
    #SLIDER DE PAGES # /html/body/div[3]/div/div/div[2]/div/div/div[2]/form/div[1]/input  # #QuestionCount # document.querySelector("#QuestionCount")
    # pour le slider de page, son id = QuestionCount, on peut essayer : 
    # driver.findElement(By.id("invoice_supplier_id")).sendKeys("value"‌​, "new value");     https://stackoverflow.com/questions/35127108/how-to-set-value-to-input-web-element-using-selenium
    #SET SESSION SETTINGS # body > div.sec-spacer > div > div > div:nth-child(2) > div > div > div.card-body > form > span > button.btn.btn-primary #OU# /html/body/div[3]/div/div/div[2]/div/div/div[2]/form/span/button[1]
    pass






#nom du questionnaire pour ajout dans le JSON (string)


#Liste des patterns regex à supprimer des textes extraits (list)

#chemin vers le conteneur à question
#body > div.sec-spacer > div > div:nth-child(3) > div > div.questions-container