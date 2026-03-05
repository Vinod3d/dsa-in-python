def RightConPyramid(n):
    pattern = []
    for i in range(1, 2*n):
        if i <= n:
            line = "* " * i
        else:
            line = "* " * (2*n - i)
        pattern.append(line)
    return pattern


num = int(input("Enter number"))

pattern = RightConPyramid(num)

for line in pattern:
    print(line)