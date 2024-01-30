import random

def ask_question(question, correct_answer):
    print(question)
    user_answer = input("Your answer: ").lower()
    
    if user_answer == correct_answer.lower():
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer is {correct_answer}\n")
        return False

def play_quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "Which planet is known as the Red Planet?": "Mars",
        "What is the largest mammal in the world?": "Blue Whale",
        "What is 7 + 5?": "12",
        # Add more questions here
    }

    question_keys = list(questions.keys())
    random.shuffle(question_keys)

    score = 0

    for question_key in question_keys:
        is_correct = ask_question(question_key, questions[question_key])
        if is_correct:
            score += 1

    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    print("Welcome to the Quiz Game!\n")
    play_quiz()
