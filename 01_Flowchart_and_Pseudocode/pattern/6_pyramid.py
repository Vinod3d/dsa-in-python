# Vertical Pyramid Pattern

def pyramid(n):
	list = []
	for i in range(0, n):
		line = ""
		for j in range(0, n-i-1):
			line += " "
		for k in range(0, 2*i+1):
			line += "*"
		list.append(line)
	return list
		

n = int(input("Enter the number of row"))

list = pyramid(n)
for line in list:
	print(line)




