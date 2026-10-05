prices = [100, 200, 300, 400, 500]

def menu():
    print("\n===== MENU ===")
    print("1. Add Item")
    print("2. Delete Item")
    print("3. Display Menu")
    print("4. Exit")

    while True:
        item = int(input("Enter your choice: "))

        if item == 1:
            add_price()
        elif item == 2:
            get_average_price()
        elif item == 3:
            get_max_price()
        elif item == 4:
            exit()
        else:
            print("Invalid choice. Please try again.")

def add_price():
    price = int(input("Enter price: "))
    prices.append(price)
    print(f"{price} added to price list.")

def get_average_price():
    get_average_price = lambda prices: sum(prices) / len(prices)
    print(get_average_price)
    

def get_max_price():
    max_price = max(prices)
    print(max_price)

menu()