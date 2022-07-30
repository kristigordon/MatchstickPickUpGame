# MatchstickPickUpGame

This is a game that tests knowledge of loops. 

The game starts with 13 "matchsticks": |
The two players input there names then go into a loop of selecting 1-3 matchsticks until there is only one left and the player to pick up that remaining stick wins. 

<img width="660" alt="Screen Shot 2022-07-30 at 9 29 27 AM" src="https://user-images.githubusercontent.com/66803124/181916524-189824a5-89e0-4f3c-9317-9675e02b11ce.png">

```
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
```

<img width="655" alt="Screen Shot 2022-07-30 at 9 30 40 AM" src="https://user-images.githubusercontent.com/66803124/181916571-1114bbdd-03ae-4116-9210-ef3e2dafa946.png">
