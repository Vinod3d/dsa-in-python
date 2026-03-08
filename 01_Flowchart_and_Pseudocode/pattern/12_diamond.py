def Diamond(h):
	pattern = []
	for i in range(1, 2*h):
		space = ' ' * (h-i) if i < h else ' ' * (i-h)
		star = '*' * (2*i-1) if i < h else '*' * (2*(2*h-i )-1)
		pattern.append(space + star)
	return pattern
		
	
	

height = int(input("Enter the number of row: "))

pattern = Diamond(height)
for line in pattern:
	print(line)
	

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *