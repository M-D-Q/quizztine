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
from functions_briefmenow import *


nom_questionnaire = "Exam-Topics 101 - Paywall breached - Input"
liste_des_patterns = [r"<span.+>",r"</span>",r"(\n)|(\\n)", r"  [ ]*", r"FILL BLANK -"]
#f3 = open("sources\examtopics.txt", "r", encoding="utf8")
#liste_url = f3.readlines()
#f3.close
liste_url = ['https://www.examtopics.com/discussions/lpi/view/40524-exam-101-500-topic-1-question-6-discussion', 'https://www.examtopics.com/discussions/lpi/view/13313-exam-101-500-topic-1-question-11-discussion', 'https://www.examtopics.com/discussions/lpi/view/37582-exam-101-500-topic-1-question-15-discussion', 'https://www.examtopics.com/discussions/lpi/view/46441-exam-101-500-topic-1-question-41-discussion', 'https://www.examtopics.com/discussions/lpi/view/58859-exam-101-500-topic-1-question-59-discussion', 'https://www.examtopics.com/discussions/lpi/view/16429-exam-101-500-topic-1-question-63-discussion', 'https://www.examtopics.com/discussions/lpi/view/21716-exam-101-500-topic-1-question-76-discussion', 'https://www.examtopics.com/discussions/lpi/view/55355-exam-101-500-topic-1-question-85-discussion', 'https://www.examtopics.com/discussions/lpi/view/76875-exam-101-500-topic-1-question-111-discussion', 'https://www.examtopics.com/discussions/lpi/view/53593-exam-101-500-topic-1-question-119-discussion']

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.implicitly_wait(3)
browser.maximize_window()

xpath_question = "/html/body/div[2]/div/div[3]/div/div[1]/div[2]/p"
css_bouton_reponse= "body > div.sec-spacer.pt-50 > div > div:nth-child(3) > div > div.discussion-header-container > div.question-body.mt-3.pt-3.border-top > a.btn.btn-primary.reveal-solution"
xpath_correct_answer = "/html/body/div[2]/div/div[3]/div/div[1]/div[2]/div/span[1]/span"
i = 0
for url in liste_url:
    browser.get(url)
    question = []
    answer = "kek"
    i+=1
    try :
        question.append(browser.find_element(By.XPATH, value=xpath_question).text)

        browser.find_element(By.CSS_SELECTOR, value=css_bouton_reponse).click()
        question.append(browser.find_element(By.XPATH, value=xpath_correct_answer).get_attribute('innerHTML'))
    except: 
        print(f"Oopsie url n°{i}")

    nettoyage_regex(liste_des_patterns, question)

    #INSERTION
    y = {
                            "id": liste_url.index(url),
                            "question": question[0],
                            "answer": question[1],
                            "explanation": "A REMPLIR",
                            "url": url
                        }
    insertion_json(y, 'auto_christine.json', str(nom_questionnaire))
    print(f"Procédure numéro : {liste_url.index(url)}")