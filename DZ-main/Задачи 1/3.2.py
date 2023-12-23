def help_bool(letter):
    rules = {
        "к": "Коммутативность: A and B == B and A, A or B == B or A",
        "а": "Ассоциативность: (A and B) and C == A and (B and C), (A or B) or C == A or (B or C)",
        "д": "Дистрибутивность: A and (B or C) == (A and B) or (A and C), A or (B and C) == (A or B) and (A or C)",
        "м": "Правило де Моргана: not (A and B) == not A or not B, not (A or B) == not A and not B"
    }
    if letter in rules:
        return rules[letter]
    else:
        return "Введите одну из букв: к, а, д, м, чтобы получить правило для логических операций"

print(help_bool(input('Введите одну из букв: к, а, д, м, чтобы получить правило для логических операций: '))) 
