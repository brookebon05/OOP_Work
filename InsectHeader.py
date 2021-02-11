import random
from datetime import date


class Insect:
    def __init__(self, w, l, f):
        self.__wings = w
        self.__legs = l
        self.__flight_length1 = f

    def flight_length(self):
        self.__flight_length1 = random.randint(1, 10)
        return self.__flight_length1

    def get_wings(self):
        return self.__wings

    def get_legs(self):
        return self.__legs

    """
    def __str__(self):
        return print(
            "Wings: ",
            self.__wings,
            "\n",
            "legs: ",
            self.__legs,
            "\n",
            "Flight: ",
            str(self.__flight_length1),
        )
    """
