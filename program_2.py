# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

# Program #2: Math Quiz
# Author: Zepora Lilly
# Date: 09/30/2025
import random

def generate_quiz():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    correct_answer = num1 + num2

    print(f"\n {num1}")
    print(f"+ {num2}")
    print("------")

    user_answer = int(input("Enter your answer: "))
    if user_answer == correct_answer:
        print("Congratulations! You got it right.")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.