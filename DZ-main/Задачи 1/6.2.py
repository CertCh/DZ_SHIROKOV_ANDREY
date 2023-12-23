def biggest_dict(**kwargs):
    my_dict = {"first_one": "we can do it"}
    for key, value in kwargs.items():
        my_dict[key] = value
    return my_dict

dct = biggest_dict(a=1, b=2, c=3, d=4, e=5)
print(dct)
