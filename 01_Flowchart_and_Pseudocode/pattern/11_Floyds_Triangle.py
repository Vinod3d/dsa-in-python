def floydTriangle(n):
	pattern = []
	IncrNum = 0
	for i in range(1, n+1):
		line = ""
		for j in range(i):
			IncrNum+=1
			line += str(IncrNum) + " "
		pattern.append(line.strip())
	return pattern
		

numRow = int(input("Enter the number of row: "))

pattern = floydTriangle(numRow)
for line in pattern:
	print(line)