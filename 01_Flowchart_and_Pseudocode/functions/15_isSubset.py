def isSubset(lst1, lst2):
    for num in lst1:
        if num not in lst2:
            return False
    return True

lst1 = [1, 2, 9]
lst2 = [1, 2, 3, 4, 5, 6]

print(isSubset(lst1, lst2))