def merge_dict(dict_list):
    flat_dict = {}
    for dict in dict_list:
        for i, val in dict.items():
            if i in flat_dict:
                flat_dict[i] +=  val
            else:
                flat_dict[i] = val
    
    return flat_dict


dict_list = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]

print(merge_dict(dict_list))