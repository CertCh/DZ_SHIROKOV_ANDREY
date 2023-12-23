def get_median(input_array):
  input_array.sort()
  n = len(input_array)
  if n % 2 == 0:
    i = n // 2 - 1
    j = n // 2
    median = (input_array[i] + input_array[j]) / 2
  else:
    i = n // 2
    median = input_array[i]
  return median

input_array = [5, 3, 7, 9, 1] 
median = get_median(input_array) 
print(median) 
