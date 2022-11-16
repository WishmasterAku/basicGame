import random

########################################################### Quiz Game
def quiz_game():
    print("Computer Quiz Game")

    results = 0
    answer = (input("What does CPU stand for? ").lower())
    if answer == "central processing unit":
        print("You are correct")
        results += 1
    else:
        print("Sorry wrong answer")
        
    answer = (input("What does GPU stand for? ").lower())
    if answer == "graphics processing unit":
        print("You are correct")
        results += 1
    else:
        print("Sorry wrong answer")
        
    answer = (input("What does RAM stand for? ").lower())
    if answer == "random access memory":
        print("You are correct")
        results += 1
    else:
        print("Sorry wrong answer")
        
    answer = (input("What does PSU stand for? ").lower())
    if answer == "power supply unit":
        print("You are correct")
        results += 1
    else:
        print("Sorry wrong answer")
        
    print(f"Total points is {results}")
########################################################### Guessing Game
def guessing_Game():
    range_Selected = input("Select a number ")
    
    if range_Selected.isdigit():
        range_Selected = int(range_Selected)
        
        if range_Selected <= 0:
            print("Select a higer number next time")
            quit()
    else:
        print("Please select a number")

    random_number = random.randint(1, range_Selected)
    
    while True:
        user_guess = input("Make a guess ")
        
        if user_guess.isdigit():
            user_guess = int(user_guess)
            
        if user_guess == random_number:
            print("You got it right!")
            break  
        elif user_guess > random_number:
             print("Too high")
        else:
            print("Too low")
        # else:
        #     if user_guess > random_number:
        #         print("Too high")
        #         continue
        #     else:
        #         print("Too Low")
        #         continue
                
def rps():
    user_wins = 0
    computer_wins = 0
    options = ["rock", "paper", "scissors"]
    while True:
        user_input = input("Type Rock, Paper, Scissors or Q to quit ").lower()
        if user_input == "q":
            break
            
        if user_input not in options: # Checking if user input is not in the list
            continue # Will continue till user types a valid choice
        
        random_number = random.randint(0,2) # 0 rock, 1, paper, 2 scissors
    print("Goodbye")