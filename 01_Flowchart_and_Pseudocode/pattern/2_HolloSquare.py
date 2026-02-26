def HolloSquare(n):
    if n < 3:
        return "Number must be at least 2 to form a hollow square."
    square = []
    for i in range(1, n + 1):
        if i == 1 or i == n:
            row = '*' * n
        else:
            row = '*' + ' ' * (n - 2) + '*'
        square.append(row)

    for line in square:
        print(line)


num = int(input("Enter the number of rows and columns: "))

print(HolloSquare(num))