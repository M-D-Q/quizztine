import json


def modify_questions(data, questionnaire_name, marked_questions_json_name):
    # Read the marked_questions.json file
    with open(marked_questions_json_name, 'r') as f:
        marked_questions = json.load(f)

    # Iterate over the marked questions in the dictionary
    for question_id, info in marked_questions.items():
        for question_id, info in marked_questions.items():
            question = next(q for q in data[questionnaire_name] if q['id'] == int(question_id))

        
        print(f"""
Question || {question["question"]}

Answer || {question["answer"]}

Explanation || {question["explanation"]}

        """)
        
    

        # Print the comment for the marked question
        print(f"=====Comment for question {question_id}: {info['comment']}======")

        osef = input("Ready to modify ?")
        if osef: 
            # Prompt the user to modify the question and explanation
            new_question =input(f"""Modify the question: 
            {repr(question["question"])}""")
            new_explanation=input(f"""Modify the explanation:
            {repr(question["explanation"])}""")
            new_answer=input(f"""Modify the answer:
            {repr(question["answer"])}""")
            
            if new_question :
                question["question"] = new_question
            if new_explanation :
                question["explanation"] = new_question
            if new_answer :
                question["answer"] = new_question

    # Write the modified data dictionary back to the JSON file
    print("Now, we will print the changes")
    with open('auto_christine.json', 'w') as f:
        json.dump(data, f, indent=4, separators=(',', ': ') )#,sort_keys=True)

###CODE PAS ENCORE FONCTIONNEL. Ca deconne pas mal au niveua de l'insertion JSON, et l'interet est quand même assez limité.


# Test the modify_questions function
    # Open the JSON file in read mode

"""with open('auto_christine.json', 'r') as f:
    # Load the contents of the file into a dictionary
    data = json.load(f)


modify_questions(data, "Exam-Topics 102-500 - Paywall breached", "marked_questions_Questionnaire_Shuffle_.json")"""
