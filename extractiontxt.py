import re
import json
from functions_txt import *

#patterns_to_remove = [r"^flast.+$", r"^.+Assessment Test$", r"^(l|v|x)(l|v|x|i)(l|v|x|i).+$", r"\n" ]
#extraction_assessment("sources\\answersassessment.txt","sources\\answersassessment1.txt", patterns_to_remove)
#formattage_insertion_assessment("sources\\answersassessment1.txt")

#patterns_to_remove = [r"(.+)?[5-9][0-9][0-9]$", r"^(Appendix|Answers)", r"((Chapter [1-2]?[0-9]:).+)$" r"\n"]
#extraction_assessment("sources\\answersLPIC1cropped.txt","sources\\answersLPIC1cropped_cleaned.txt", patterns_to_remove)

chapter_names = ["Chapter 1: Exploring Linux Command-Line Tools", "Chapter 2: Managing Software", "Chapter 3: Configuring Hardware", "Chapter 4: Managing Files",
"Chapter 5: Booting Linux and Editing Files", "Chapter 6: Configuring the X Window System, Localization, and Printing", "Chapter 7: Administering the System",
"Chapter 8: Configuring Basic Networking", "Chapter 9: Writing Scripts, Configuring Email, and Using Databases", "Chapter 10: Securing Your System" ]

#patterns_to_remove = [r"(.+)?[5-9][0-9][0-9]$", r"^(Appendix|Answers)", r"((Chapter [1-2]?[0-9]:).+)$" r"\n"]
formattage_insertion("sources\\answersLPIC1cropped_cleaned.txt", chapter_names)