import RetailItemClass as ret


def main():
    # Create jacket
    jacket = ret.RetailItem("Jacket", 12, "$59.95")
    print(jacket.get_retail_item())

    # Create Designer jeans
    des_jeans = ret.RetailItem("Designer Jeans", 40, "$34.95")
    print(des_jeans.get_retail_item())

    # Create shirt
    shirt = ret.RetailItem("Shirt", 20, "$24.95")
    print(shirt.get_retail_item())


main()