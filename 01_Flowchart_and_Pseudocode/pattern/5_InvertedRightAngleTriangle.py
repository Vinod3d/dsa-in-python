def InvertedRightAngleTriangle(n):
    list = []
    for i in range(n, 0, -1):
        line = '*' * i
        list.append(line)
    return list

n = int(input("Enter the number of rows: "))
list = InvertedRightAngleTriangle(n)

for line in list:
    print(line)