
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