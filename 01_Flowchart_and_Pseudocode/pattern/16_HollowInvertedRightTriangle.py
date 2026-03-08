
def HollowInvertedRightTriangle(n):
	pattern = []
	for i in range(n, 0, -1):
		line = ""
		if i == n:
			line = "*" * n
		else:
			for j in range(1, i+1):
				if j == 1 or j == i:
					line += "*"
				else:
					line += " "
		pattern.append(line)
	return pattern
			
		

num = int(input("Enter the number of row: "))

pattern = HollowInvertedRightTriangle(num)
for line in pattern:
	print(line)