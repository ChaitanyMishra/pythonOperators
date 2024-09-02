import random

print("----->Guess The Number<------")
print("Please Choose The Mode--> ")
print("press '1' for Player vs computer: ")
print("press '2' for Player vs player: ")
mode = input("Select mode: ")
rounds = int(input("How much rounds you want's to play? "))
player1_score = 0
player2_score = 0
print("You have only '5' chances to guess correct! ")
# ==================================================================================================
if mode == "1":
    print("-----> player vs computer <-------")
    for i in range(1, rounds + 1):
        print(f"round {i} of {rounds}")
        number = random.randint(1, 100)
        attempt = 5
        print("Guess number between '1' to '100' ! ")
        for cattempt in range(1, attempt + 1):
            guess = int(input(f"attempt {attempt} ! "))
            if number == guess:
                print("You won the point +1")
                player1_score += 1
                break
            elif number > guess:
                print("Too low !")
            elif number < guess:
                print("Too high !")
        else:
            print("You are out of attempt")
            print(f"Correct answer is: {number} ")
# ----------------------------------------------------------------------------------------------------------
elif mode == "2":
    print("You have only '5' chnaces to guess correct ! ")
    print("-------------------------------------")
    print("-----------> player vs player <-----------")
    for i in range(1, rounds + 1):
        print(f"round {i} of {rounds} ")
        player1 = int(input("Player '2' enter number between '0' to '100' ! "))
        attempts = 5
        print("Guess number between '1' to '100' ! ")
        for attempt in range(1, attempts + 1):
            guess = int(input(f"attempt {attempt} : "))
            if player1 == guess:
                print("you won +1 points: ")
                player1_score += 1
                break
            elif player1 > guess:
                print("Too low !")
            elif player1 < guess:
                print("Too high !")
        else:
            print("You are out of attempt")
            print(f"Correct answer is: {player1} ")
    # ------------------------------------------------------------------------------------------------------------------
    player2 = int(input("Player '1' enter number between '0' to '100' ! "))
    print("Guess number between '1' to '100' ! ")
    for attempt in range(1, attempt + 1):
        guess = int(input(f"attempt {attempt} : "))
        if player2 == guess:
            print("you won +1 points: ")
            player2_score += 1
            break
        elif player2 > guess:
            print("Too low !")
        elif player2 < guess:
            print("Too high !")
        else:
            print("You are out of attempt")
            print(f"Correct answer is: {player2} ")
else:
    print("invalid input ! CHOOSE CORRECT GAME MODE! ")
# ===================================================================================================================
if mode == "1":
    print("\nGame Over!")
    print(f"Player 1 Score: {player1_score}")
    print("Computer wins!" if player1_score == 0 else "Player 1 wins!")
elif mode == "2":
    print("\nGame Over!")
    print(f"Player 1 Score: {player1_score}")
    print(f"Player 2 Score: {player2_score}")

    if player1_score > player2_score:
        print("Player 1 is the winner!")
    elif player2_score > player1_score:
        print("Player 2 is the winner!")
    else:
        print("It's a tie!")
# ==========================================================================================================================
