
def cleaned_str(st):
    chars = []
    for c in st:
        if c != "@":
            chars.append(c)
        elif chars:
            chars.pop()
    return "".join(chars)
text = "гр@оо@лк@оц@ва"
print(cleaned_str(text))