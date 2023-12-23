def multiply_nums(input_string):
  numbers = input_string.split(", ")
  mul = 1
  for num in numbers:
    mul *= int(num)
  return mul


input_string = "2, 3, 4, 5" 
result = multiply_nums(input_string) 
print(result) 
