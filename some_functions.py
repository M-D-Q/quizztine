import re
liste_patterns2 =['<br>','<font color="#333333">', '</font>', '<span.+span>']


kek1 = "A.<br> /proc/keys"
kek2 = """B.<br><font color="#333333"> /etc/inittab</font>"""
kek3 = "C.<br> /proc/inittab font color"
kek4 = "D.<br> /etc/reboot"

liste_occurences2 = [kek1, kek2, kek3, kek4]
liste_answers = {}

def nettoyage_ethnique(liste_patterns,liste_occurences):
    for chocolat in range(0, len(liste_patterns)):
        pattern = liste_patterns[int(chocolat)]
        liste_occurences[0] = re.sub(pattern, '', liste_occurences[0])
        print(liste_occurences[0])
        liste_occurences[1] = re.sub(pattern, '', liste_occurences[1])
        print(liste_occurences[1])
        liste_occurences[2] = re.sub(pattern, '', liste_occurences[2])
        print(liste_occurences[2])
        liste_occurences[3] = re.sub(pattern, '', liste_occurences[3])
        print(liste_occurences[3])
        print("Nettoyage numero "+str(chocolat))
    print("Finito!")

nbquestion = "1"
def mettage_answers(liste_occurences, liste_answers, nbquestion):
    templist=[]
    for chocolat in range(0, len(liste_occurences)):
        if "font color" in liste_occurences[int(chocolat)]:
            print("kekii")
            templist.append(liste_occurences[int(chocolat)])
    liste_answers[nbquestion] = templist       

mettage_answers(liste_occurences2, liste_answers, nbquestion)
print(liste_answers)
#nettoyage_ethnique(liste_patterns2, liste_occurences2)
#print(liste_occurences2)