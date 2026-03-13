def rotateList(lst, k):
    if len(lst) == 0:
        return []
    n = len(lst)
    k = k % n

    idx = n - k
    rA = []
    for i in range(idx, n):
        rA.append(lst[i])
    for i in range(idx):
        rA.append(lst[i])
    return rA


    
     
list = [10, 20, 30, 40, 50]

print(rotateList(list, k = 3))