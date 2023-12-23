def remove_excess_punctuation(string):
  result = ""
  last_char = string[-1]
  if last_char == "?" or last_char == "!":
    result = last_char
    for char in string[-2::-1]:
      if char != last_char:
        result = char + result
      else:
        pass
  else:
    return string
  return result

string = "Кто ты???"
print(remove_excess_punctuation(string))
