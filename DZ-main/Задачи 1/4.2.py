def change(lst):
    if lst and len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

print(change([1, 2, 3, 4])) 
print(change(["a", "b", "c"])) 
print(change([True])) 
