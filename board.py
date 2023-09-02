#################################################################
# FILE : board.py
# WRITER : Adi Deshen
# EXERCISE : intro2cs1 ex9 2021
# DESCRIPTION: This program defines the Board class.
#################################################################

from car import Car
from copy import deepcopy

class Board:
    """
    This is a class of the object board.
    Each board has a size, graphic display and list of objects from type cars that are in the it.
    This class has 7 methods:
    1. __str__ - This method returns the graphic display of the board.
    2. cell_list - This method returns a list of coordinates of the board's list.
    3. possible_moves - This method returns a list of tuples representing legal moves of all of the cars that are in
       the board.
    4. target_location - This method returns the coordinate of the target cell.
    5. cell_content - This method returns the content of a cell - None if there isn't a car in it, the car name if it's
       in it.
    6. add_car - This method adds a car to the board and returns True upon success, False if failed.
    7. move_car - This method moves a car in a given direction and returns True upon success, False otherwise.
    """

    def __init__(self) -> None:
        self.size = 7
        row = self.size * ["_"]
        self.board = []
        for r in range(self.size):
            self.board.append(deepcopy(row))
        for row in range(self.size):
            if row != (self.size//2):
                self.board[row].append("*")
            else:
                self.board[row].append("E")
        self.cars = []

    def __str__(self) -> str:
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        str_board = ""
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                str_board = str_board + self.board[row][col]
            str_board = str_board + '\n'
        return str_board


    def cell_list(self) -> list:
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        list_of_coordinates = []
        for row in range(len(self.board)):
            for col in range(len(self.board[0]) - 1):
                list_of_coordinates.append((row, col))
        list_of_coordinates.append(self.target_location())
        return list_of_coordinates


    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        possible_moves = []
        for car in self.cars:
            for move in car.possible_moves():
                counter = 0
                for cell in car.movement_requirements(move):
                    if self.cell_content(cell) is None and cell in self.cell_list():
                        counter += 1
                if counter == len(car.movement_requirements(move)):
                    possible_moves.append((car.get_name(), move, car.possible_moves()[move]))
        return possible_moves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return self.size//2, self.size


    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        if coordinate in self.cell_list():
            if self.board[coordinate[0]][coordinate[1]] == "_" or self.board[coordinate[0]][coordinate[1]] == "E":
                return None
            else:
                return self.board[coordinate[0]][coordinate[1]]
        else:
            return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        for c in self.cars:
            if c.get_name() != car.get_name():
                continue
            else:
                return False
        for coordinate in car.car_coordinates():
            if coordinate in self.cell_list() and self.cell_content(coordinate) is None:
                continue
            else:
                return False
        for coordinate in car.car_coordinates():
            self.board[coordinate[0]][coordinate[1]] = car.get_name()
        self.cars.append(car)
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for car in self.cars:
            if car.get_name() == name:
                if movekey in car.possible_moves():
                    for cell in car.movement_requirements(movekey):
                        if cell in self.cell_list() and (self.board[cell[0]][cell[1]] == "_" or self.board[cell[0]][cell[1]] == "E"):
                            continue
                        else:
                            return False
                    for cell in car.movement_requirements(movekey):
                        self.board[cell[0]][cell[1]] = car.get_name()
                    car_coordinates = car.car_coordinates()
                    if movekey == "u" or movekey == "l":
                        self.board[car_coordinates[-1][0]][car_coordinates[-1][1]] = "_"
                    elif movekey == "r" or movekey == "d":
                        self.board[car_coordinates[0][0]][car_coordinates[0][1]] = "_"
                    car.move(movekey)
                    return True
                else:
                    return False
        else:
            return False
