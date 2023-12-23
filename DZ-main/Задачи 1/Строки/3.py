def top3(st):
    freq = {}
    for c in st:  
        if c != " ":
            c = c.lower()
            freq[c] = freq.get(c, 0) + 1
    top = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3]
    result = ""
    for letter, count in top:
        result += f"{letter} - {count}, "
    result = result[:-2]
    return result

text = "Привет как дела норм ок"
print(top3(text)) 
