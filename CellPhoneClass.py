class Cellphone:
    def __init__(self, brand, model, price):
        self.__manufact = brand
        self.__model = model
        self.__retail_price = price

    def set_manufact(self, new_manu):
        self.__manufact = new_manu

    def set_model(self, new_model):
        self.__model = new_model

    def set_retail_price(self, new_price):
        self.__retail_price = new_price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__retail_price
