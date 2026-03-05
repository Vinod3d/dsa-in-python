# This program generates a rectangle pattern of asterisks based on user input for rows and columns.
# def generateRectangle(row, col):
#     rectangle = []
#     for i in range(1, row + 1):
#         line = '*' * col
#         rectangle.append(line)
#     return rectangle

# row = int(input("Enter the number of rows: "))
# col = int(input("Enter the number of columns: "))

# rect = generateRectangle(row, col)

# for line in rect:
#     print(line)


# Optimized version without using a list to store the rectangle pattern
def generateRectangle(row, col):
    return ['*' * col for _ in range(row)]