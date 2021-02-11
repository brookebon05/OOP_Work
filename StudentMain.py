import StudentClass as s


def main():
    year1 = int(input("Please enter your birth year in form: YYYY "))
    month1 = int(input("Please enter your birth month in form: MM "))
    day1 = int(input("Please enter your birth day in form: DD "))
    class1 = input("Please enter your classification in form: FR, SO, JR, SR: ")

    student1 = s.Student(year1, month1, day1, class1)
    print("Age in years: ", student1.get_age())
    print(
        "Due to your classification as a ",
        class1,
        " your registering dates are: ",
        student1.get_register_date(),
    )


main()