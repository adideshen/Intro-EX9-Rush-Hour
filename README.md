# Intro-EX9-Rush-Hour

This is the "Rush Hour" game. The goal in this game is to get the red car to the exit, which is in coordinate (3,7).
There is a board that the user provides to the program as a JSON file (for exmple - the "game_example.json" file). The file contains the cars (their name and length), their location on the board and their orientation.
In this game the user enters the name of the car and in which direction to move it in the format "NAME,DIRECTION" (for expmle: "R,r" - R represents the car's name and r represents the direction). Cars with horizontal orientation(1) can move only to the right(r) and left(l), cars with vertical orientation(0) can move only up(u) and down(d).

In oreder to run the game, run the next line in the command line - ‘python3 Game.py [path_to_json].
