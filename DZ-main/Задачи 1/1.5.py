def list_sort(lst):
    lst.sort(key=abs, reverse=True)
    return lst

print(list_sort([1, -5, 3, -2, 4]))
