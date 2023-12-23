def to_float(num):
    try:
        return float(num)
    except ValueError:
        return "Невозможно преобразовать"
print(to_float(10)) 
print(to_float("3.14")) 
print(to_float("ааа кек ща ощшибка будет")) 
