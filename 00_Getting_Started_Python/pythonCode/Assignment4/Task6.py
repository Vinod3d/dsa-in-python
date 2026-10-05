# Task 6: Read File Safely 
import os

filename = input("Enter filename to open: ").strip()

if os.path.exists(filename):
    with open(filename, "r") as file:
        content = file.read()
        print("\n--- File Content ---")
        print(content)
else:
    print("File not found. Please check the filename.")