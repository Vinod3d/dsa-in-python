import os

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")
choice = int(input("Enter your choice: "))

if choice == 1:
    filename = input("Enter the filename: ")
    with open(filename, "w") as f:
        f.write(input("Enter the content: "))
elif choice == 2:
    filename = input("Enter the filename: ")
    with open(filename, "r") as f:
        print(f.read())
elif choice == 3:
    filename = input("Enter the filename: ")
    with open(filename, "a") as f:
        f.write(input("Enter the content: "))
elif choice == 4:
    filename = input("Enter the filename: ")
    os.remove(filename)
else:
    print("Invalid choice")
