#! /usr/bin/bash

echo "Let's get started!"

# Numéro du précédent chaptire
numChapter=$(($(cat auto_christine.json | grep chapitre | tail -n 1 | cut -d'"' -f 2 | cut -d"e" -f 2)+1))

### Injection nouveau chapitre dans BD json

#################################
# BOUCLE JUSQUE numChapter = 10 #
#################################

######################################
# Supprimer dernier } & ] du fichier #
######################################

# Chapitre
echo "{" >> auto_christine.json
echo '"chapitre$numChapter": [' >> auto_christine.json
echo "    {" >> auto_christine.json
##############################################
# BOUCLE JUSQUE id = 20 pour chaque chapitre #
##############################################

# id
id=$(head questions.txt | cut -d" " -f1)
echo '        "id":$id' >> auto_christine.json

# question

	# ligne de début question suivante
nbIteration=$(($(uniq -u questions.txt | nl | grep "$(($id+1)). " | head -1 | cut -f1)-1))
for i in 'seq 1 $nbIteration'
do
	uniq -u questions.txt | head -1 > tmp$i.txt
	cat tmp$i.txt >> questions.txt
	i=$(($i+1))
done
question=$(paste -d "" tmp*)
echo '        "question":"$question",' >> auto_christine.json
rm tmp*

# answer
answer=$(head -1 answers.txt | cut -d "." -f 2)
echo '        "answer":"$answer",' >> auto_christine.json

# explanation

nbIterationExplanation=$(($(uniq -u answers.txt | nl | grep "$(($id+1)). " | head -1 | cut -f1)-1))
for i in 'seq 1 $nbIterationExplanation'
do
        uniq -u answers.txt | head -1 > tmp$i.txt
        cat tmp$i.txt >> answers.txt
        i=$(($i+1))
done
answer=$(paste -d "" tmp*)
echo '        "answer"="$answer",' >> auto_christine.json
rm tmp*

echo "    }," >> auto_christine.json

# FIN BOUCLE QUESTION

# FIN DE BOUCLE CHAPITRE

##############################################
# Voir comment supprimer la dernière virgule #
##############################################

echo "]" >> auto_christine.json
echo "}" >> auto_christine.json
