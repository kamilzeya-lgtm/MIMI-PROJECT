questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for AI?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which data type stores multiple values in Python?",
        "options": ["A. int", "B. list", "C. float", "D. bool"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Unit",
            "D. Control Processing Unit"
        ],
        "answer": "A"
    }
]


def conduct_quiz():
    score = 0

    print("\n===== QUIZ START =====")

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")

        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", q["answer"])

    return score


def save_result(score):
    with open("quiz_result.txt", "w") as file:
        file.write("===== QUIZ RESULT =====\n")
        file.write(f"Score: {score}/{len(questions)}\n")

        percentage = (score / len(questions)) * 100
        file.write(f"Percentage: {percentage}%\n")

    print("\nResult saved to quiz_result.txt")


score = conduct_quiz()

print("\n===== FINAL RESULT =====")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

save_result(score)