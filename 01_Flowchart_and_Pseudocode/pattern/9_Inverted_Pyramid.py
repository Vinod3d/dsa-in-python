
def InvertedPyramid(n):
	pyramid = []
	for i in range(n, 0, -1):
		star = "*" * (2*i-1)
		space = " " * (n-i)
		pyramid.append(space+star+space)
	return pyramid


n = int(input("Enter the number of row: "))

pattern = InvertedPyramid(n)
for line in pattern:
	print(line)