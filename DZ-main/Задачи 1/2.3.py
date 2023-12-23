def mul_to_int(a, b):
    product = a * b
    if product == int(product):
        return int(product)
    else:
        return product

print(mul_to_int(2, 3)) 
print(mul_to_int(2.5, 4)) 
print(mul_to_int(2.5, 1.5)) 
