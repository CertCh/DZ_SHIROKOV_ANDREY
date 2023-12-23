def number_to_russian(number):
  units = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
  tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
  hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
  special_cases = {10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"}
  result = ""
  if 0 <= number <= 9:
    return units[number]
  if 10 <= number <= 19:
    return special_cases[number]
  if 20 <= number <= 99:
    ten_index = number // 10
    unit_index = number % 10
    if unit_index == 0:
      return tens[ten_index]
    else:
      return tens[ten_index] + " " + units[unit_index]
  if 100 <= number <= 999:
    hundred_index = number // 100
    remainder = number % 100
    if remainder == 0:
      return hundreds[hundred_index]
    else:
      return hundreds[hundred_index] + " " + number_to_russian(remainder)

number = 123
print(number_to_russian(number))
