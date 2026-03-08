def RightHollowTriangle(n):
	pattern = []
	for i in range(1, n+1):
		line = ''
		if i == n:
			line =  "*" * n
		else:
			for j in range(1, i+1):
				if j == 1 or i == j:
					line += '*'
				else:
					line += ' '
		pattern.append(line)
	return pattern
		

num = int(input("Enter the number of row: "))

pattern = RightHollowTriangle(num)
for line in pattern:
	print(line)