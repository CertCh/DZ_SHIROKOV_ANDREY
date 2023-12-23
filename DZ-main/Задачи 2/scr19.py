def get_accumulated_array(input_list):
  output_list = []
  current_sum = 0
  for num in input_list:
    current_sum += num
    output_list.append(current_sum)
  return output_list

input_list = [1, 2, 3, 4, 5] 
output_list = get_accumulated_array(input_list) 
print(output_list) 
