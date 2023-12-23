def hacker_speak(input_string):
  replacements = {"А": "4", "Е": "3", "О": "0", "С": "(", "Т": "7"}
  output_string = ""
  for char in input_string:
    if char in replacements:
      output_string += replacements[char]
    else:
      output_string += char
  return output_string

input_string = "Привет, мир!" 
output_string = hacker_speak(input_string) 
print(output_string) 
