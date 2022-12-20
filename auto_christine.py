import json
from fonctions_main import *
#TO DO : ajouter ascii art, sound "lets get started"

with open ("auto_christine.json", "r", encoding='utf-8') as dico:
    dataset = dico.read()
    data = json.loads(dataset)

liste_questionnaires_book = ["Assessment Test", "Chapter 1: Exploring Linux Command-Line Tools", "Chapter 2: Managing Software", "Chapter 3: Configuring Hardware", "Chapter 4: Managing Files",
"Chapter 5: Booting Linux and Editing Files", "Chapter 6: Configuring the X Window System, Localization, and Printing", "Chapter 7: Administering the System"]
# WORKING ON IT "Chapter 8: Configuring Basic Networking", "Chapter 9: Writing Scripts, Configuring Email, and Using Databases", "Chapter 10: Securing Your System"

liste_questionnaires_dumps = ["Exam-Topics 101 - Paywall breached (w/ explanations)", "Exam-Topics 101 - Paywall breached - Version Large (w/ explanations)", "Exam-Topics 101 - Paywall breached - Input"]
continuer = 1
while continuer == 1:
    choix_first = str(input("""
What do you want to study ?
0 - Assessment Test & Chapters w/ explanations from LPIC-1 Study Guide book ?
1 - Dumps questionnaires - Choice answers

Enter chosen number here ->"""))
    if choix_first == "0" :
        deroulement_questionnaire(liste_questionnaires_book,data)
    elif choix_first == "1":
       deroulement_questionnaire(liste_questionnaires_dumps,data)
    print("c'est finito")
    continuer = int(input("""
Continuer ? (1 = Oui)
--> """))
    # Et de l'esthétique bien sur.