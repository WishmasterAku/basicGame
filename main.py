playerName = (input("Hello please enter your name "))
gameActive = (input("Type yes to Start Game ").lower())
if gameActive != "yes":
    print("Shutting Down")
    quit()
print("Let the games begin!")
print("Please choose which game you like to play")
print("1. Quiz Game\n2. Guess the Number\n3. Rock Paper Scissors\n4. Adventurer Games\n5. Zelda Python")
gameOption = input("")