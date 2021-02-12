import CellPhoneClass as c


def main():
    my_cell = c.Cellphone("Samsung", "4S", "$302")

    # Print old phone
    print("Manufacturer is: ", my_cell.get_manufact())
    print("Model is: ", my_cell.get_model())
    print("Price is: ", my_cell.get_price())

    # Make new phone
    my_cell.set_manufact("Apple")
    my_cell.set_model("8S")
    my_cell.set_retail_price("$500")

    # Print new phone
    print("New manufacturer is: ", my_cell.get_manufact())
    print("New model is: ", my_cell.get_model())
    print("New price is: ", my_cell.get_price())


main()