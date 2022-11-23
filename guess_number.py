# guess_the_number v.0.1

import random

hl = "=========================="

# Welcome
print(hl)
print("Welcome to game!\n"
      "I'll generate a random number and you need to guess that number.\n"
      "You'll have limited number of attempts.\n"
      "But I'll give you some hints =)\n"
      "Let's start!")

# Difficulty level / Start menu
active = True
while active:
    print(hl)
    difficulty = input("Please select a difficulty level:\n"
                       "1 => Easy.\n"
                       "2 => Medium.\n"
                       "3 => HARD.\n\n"
                       "0 => custom.\n")
    
    if not difficulty.isnumeric():
        print("\nI need a number, what are you talking about?")
        continue
    difficulty = int(difficulty)
        
    
# Setting attempts and random numbers range.
# Easy
    if difficulty == 1:
        random_range = [0, 100]
        num = random.randint(random_range[0], random_range[1])
        attempts = 7
# Medium
    elif difficulty == 2:
        random_range = [0, 10_000]
        num = random.randint(random_range[0], random_range[1])
        attempts = 15
# Hard
    elif difficulty == 3:
        random_range = [0, 1_000_000]
        num = random.randint(random_range[0], random_range[1])
        attempts = 25
# Custom
    elif difficulty == 0:
        random_range = [0, 0]

        while True:
            print(hl)
            min_num = input("What is the minimum possible number?\n")
            if not min_num.isnumeric():
                print("\nI need a number, what are you talking about?")
                continue
            random_range[0] = int(min_num)
            break

        while True:
            print(hl)
            max_num = input("What is the maximum possible number?\n")
            if not max_num.isnumeric():
                print("\nI need a number, what are you talking about?")
                continue
            random_range[1] = int(max_num)
            break

        num = random.randint(random_range[0], random_range[1])

        while True:
            print(hl)
            attempts = input("How many attempts do you need "
                             "to guess a number in this range?\n")
            if not attempts.isnumeric():
                print("\nI need a number, what are you talking about?")
                continue
            attempts = int(attempts)
            break

# Wrong menu number
    else:
        print("\nHey! What is this? Are you kidding me?")
        continue

    print(hl)
    print(f"You have {attempts} attempts to guess number from "
          f"{random_range[0]:,} to {random_range[1]:,}")

# Game
    guesses_list = []
    attempt_number = 0

    while True:
        print(hl)
        guess = input("Your guess?\n")
        if not guess.isnumeric():
            print("\nI need a number, what are you talking about?")
            continue
        guess = int(guess)
        attempts -= 1
        attempt_number += 1
        print(hl)

# Win
        if guess == num:
            print("Congratulations! YOU WIN!!!")
            while True:
                print(hl)
                play_again = input("Do you want to play again?\n"
                                   "1 => Yes.\n"
                                   "0 => No.\n")
                if not play_again.isnumeric():
                    print("\nI need a number, what are you talking about?")
                    continue
                else:
                    play_again = int(play_again) 
                    break

            if play_again == 1:
                break
            else:
                active = False
                break

# Game over
        elif attempts == 0:
            print("GAME OVER.")
            print(f"My number was: {num}")
            while True:
                print(hl)
                play_again = input("Do you want to play again?\n"
                                   "1 => Yes.\n"
                                   "0 => No.\n")
                if not play_again.isnumeric():
                    print("\nI need a number, what are you talking about?")
                    continue
                else:
                    play_again = int(play_again) 
                    break

            if play_again == 1:
                break
            else:
                active = False
                break

# Too small number
        elif guess < num:
            print(f"Now you have only {attempts} attempts")
            print("\nMy number is GREATER than your guess.")
            guesses_list.append(f"{attempt_number}. N > {guess:,}")
            print("\nYour last guesses:")
            for guess_from_list in guesses_list:
                print (guess_from_list)

# Too big number
        elif guess > num:
            print(f"Now you have only {attempts} attempts")
            print("\nMy number is LESS than your guess.")
            guesses_list.append(f"{attempt_number}. N < {guess:,}")
            print("\nYour last guesses:")
            for guess_from_list in guesses_list:
                print (guess_from_list)
