#################################################################
# FILE : game.py
# WRITER : Adi Deshen
# EXERCISE : intro2cs1 ex9 2021
# DESCRIPTION: This program defines the Game class and runs a game.
#################################################################

from car import Car
from board import Board
from helper import *
import sys


class Game:
    """
    This is a class of the object game.
    Each game has a board.
    This class has 3 methods:
    1. user_input - This method checks if a user input is valid and returns True if it is and False if it isn't.
    2. __single_turn - This method run a single turn of the game. If it is possible it moves a car in a given direction.
       The method return True for success, false for a fail and "!" if the user want to end the game.
    3. play - This method run a game.
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board

    def user_input(self, input_list):
        """
        This function checks if a user input is valid and returns True if it is and False if it isn't.
        :param input_list: The user input.
        :return: True if it is valid and False if it isn't
        """
        if len(input_list) != 2 or len(input_list[0]) != 1 or len(input_list[1]) != 1:
            return False
        else:
            return input_list

    def __single_turn(self):
        """
        This function is a single turn of the game. If it is possible it moves a car in a given direction.
        :return: True a given move has been done, False if it isn't and "!" if the user inserts the input "!" in order
        to end the game.
        """
        print(self.board)
        user_input = input("Please tell me which car would you like to move and in which direction?")
        input_list = user_input.split(",")
        while not self.user_input(input_list):
            user_input = input("Please tell me which car would you like to move and in which direction?")
            input_list = user_input.split(",")
        legal_cars_name = ["Y", "B", "O", "G", "W", "R"]
        if user_input == "!":
            return user_input
        elif input_list[1] != "u" and input_list[1] != "d" and input_list[1] != "r" and input_list[1] != "l":
            print("I'm sorry, this is not a possible direction of movement. Please try again")
            return True
        elif input_list[0] not in legal_cars_name:
            print("I'm sorry, there's no such car on the board. Please try again")
            return True
        elif not self.board.possible_moves():
            print("I'm sorry, but there are no more possible moves")
            return False
        else:
            return self.board.move_car(input_list[0], input_list[1])

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        result = self.__single_turn()
        while self.board.cell_content(self.board.target_location()) is None:
            if result == "!":
                print("Thank you for playing. I hope to see you again!")
                return
            elif not result:
                print("This is not a valid input. Please try again")
                result = self.__single_turn()
                continue
            elif result:
                result = self.__single_turn()
                continue
        print("Congratulations, you won!!!")
        return


if __name__ == "__main__":
    game_board = Board()
    cars = load_json(sys.argv[1])
    legal_cars_name = ["Y", "B", "O", "G", "W", "R"]
    for c in cars:
        if c in legal_cars_name and 1 < cars[c][0] < 5:
            car = Car(c, cars[c][0], (cars[c][1][0] ,cars[c][1][1]), cars[c][2])
            game_board.add_car(car)
    our_game = Game(game_board)
    our_game.play()

