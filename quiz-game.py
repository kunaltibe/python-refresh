# Quiz Game
# Author: Kunal Tibe
# Description: A quiz game with questions, options, and score tracking.

questions = ("1. What gas do plants absorb from the atmosphere during photosynthesis?",
             "2. What is the center of an atom called?",
             "3. What is the boiling point of water at sea level?",
             "4. Which planet has the most moons in the solar system?",
             "5. What part of the cell contains genetic material?")
options = (("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
           ("A. Electron", "B. Proton", "C. Neutron", "D. Nucleus"),
           ("A. 90°C", "B. 100°C", "C. 120°C", "D. 80°C"),
           ("A. Jupiter", "B. Saturn", "C. Neptune", "D. Uranus"),
           ("A. Mitochondria", "B. Cytoplasm", "C. Nucleus", "D. Ribosomes"))
answers = ("C", "D", "B", "B", "C")
guesses = []
question_num = 0
score = 0

print("--------------------------------------------------------")
print("WELCOME TO THE QUIZZ GAME!")

for question in questions:
    print("--------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Guess the Answer (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess in answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"The Correct Answer is {answers[question_num]}")
    question_num += 1

print("--------------------------------------------------------")
print("Answers: ", end= "")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses: ", end= "")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Score: {score}%")
print("--------------------------------------------------------")