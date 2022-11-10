playerName = (input("Hello please enter your name "))
gameActive = (input("Type yes to Start Game ").lower())
if gameActive != "yes":
    print("Shutting Down")
    quit()
print("Let the games begin!")
print("Please choose which game you like to play")
print("1. Quiz Game\n2. Guess the Number\n3. Rock Paper Scissors\n4. Adventurer Games\n5. Zelda Python")
gameOption = input("1")

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
    
print(f"{playerName}'s total points is {results}")
