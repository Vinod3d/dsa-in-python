def RightTriangle(n):
	pattern = []
	for i in range(1, n+1):
		space = ' ' * (n-i)
		star = '*' * i
		pattern.append(space + star)
	return pattern

num = int(input("Enter the number of row: "))

pattern = RightTriangle(num)
for line in pattern:
	print(line)