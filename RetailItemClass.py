class RetailItem:
    def __init__(self, desc, units, price):
        self.__item_desc = desc
        self.__units = units
        self.__price = price

    def get_retail_item(self):
        return (
            "Item: ",
            self.__item_desc,
            "Number units: ",
            self.__units,
            "Price: ",
            self.__price,
        )
