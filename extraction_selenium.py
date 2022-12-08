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
import time
import re
from datetime import date
from selenium.webdriver.chrome.options import Options
from some_functions import *


liste_patterns =['<br>','<font color="#333333">', '</font>', '<span.+span>', '\\n(.+)?']
dico_answers = {}
#xpath1= "/html/body/div/div/section/div[2]/article/header/h1"
xpath1="/html/body/div/div/section/div[2]/article/div/p[1]"
xpath2 = "/html/body/div/div/section/div[2]/article/div/p[2]"
xpath3 = "/html/body/div/div/section/div[2]/article/div/p[3]"
xpath4 = "/html/body/div/div/section/div[2]/article/div/p[4]"
xpath5 = "/html/body/div/div/section/div[2]/article/div/p[5]"
xpath6 = "/html/body/div/div/section/div[2]/article/div/p[6]"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.implicitly_wait(3)
browser.maximize_window()

browser.get("https://www.briefmenow.org/comptia/which-sysv-init-configuration-file-should-be-modified-to-disable-the-ctrl-alt-delete-key-combination-2/")
browser.find_element(By.CSS_SELECTOR, "#first-step .icon-close").click()

nbquestion = range(1,120)
i = 1
k = 1

for iteration in nbquestion :
  #reinit variables
  templist=[]
  kek1, kek2, kek3, kek4, kek5, kek6 = 0, 0, 0, 0, 0, 0
  #NEXT BUTTON (AFTER FIRST PAGE)
  if i != 1 :
    browser.find_element(By.CSS_SELECTOR, ".single-top .nav-next strong").click()
  #EXTRACTION
  kek1 = browser.find_element(By.XPATH, value=xpath1).get_attribute('innerHTML')
  kek2 = browser.find_element(By.XPATH, value=xpath2).get_attribute('innerHTML')
  try :
    kek3 = browser.find_element(By.XPATH, value=xpath3).get_attribute('innerHTML')
    kek4 = browser.find_element(By.XPATH, value=xpath4).get_attribute('innerHTML')
    kek5 = browser.find_element(By.XPATH, value=xpath5).get_attribute('innerHTML')
    try :  
      kek6 = browser.find_element(By.XPATH, value=xpath6).get_attribute('innerHTML')
      templist.extend((kek1, kek2, kek3, kek4, kek5, kek6))
    except :
      print("pas de réponse E")
      templist.extend((kek1, kek2, kek3, kek4, kek5))
  except :
    print("Only réponse A ")
    print("Ca veut dire que c'est une réponse en commande libre ?")
    templist.extend((kek1, kek2))
    wrapping_input(templist, dico_answers, k, liste_patterns)
    k += 1
    issou = 1
    print("Question spéciale numéro "+str(k)+" !")
  if issou != 1 :
    wrapping_normal(templist, dico_answers, i, liste_patterns)
    print("C'était le n°"+str(i)+"... Passage à la question suivante ...")
    i += 1
print('Finito !')
browser.quit()

"""print("Mettage good answers")
  print("==========================================")
  mettage_answers(templist, dico_answers, i, liste_patterns )
  print(dico_answers)
  print("==========================================")

  print("Nettoyage...")
  nettoyage_regex(liste_patterns, templist)
  print("==========================================")
  print("==========================================")

  print("ajout d'un saut de ligne")
  ajout_sautligne(templist)
  print(templist)

  print("Insertion dans le JSON")
  y = {
            "id":i,
            "question":(' '.join(templist)),
            "answer":(','.join(dico_answers[i])),
            "explanation":" "
        }
  insertion_json(y, 'auto_christine.json',"questionnaire2018")"""





