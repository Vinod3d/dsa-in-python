def SandGlass(n):
	pattern = []

	# Upper half
	for i in range(n):
		star = '*' * (2*(n-i)-1)
		space = ' ' * i
		pattern.append(space + star)

	# Lower half
	for i in range(1, n):
		star = '*' * (2 * i + 1)
		space = ' ' * ( n - i - 1 )
		pattern.append(space + star)
	
	return pattern

num = int(input("Enter the number of row: "))

pattern = SandGlass(num)
for line in pattern:
	print(line)