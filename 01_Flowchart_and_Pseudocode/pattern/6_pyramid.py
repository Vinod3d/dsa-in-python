# Vertical Pyramid Pattern

def pyramid(n):
	pyramid = []
	for i in range(1, n+1):
		star = '*' * (2*i-1)
		space = ' ' * (n-i)

		pyramid.append(space + star + space)
	return pyramid
		

n = int(input("Enter the number of row"))

pattern = pyramid(n)
for line in pattern:
	print(line)




