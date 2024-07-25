import sys

print("!!!!!!! Welcome to SWB Shree will make you millionaire!!!!!!\n\n\n\n")

# List of questions
questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is the largest mammal in the world?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What gas do plants absorb from the atmosphere?",
    "What is the tallest mountain in the world?",
    "Which element is represented by the chemical symbol 'O'?",
    "What is the currency of Japan?",
    "Who painted the Mona Lisa?",
    "What is the boiling point of water in Celsius?",
    "What is the main ingredient in guacamole?",
    "What is the national flower of India?",
    "In which year did the Titanic sink?",
    "Who is the author of 'To Kill a Mockingbird'?"
]

# List of options for each question
options = [
    ["A) Paris", "B) Madrid", "C) Rome", "D) Berlin"],
    ["A) Venus", "B) Jupiter", "C) Mars", "D) Saturn"],
    ["A) African Elephant", "B) Polar Bear", "C) Blue Whale", "D) Giraffe"],
    ["A) Charles Dickens", "B) Jane Austen", "C) William Shakespeare", "D) Mark Twain"],
    ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
    ["A) Mount Everest", "B) K2", "C) Kilimanjaro", "D) Kangchenjunga"],
    ["A) Oxygen", "B) Osmium", "C) Gold", "D) Iron"],
    ["A) Yen", "B) Won", "C) Yuan", "D) Euro"],
    ["A) Michelangelo", "B) Leonardo da Vinci", "C) Vincent van Gogh", "D) Pablo Picasso"],
    ["A) 100°C", "B) 0°C", "C) 50°C", "D) 75°C"],
    ["A) Avocado", "B) Tomato", "C) Onion", "D) Garlic"],
    ["A) Lotus", "B) Rose", "C) Lily", "D) Sunflower"],
    ["A) 1911", "B) 1912", "C) 1915", "D) 1917"],
    ["A) Harper Lee", "B) J.K. Rowling", "C) George Orwell", "D) Ernest Hemingway"]
]

# List of correct answers
correct_answers = ["A", "C", "C", "C", "A", "A", "A", "A", "B", "B", "A", "A", "B", "A"]

# For user score
user_score = 5000

for i in range(len(questions)):
    print(questions[i])
    print(options[i])
    answer = input("Enter your answer (or enter '0' to quit the game): ")
    if answer == '0':
        print("Thank you for playing! You are taking home ${}".format(user_score))
        sys.exit()
    a = answer.upper()
    if a == correct_answers[i]:
        print("Correct!")
        user_score *= 2
        print("Congratulations! You are taking home ${}".format(user_score))
    else:
        print("Incorrect answer! Thank you for playing!")
        print("Congratulations! You are taking home ${}".format(user_score))
        sys.exit()