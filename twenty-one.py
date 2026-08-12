#simple game of 21, also known as blackjack, this is a two player version of the game, where the player can choose to hit or stand

import random

#vars
game_over1 = False
totalCardAmount = 0
totalMoney = 100
#game_over2 = False

#greeting message
print("Welcome to 21, the goal is to get as close to 21 or at 21, if you go over 21 you lose. You can also bet money, you start with $100.")

while game_over1 == False:

    input1 = input("\nHit or Stand Player 1 (Press Q to end game, H for Hit, S for Stand): \n")

    #if u pressed Q it quits the game (or lowercase q)
    if input1 == "Q" or input1 == "q":
        print("\nYou chose to quit, fuck u")
        game_over1 = True

    elif input1 == "H" or input1 == "h":
        cardValue = random.randint(1, 11)
        totalCardAmount += cardValue
        print(f"\nYou drew a {cardValue} card, your total card amount is {totalCardAmount}")

    elif input1 == "S" or input1 == "s":
        print("\nYou chose to stand")
        print(f"\nYour total card amount is {totalCardAmount}")
        
        game_over1 = True

    if totalCardAmount > 21:
        print(f"\nYou went over 21, you lose, your total card amount is {totalCardAmount}")
        game_over1 = True

