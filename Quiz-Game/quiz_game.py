print("=" * 50)
print("           PYTHON QUIZ GAME")
print("=" * 50)

while True:
    score = 0
    questions = [
        {
            "question": "1. Which language is this quiz about?",
            "options": ["A. Java", "B. Python", "C. C++", "D. JavaScript"],
            "answer": "B"
        },
        {
            "question": "2. Which function is used to display output in Python?",
            "options": ["A. output()", "B. display()", "C. print()", "D. show()"],
            "answer": "C"
        },
        {
            "question": "3. Which symbol is used to write a comment in Python?",
            "options": ["A. //", "B. #", "C. <!-- -->", "D. /* */"],
            "answer": "B"
        },
        {
            "question": "4. Which data type is used to store whole numbers?",
            "options": ["A. float", "B. string", "C. int", "D. bool"],
            "answer": "C"
        },
        {
            "question": "5. Which data type stores True or False?",
            "options": ["A. bool", "B. int", "C. str", "D. float"],
            "answer": "A"
        },
        {
            "question": "6. Which keyword is used to create a function?",
            "options": ["A. function", "B. define", "C. def", "D. fun"],
            "answer": "C"
        },
        {
            "question": "7. Which loop is commonly used to iterate through a list?",
            "options": ["A. repeat", "B. for", "C. loop", "D. during"],
            "answer": "B"
        },
        {
            "question": "8. Which brackets are used to create a list?",
            "options": ["A. ()", "B. {}", "C. []", "D. <>"],
            "answer": "C"
        },
        {
            "question": "9. Which method converts a string to uppercase?",
            "options": ["A. .upper()", "B. .uppercase()", "C. .up()", "D. .capital()"],
            "answer": "A"
        },
        {
            "question": "10. What does len() return?",
            "options": [
                "A. The largest value",
                "B. The length of an object",
                "C. The smallest value",
                "D. The data type"
            ],
            "answer": "B"
        },
        {
            "question": "11. Which data structure stores key-value pairs?",
            "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
            "answer": "D"
        },
        {
            "question": "12. Which operator is used for exponentiation?",
            "options": ["A. ^", "B. **", "C. //", "D. %%"],
            "answer": "B"
        },
        {
            "question": "13. Which keyword is used to make a decision in Python?",
            "options": ["A. if", "B. when", "C. check", "D. decide"],
            "answer": "A"
        },
        {
            "question": "14. Which function is used to take input from the user?",
            "options": ["A. get()", "B. input()", "C. read()", "D. scan()"],
            "answer": "B"
        },
        {
            "question": "15. Which keyword is used to stop a loop immediately?",
            "options": ["A. stop", "B. exit", "C. break", "D. close"],
            "answer": "C"
        }
    ]

    print("\nLet's start the quiz!")
    print("Enter A, B, C, or D for each question.\n")

    for current_question in questions:

        print("-" * 50)
        print(current_question["question"])

        for option in current_question["options"]:
            print(option)

        while True:
            user_answer = input("Your answer: ").upper()

            if user_answer in ["A", "B", "C", "D"]:
                break

            print("Invalid input! Please enter A, B, C, or D.")

        if user_answer == current_question["answer"]:
            print("✓ Correct!")
            score += 1
        else:
            print("✗ Wrong!")
            print("Correct answer:", current_question["answer"])

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print("\n" + "=" * 50)
    print("             QUIZ COMPLETED")
    print("=" * 50)

    print("Total Questions :", total_questions)
    print("Correct Answers :", score)
    print("Wrong Answers   :", total_questions - score)
    print("Percentage      :", percentage, "%")

    if percentage == 100:
        print("Grade           : A+")
        print("Excellent! Perfect score!")

    elif percentage >= 80:
        print("Grade           : A")
        print("Great job!")

    elif percentage >= 60:
        print("Grade           : B")
        print("Good work!")

    elif percentage >= 40:
        print("Grade           : C")
        print("Keep practicing!")

    else:
        print("Grade           : D")
        print("You need more practice.")

    print("=" * 50)

    play_again = input("\nDo you want to play again? (Y/N): ").upper()

    if play_again != "Y":
        print("\nThank you for playing!")
        break