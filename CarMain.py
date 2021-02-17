import CarClass as c1


def main():
    my_car = c1.Car(2020, "Ford")

    for i in range(5):
        my_car.accelerate()
        print(
            "Acceleration ", i + 1, ", the new speed is: ", my_car.get_speed(), sep=""
        )

    for i in range(5):
        my_car.brake()
        print("Brake ", i + 1, ", the new speed is: ", my_car.get_speed(), sep="")


main()