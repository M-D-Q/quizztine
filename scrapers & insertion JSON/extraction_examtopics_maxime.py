from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import *
from selenium.webdriver.chrome.options import Options
from functions_briefmenow import *

nom_questionnaire = "Exam-Topics 102-500 - Paywall breached"
liste_des_patterns = [r"<span.+>",r"</span>",r"(\n)|(\\n)", r"  [ ]*"]
f3 = open("sources\\102-500.txt.txt", "r", encoding="utf8")
liste_url = f3.readlines()
f3.close

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.implicitly_wait(3)
browser.maximize_window()

xpath_question = "/html/body/div[2]/div/div[3]/div/div[1]/div[2]/p"
xpath1 = "/html/body/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/ul/li[1]"
xpath2 = "/html/body/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/ul/li[2]"
xpath3 = "/html/body/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/ul/li[3]"
xpath4 = "/html/body/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/ul/li[4]"
xpath5 = "/html/body/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/ul/li[5]"
xpath_correct_answer = "/html/body/div[2]/div/div[3]/div/div[1]/div[2]/div[3]/span[1]/span"
a_revoir =[]

#Mettre un re.sub qui remplace les ([A-E]\. ) par un 1\\n
#Créer le truc d'insertion dans le json, notamment avec une mention pour les réponses sans input pour que je vienne les revoir plus tard
#concatener les keks via une liste ou pendant l'insertion JSON ? 
i=0
for url in liste_url:
    browser.get(url)
    question = []
    answer = "kek"
    try :
        question.append(browser.find_element(By.XPATH, value=xpath_question).text)
        question.append(browser.find_element(By.XPATH, value=xpath1).get_attribute('innerHTML'))
        question.append(browser.find_element(By.XPATH, value=xpath2).get_attribute('innerHTML'))
        question.append(browser.find_element(By.XPATH, value=xpath3).get_attribute('innerHTML'))
        question.append(browser.find_element(By.XPATH, value=xpath4).get_attribute('innerHTML'))
        browser.find_element(By.CSS_SELECTOR, "body > div.sec-spacer.pt-50 > div > div:nth-child(3) > div > div.discussion-header-container > div.question-body.mt-3.pt-3.border-top > a.btn.btn-primary.reveal-solution").click()
        answer = browser.find_element(By.XPATH, value=xpath_correct_answer).text
        
        try : 
            question.append(browser.find_element(By.XPATH, value=xpath5).get_attribute('innerHTML'))
            i+=1
        except : 
            print("oopsie, pas de rép E")
            question.append("")
            i+=1
        
        nettoyage_regex(liste_des_patterns, question)
        print(f"""{question[0]}
{question[1]}
{question[2]}
{question[3]}
{question[4]}
{question[5]}""")
        print(" QUESTION SUIVANTE ===============================")
    except :

        a_revoir.append(url)
        print(f"Procédure numéro : {liste_url.index(url)} : FAIL/A REVOIR")
    
        continue
    print("finito question")

    #INSERTION
    y = {
                            "id": i,
                            "question": f"{question[0]} \n{question[1]} \n{question[2]} \n{question[3]} \n{question[4]} \n{question[5]}",
                            "answer": answer,
                            "explanation": "A REMPLIR",
                            "url": url
                        }
    insertion_json(y, 'auto_christine.json', str(nom_questionnaire))
    print(f"Procédure numéro : {liste_url.index(url)}")

print(a_revoir)
