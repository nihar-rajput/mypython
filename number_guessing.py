# python number guessing game

import random

lowest = 1
highest = 100

answer = random.randint(lowest,highest)
guesses = 0
is_running = True

print("-------number guessing game-------")
print(f"guess a number between {lowest} to {highest}")
print()

while is_running:
     guess = input("Enter your guess : ")

     if guess.isdigit():
          guess = int(guess)
          guesses += 1

          if guess < lowest or guess > highest:
              print("that number is out of range")
              print(f"please select a number between {lowest} and {highest}")
          elif guess< answer:
              print("too low! try again!")
          elif guess > answer:
               print("Too high! try again!")
          else:
               print(f"CORRECT! the answer was {answer}")
               print(f"number of guesses: {guesses}")

     else:
          print("invalid guess")
          print(f"guess a number between {lowest} to {highest}")