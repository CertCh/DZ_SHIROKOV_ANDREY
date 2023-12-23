def shortener(st):
    result = ""
    level = 0
    for c in st:
        if c == "(":
            level += 1
        elif c == ")":
            level -= 1
        elif level == 0:
            result += c
    return result

text = "я написал, (это) но об этом не узнают"
print(shortener(text)) 
