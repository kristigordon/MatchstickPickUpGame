# MatchstickPickUpGame

This is a game that tests knowledge of conditionals, loops and ends with cleaning up the code. 

The game starts with 13 "matchsticks": |
The two players input there names then go into a loop of selecting 1-3 matchsticks until there is only one left and the player to pick up that remaining stick wins. 

<img width="660" alt="Screen Shot 2022-07-30 at 9 29 27 AM" src="https://user-images.githubusercontent.com/66803124/181916524-189824a5-89e0-4f3c-9317-9675e02b11ce.png">


<img width="655" alt="Screen Shot 2022-07-30 at 9 30 40 AM" src="https://user-images.githubusercontent.com/66803124/181916571-1114bbdd-03ae-4116-9210-ef3e2dafa946.png">

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
This first solution definitely works, however there is a lot of duplication. I am basically running the same 10 lines for player1 again for player2 in one long duplicative loop. I think I can do better. 

This starts with creating a "current_player" value that we will start with it set to player1.

Most of the rest of the first loop I had can stay, just need to change out any instance of player1 with current player and comment out the player2 loop.

<img width="609" alt="Screen Shot 2022-07-30 at 9 44 23 AM" src="https://user-images.githubusercontent.com/66803124/181917180-5b1e3020-89af-47f8-855a-7f46671bea6b.png">

This "works" but now only player1 gets to pick up matchsticks and inevitably wins the game. No fair. Let's have player2 enter the fray. 

We need to rotate each player into the current_player slot. 

We can do this by checking if the current_player is player1 after a loop runs. If so, then let's switch them out of playler2. If it isn't, then let's make it player1 and keep on chuggin.

<img width="912" alt="Screen Shot 2022-07-30 at 9 46 26 AM" src="https://user-images.githubusercontent.com/66803124/181917249-97eba8e0-6d12-4a2d-89c3-7b583884689a.png">

And once again, it works!

As long as our players are trustworthy and only type the numbers 1-3.... 

<img width="694" alt="Screen Shot 2022-07-30 at 9 47 52 AM" src="https://user-images.githubusercontent.com/66803124/181917309-5cbc9971-40ed-4e21-9fee-312bf8571692.png">

... I can't have my wife winning EVERY game. 

So lets put some parameters in place:
The player should only be able to select number 1, 2, or 3. Anything else will result in an error message and another input message attached to choice variable for the opportunity to try again. 

<img width="896" alt="Screen Shot 2022-07-30 at 9 54 19 AM" src="https://user-images.githubusercontent.com/66803124/181917531-978c98e0-ba4b-464b-9b5d-c359ef93a694.png">

And we got her! Now I can have a chance to ~*maybe*~ win. 

