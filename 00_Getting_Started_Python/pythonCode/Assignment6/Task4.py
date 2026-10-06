filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        print("First 3 lines of the file:")
        for _ in range(3):
            line = file.readline()
            if not line:
                break
            print(line, end="")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

except PermissionError:
    print(f"Error: Permission denied to access '{filename}'.")

finally:
    print("\nFile operation attempted.")