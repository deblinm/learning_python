#list of questions. Randomly googled some question, but you can dd more question and increase
#the total_questions value as and when you want.
#store the answers
#randomly pick questions
#ask the questions
#see if they are correct
#keep a track of the score
#tell the user their score



import random

questions = {
    "What keyword starts a conditional check (if/then)?" : "if",
    "What keyword defines a reusable block of code?" : "def",
    "What keyword provides an alternative to if or elif" : "else",
    "What keyword checks if two variables refer to the same object? ":"is",
    "What function returns the length of a sequence?" : "len"
}


def trivia_game():
    questions_list = list(questions.keys())
    total_questions = 3
    score = 0
    random_question = random.sample(questions_list, total_questions)

    for index,question in enumerate(random_question):
        print(f"{index}. {question}")
        answer = input("Enter your answer: ").lower().strip()

        correct_answer = questions[question].lower().strip()

        if answer == correct_answer:
            print(f"Correct! \n")
            score+=1
        else:
            print(f"Wrong! The correct answer is {correct_answer}. \n")

    return score


total = trivia_game()
print(f"Total score: {total}")