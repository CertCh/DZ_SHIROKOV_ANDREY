dct = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(id(dct))
first_value = dct["a"]
last_value = dct["e"]
dct["a"] = last_value
dct["e"] = first_value
del dct["b"]
dct["new_key"] = "new_value"
print(dct)
print(id(dct))
