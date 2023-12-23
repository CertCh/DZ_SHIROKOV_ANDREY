def to_dict(lst):
    dct = {}
    for elem in lst:
        dct[elem] = elem
    return dct

lst = [1, 2, 3, "a", "b", "c"]
dct = to_dict(lst)
print(dct) 
