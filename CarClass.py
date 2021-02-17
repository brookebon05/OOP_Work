class Car:
    def __init__(self, year1, make1):
        self.__year_model = year1
        self.__make = make1
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
        # return print("Speed was set to: ", self.__speed)

    def brake(self):
        self.__speed -= 5
        # return print("Speed was set to: ", self.__speed)

    def get_speed(self):
        return self.__speed
