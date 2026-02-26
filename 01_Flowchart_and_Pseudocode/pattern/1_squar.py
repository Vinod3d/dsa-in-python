# seudo code
# 1. Start
# 2. Get the number of rows and columns from the user
# 3. For each row from 1 to number of rows
#    a. For each column from 1 to number of columns
#       i. Print the current row number
#    b. Move to the next line
# 4. End

def print_square_pattern(n):
    square = []
    for i in range(1, n):
        row = '*' * n
        square.append(row)
    return square

n = int(input("Enter the number of rows and columns: "))
pattern = print_square_pattern(n)
for line in pattern:
    print(line)