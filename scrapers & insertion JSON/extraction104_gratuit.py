from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import *
from selenium.webdriver.chrome.options import Options
from functions_briefmenow import *

#nom du questionnaire pour ajout dans le JSON (string)

#Liste des patterns regex à supprimer des textes extraits (list)

# Open le TXT avec les urls et stocker chaque ligne dans une liste (with open etc)

# ouvrir le truc webdriver :
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.implicitly_wait(3)
browser.maximize_window()

#QUESTION avec ERREUR : Mettre les URLs dans une liste à part pour ensuite voir si le pdf de Slimane les contient ou pas



#QUESTION AVEC ABCDE - Gérer les différents nombres d'options de réponse, essayer d'extraire les explications existantes, si elles existent.



#QUESTION AVEC IMAGE - Detecter l'image et mettre ça dans une liste à part pour traitement manuel ou pas.






