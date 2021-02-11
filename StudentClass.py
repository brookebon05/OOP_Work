import datetime


class Student:
    def __init__(self, year, month, day, class1):
        self.studID = 123456789
        self.dob = datetime.datetime(year, month, day)
        self.name = "Blank name"
        self.classification = class1
        self.age = 0
        self.register_date = "No date"

    def get_age(self):
        today = datetime.datetime.today()
        self.age = (today - self.dob) / 365
        return self.age

    def get_register_date(self):
        if self.classification == "FR":
            self.register_date = "11/10-11/12"
        elif self.classification == "SO":
            self.register_date = "11/7-11/9"
        elif self.classification == "JR":
            self.register_date = "11/4-11/6"
        elif self.classification == "SR":
            self.register_date = "11/1-11/3"
        else:
            print("Please try entering your classification in the right form.")
        return self.register_date
