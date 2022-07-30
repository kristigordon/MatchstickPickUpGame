print("Welcome to the Matchstick Pickup Game!")
print("*******************************")
player1 = input("Player 1's Name:\n")
player2 = input("Player 2's Name:\n")
matchstick = 13

while True:
    print("|" * matchstick)
    print(f"There are {matchstick} matchsticks left")
    p1_choice = int(input(f"{player1}, how mnay matchsticks do you select?\n"))
    matchstick -= p1_choice
    if matchstick <= 0:
        print(f"{player1} wins the game!")
        break

    print ("| " * matchstick)
    print(f"There are {matchstick} matchsticks left")
    p2_choice = int(input(f"{player2}, how mnay matchsticks do you select?\n"))
    matchstick -= p2_choice
    if matchstick <= 0:
        print(f"{player2} wins the game!")
        break

print("GAME OVER!")
