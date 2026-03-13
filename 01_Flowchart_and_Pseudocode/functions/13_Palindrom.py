def palindrom(lst):
    ori = list(lst)
    rev = []
    length = len(lst)
    for i in range(length-1, -1, -1):
        rev.append(lst[i])
    return ori == rev

my_list = ('a', 'b', 'c', 'b', 'a')

print(palindrom(my_list))