import re
import json
from functions_txt import *

#patterns_to_remove = [r"^flast.+$", r"^.+Assessment Test$", r"^(l|v|x)(l|v|x|i)(l|v|x|i).+$", r"\\n ? ?", r"  [ ]*" ]
#extraction_assessment("sources\\answersassessment.txt","sources\\answersassessment1.txt", patterns_to_remove)
#formattage_insertion_assessment("sources\\answersassessment1.txt")


###### BOF, ne supprime pas les lignes vide
#patterns_to_remove = [r"(.+)?[5-9][0-9][0-9]$", r"^(Appendix|Answers)", r"((Chapter [1-2]?[0-9]:).+)$", r"(\\n ? ?)|(\\n ? ?)", r"  [ ]*",]
#extraction_answers("sources\\answersLPIC1cropped.txt","sources\\answersLPIC1cropped_cleaned.txt", patterns_to_remove)



#patterns_to_remove = [r"(.+)?[5-9][0-9][0-9]$", r"^(Appendix|Answers)", r"((Chapter [1-2]?[0-9]:).+)$" r"\n"]
#formattage_insertion("sources\\answersLPIC1cropped_cleaned.txt", chapter_names)


#extraction_questions("sources\\questionsassessment.txt", "sources\\questionsassessment_cleaned.txt")
#formattage_insertion_question("sources\\questionsassessment_cleaned.txt")

#####GOOD FOR ASSESSMENT
#tous_ensemble_assessment("sources\\questionsassessment_cleaned.txt", "sources\\answersassessment1.txt", "Assessment Test")
#####

#### FAIT EXTRACTION QUESTIONS
#patterns_to_remove_questiongeneral = [r"(.+)?c[0-9][0-9].indd.+", r"(.+)?Review Questions(.+)?", "(.*)Chapter(.+)", r"(\n)|(\\n)", r"  [ ]*"]
#doc_source_questions = "sources\\questionsLPIC1_cropped.txt"
doc_cible_questions = "sources\\questionsLPIC1_cropped_cleaned.txt"
#extraction_questions(doc_source_questions, doc_cible_questions, patterns_to_remove_questiongeneral)
####

# retirer les trucs indésirables, mettre les livres sterling au num des question, concatener tous avec un espace entre lines concaténées
# split aux livres sterling
# suppr les doubles espaces. remplacer les lettre de réponse par '\n'+lettre de réponse
doc_cible_answers = "sources\\answersLPIC1cropped_cleaned.txt"
chapter_names = ["Chapter 1: Exploring Linux Command-Line Tools", "Chapter 2: Managing Software", "Chapter 3: Configuring Hardware", "Chapter 4: Managing Files",
"Chapter 5: Booting Linux and Editing Files", "Chapter 6: Configuring the X Window System, Localization, and Printing", "Chapter 7: Administering the System",
"Chapter 8: Configuring Basic Networking", "Chapter 9: Writing Scripts, Configuring Email, and Using Databases", "Chapter 10: Securing Your System" ]
#print(formattage_1ststep("sources\\answersLPIC1cropped_cleaned.txt"))

tous_ensemble_general(doc_cible_questions, doc_cible_answers, chapter_names)

"""patterns_to_remove = [r"(.+)?Assessment Test(.+)?", r"  [ ]*", r"^(.+)?flast.+$", r"\n"]

f = open("sources\\questionsassessment.txt", "r", encoding="utf8")
linelist = f.readlines()
f.close
f2 = open("sources\\questionsassessment_cleaned.txt", "w", encoding="utf8")
i = 0
for line in linelist:
    i += 1
    line = re.sub(r'([A-B-C-D-E]\.)', r"§\1", line)
    line = re.sub(r'(^[1-9][0-9]?\.)', r"£\1", line)
    line = re.sub(r'\"', r'\\"', line)
    for patternos in range(0,len(patterns_to_remove)): 
        pattern = patterns_to_remove[int(patternos)]
        for johnny in range(0, len(linelist)):
            linelist[int(johnny)] = re.sub(pattern, ' ', linelist[int(johnny)])
    f2.write(line)
    print(f"Ligne numéro : {i}")
f2.close()"""