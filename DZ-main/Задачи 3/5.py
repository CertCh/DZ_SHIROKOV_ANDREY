def sum_of_numbers(string):
  current_number = ""
  total = 0
  for char in string:
    if char.isdigit():
      current_number += char
    else:
      if current_number != "":
        total += int(current_number)
        current_number = ""
  if current_number != "":
    total += int(current_number)
  return total

string = "abc123def45ghi6"
print(sum_of_numbers(string))
