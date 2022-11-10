from games import quiz_game

#playerName = (input("Hello please enter your name "))
gameActive = (input("Type yes to Start Game ").lower())
if gameActive != "yes":
    print("Shutting Down")
    quit()
print("Let the games begin!")
print("Please choose which game you like to play")
game_option = input("1. Quiz Game\n2. Guess the Number\n3. Rock Paper Scissors\n4. Adventurer Games\n5. Zelda Python\n")
      
if game_option == "1":
    quiz_game()
else:
    ("Try again next time")
    quit()
    