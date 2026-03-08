
def generateRightTriangle(n):
    list = []
    for i in range(1, n+1):
        line = '*' * i
        list.append(line)
    return list

n = int(input("Enter the number of rows: "))
list = generateRightTriangle(n)

for line in list:
    print(line)


# *
# **
# ***
# ****
# *****