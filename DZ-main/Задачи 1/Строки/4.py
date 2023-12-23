def camel(st):
    result = ""
    upper = True
    for c in st:
        if c.isalpha():
            if upper:
                c = c.upper()
                upper = False
            else:
                c = c.lower()
                upper = True
        result += c
    return result

text = "ааа я устал уже"
print(camel(text)) 
