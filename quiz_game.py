# python quiz game

questions = ("how many elements are there in the periodic table?: ",
             "which animal lays the largest eggs? : ",
             "how many bones are in the human body? : ",
             "what is the most abundant gas in earth's atmosphere",
             "which planet in the solar system is the hottest? :")

options = (("A. 116","b. 117","c. 118","d. 119"),
           ("A. whale","b. crocodile","c. elephant","d. ostrich"),
           ("A. 206","b. 207","c. 208","d. 209"),
           ("A. nitrogen","b. oxygen","c. carbon-dioxide","d. hydrogen"),
           ("A .mercury","b. venus","c. earth","d. mars"))


answers = ("C","D","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
     print("------------------------")
     print(question)
     for option in options[question_num]:
          print(option)

     guess = input("enter ( a, b, c, d): ").upper()
     guesses.append(guess)
     if guess == answers[question_num]:
          print("Correct")
          score+=1
     else :
          print("Incorrect")
          print(f"{answers[question_num]} is the correct answer")


     question_num +=1

print("------------------------")
print("------------result------------")
print("--------------------------")

print("answers: ",end="\n")
for answer in answers:
     print(answer,end=" ")
     print()

print()
print("guesses: ",end="\n")
for guess in guesses:
     print(guess,end=" ")
     print()
print()

score = int(score / len(questions) * 100)
print(f"total score is :{score}%")





