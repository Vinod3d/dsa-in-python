def LeftConPyramid(n):
    pattern = []
    for i in range(1, 2*n):
        line = ""
        if i <= n:
            line += " " * (n - i)
            line += "*" * i
        else:
            line += " " * (i - n)
            line += "*" * (2*n-i)
        pattern.append(line)
    
    return pattern
        




num = int(input("Enter number"))

pattern = LeftConPyramid(num)

for line in pattern:
    print(line)