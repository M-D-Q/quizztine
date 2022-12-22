from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from functions_briefmenow import *


nom_questionnaire = "Exam-Topics 102-500 - Paywall breached - Input"
liste_des_patterns = [r"<span.+>",r"</span>",r"(\n)|(\\n)", r"  [ ]*", r"FILL BLANK -"]
#f3 = open("sources\examtopics.txt", "r", encoding="utf8")
#liste_url = f3.readlines()
#f3.close
liste_url = ['https://www.examtopics.com/discussions/lpi/view/21612-exam-102-500-topic-1-question-1-discussion', 'https://www.examtopics.com/discussions/lpi/view/30142-exam-102-500-topic-1-question-3-discussion', 'https://www.examtopics.com/discussions/lpi/view/19422-exam-102-500-topic-1-question-4-discussion', 'https://www.examtopics.com/discussions/lpi/view/14530-exam-102-500-topic-1-question-19-discussion', 'https://www.examtopics.com/discussions/lpi/view/30087-exam-102-500-topic-1-question-27-discussion', 'https://www.examtopics.com/discussions/lpi/view/30089-exam-102-500-topic-1-question-29-discussion', 'https://www.examtopics.com/discussions/lpi/view/19528-exam-102-500-topic-1-question-33-discussion', 'https://www.examtopics.com/discussions/lpi/view/14851-exam-102-500-topic-1-question-34-discussion', 'https://www.examtopics.com/discussions/lpi/view/30151-exam-102-500-topic-1-question-37-discussion', 'https://www.examtopics.com/discussions/lpi/view/42189-exam-102-500-topic-1-question-46-discussion', 'https://www.examtopics.com/discussions/lpi/view/66389-exam-102-500-topic-1-question-54-discussion', 'https://www.examtopics.com/discussions/lpi/view/14246-exam-102-500-topic-1-question-55-discussion', 'https://www.examtopics.com/discussions/lpi/view/30159-exam-102-500-topic-1-question-64-discussion', 'https://www.examtopics.com/discussions/lpi/view/29920-exam-102-500-topic-1-question-71-discussion', 'https://www.examtopics.com/discussions/lpi/view/29921-exam-102-500-topic-1-question-87-discussion', 'https://www.examtopics.com/discussions/lpi/view/29922-exam-102-500-topic-1-question-88-discussion', 'https://www.examtopics.com/discussions/lpi/view/30423-exam-102-500-topic-1-question-90-discussion', 'https://www.examtopics.com/discussions/lpi/view/66813-exam-102-500-topic-1-question-94-discussion', 'https://www.examtopics.com/discussions/lpi/view/30182-exam-102-500-topic-1-question-102-discussion', 'https://www.examtopics.com/discussions/lpi/view/30616-exam-102-500-topic-1-question-107-discussion', 'https://www.examtopics.com/discussions/lpi/view/29996-exam-102-500-topic-1-question-118-discussion']

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
    answer = []
    i+=1
    try :
        question.append(browser.find_element(By.XPATH, value=xpath_question).text)

        browser.find_element(By.CSS_SELECTOR, value=css_bouton_reponse).click()
        answer.append(browser.find_element(By.XPATH, value=xpath_correct_answer).get_attribute('innerHTML'))
    except: 
        print(f"Oopsie url n°{i}")

    nettoyage_regex(liste_des_patterns, question)

    #INSERTION
    y = {
                            "id": liste_url.index(url),
                            "question": question[0],
                            "answer": answer,
                            "explanation": "A REMPLIR",
                            "url": url
                        }
    insertion_json(y, 'auto_christine.json', str(nom_questionnaire))
    print(f"Procédure numéro : {liste_url.index(url)}")