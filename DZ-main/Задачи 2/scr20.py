def is_increasing(input_list):
  for i in range(1, len(input_list)):
    if input_list[i] < input_list[i-1]:
      return False
  return True

input_list = [1, 2, 3, 4, 5] 
result = is_increasing(input_list) 
print(result) 
