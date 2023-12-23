def remove_stroki(string):
  string = string.strip()
  result = ""
  prev_space = False
  for char in string:
    if char != " ":
      result += char
      prev_space = False
    elif not prev_space:
      result += char
      prev_space = True
  return result

string = "  Это  пример   строки с   лишними  пробелами  "

print(remove_stroki(string))
