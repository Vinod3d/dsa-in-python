
## Task 3
order = []
while True:
    print("1 - Add order")
    print("2 - Show orders")
    print("q - Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        order.append(int(input("Enter the order amount: ")))
    elif choice == "2":
        print(order)
    elif choice == "q":
        break
    else:
        continue