def RightNumTriangle(n):
	numTriangle = []
	for i in range(1, n+1):
		line = f"{i}" * i
		numTriangle.append(line)
	return numTriangle



height = int(input("Enter the number of row: "))

pattern = RightNumTriangle(height)
for line in pattern:
	print(line)