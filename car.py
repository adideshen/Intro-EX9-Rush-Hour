#################################################################
# FILE : car.py
# WRITER : Adi Deshen
# EXERCISE : intro2cs1 ex9 2021
# DESCRIPTION: This program defines the Car class.
#################################################################

class Car:
    """
    This is a class of the object car.
    Each car has a name, length, coordinates where it's placed, and whether it's placed horizontally or vertically.
    This class has 5 methods:
    1. car_coordinates - This method returns a list of coordinates the car is in.
    2. possible_moves - This method returns a dictionary of the possible moves of the car.
    3. movement_requirements - This method returns a list of cell locations which must be empty in order for a move to be legal.
    4. move - This method moves a car as wanted and returns true if the move had been done and false if not.
    5. get_name - This method returns the car's name.
    """

    def __init__(self, name, length, location, orientation) -> None:
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def car_coordinates(self) -> list:
        """
        :return: A list of coordinates the car is in
        """
        list_of_coordinates = []
        if self.orientation == 0:
            for i in range(self.length):
                list_of_coordinates.append((self.location[0] + i, self.location[1]))
        else:
            for i in range(self.length):
                list_of_coordinates.append((self.location[0], self.location[1] + i))
        return list_of_coordinates

    def possible_moves(self) -> dict:
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        possible_moves = {}
        if self.orientation == 0:
            possible_moves["u"] = "cause the car to move up"
            possible_moves["d"] = "cause the car to move down"
        if self.orientation == 1:
            possible_moves["l"] = "cause the car to move to the left"
            possible_moves["r"] = "cause the car to move to the right"
        return possible_moves

    def movement_requirements(self, movekey: str) -> list:
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        list_of_required_empty_cells = []
        if movekey == 'u':
            list_of_required_empty_cells.append((self.location[0] - 1, self.location[1]))
        elif movekey == 'd':
            list_of_required_empty_cells.append((self.location[0] + self.length, self.location[1]))
        elif movekey == 'l':
            list_of_required_empty_cells.append((self.location[0], self.location[1] - 1))
        elif movekey == 'r':
            list_of_required_empty_cells.append((self.location[0], self.location[1] + self.length))
        return list_of_required_empty_cells

    def move(self, movekey: str) -> bool:
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if movekey == "u":
            if self.orientation == 0:
                self.location = self.location[0] - 1, self.location[1]
                return True
            else:
                return False
        elif movekey == "d":
            if self.orientation == 0:
                self.location = self.location[0] + 1, self.location[1]
                return True
            else:
                return False
        elif movekey == "l":
            if self.orientation == 1:
                self.location = self.location[0], self.location[1] - 1
                return True
            else:
                return False
        elif movekey == "r":
            if self.orientation == 1:
                self.location = self.location[0], self.location[1] + 1
                return True
            else:
                return False

    def get_name(self) -> str:
        """
        :return: The name of this car.
        """
        return self.name
