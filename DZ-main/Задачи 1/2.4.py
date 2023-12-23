def radius(X):
    # V = 4/3 * pi * r^3
    # r = (3 * V / (4 * pi))^(1/3)
    return (3 * X / (4 * 3.14)) ** (1/3)
print(radius(100))
print(radius(500)) 
