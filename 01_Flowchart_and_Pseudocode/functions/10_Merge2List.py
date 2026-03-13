def mergeList(k, v):
    if len(keys) != len(values):
        return False
    dict = {}
    for i in range(len(keys)):
        dict[keys[i]] = values[i]
    return dict
        



keys = ['a', 'b', 'c']
values = [1, 2, 3]

print(mergeList(keys, values))