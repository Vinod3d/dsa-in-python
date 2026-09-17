price_dict={
    "Laptop":1000,
    "Mouse":10,
    "Keyboard":20,
    "Monitor":200,
    "Headphones":100,
    "Charger":50,
    "Bag":30,
    "USB Drive":20,
    "Mousepad":10,
    "Cable":5,
}

price_dict["RAM"] = 6000
price_dict["SSD"] = 8000
price_dict["Laptop"] = 12000
price_dict["Bag"] = 400
print("Updated price dictionary:")
print(price_dict)

# remove product
price_dict.pop("Charger")

average_price= lambda price_dict: sum(price_dict.values())/len(price_dict)
print("Average price of the products:", average_price(price_dict))

# without inbuilt function
def getMinimum(price_dict):
    min_price = price_dict[0]
    for price in price_dict:
        if price < min_price:
            min_price = price
    return min_price

def getMaximum(price_dict):
    max_price = price_dict[0]
    for price in price_dict:
        if price > max_price:
            max_price = price
    return max_price

print("Minimum price of the products:", getMinimum(price_dict))
print("Maximum price of the products:", getMaximum(price_dict))