def count_happy_numbers(length):
  if length % 2 != 0 or length <= 0:
    return "Ошибка: длина числа должна быть четным положительным числом"
  count = 0
  half = length // 2
  for number in range(10 ** (length - 1), 10 ** length):
    string = str(number)
    left_sum = sum(int(char) for char in string[:half])
    right_sum = sum(int(char) for char in string[half:])
    if left_sum == right_sum:
      count += 1
  return count

length = 4
print(count_happy_numbers(length))
