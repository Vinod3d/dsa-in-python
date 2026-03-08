def NumberPyramid(n):
	pattern = []
	for i in range(1, n+1):
		line = ""
		space = " " * (n - i)
		for j in range(1, i+1):
			if j == i:
				line += str(j)
			else:
				line += str(j) + " "
		pattern.append(space + line + space)
	return pattern

num = int(input("Enter the number of row: "))

pattern = NumberPyramid(num)
for line in pattern:
	print(line)