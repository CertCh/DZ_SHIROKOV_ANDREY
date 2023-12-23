def positive_neighbors(string):
  length = len(string)
  if length == 0:
    return False
  if length == 1:
    if string.isalpha():
      return False
    elif string == "+":
      return True
    else:
      return False
  if length >= 2:
    if string[0].isalpha():
      return False
    if string[-1].isalpha():
      return False
    for i in range(1, length - 1):
      if string[i].isalpha():
        if string[i - 1] != "+" or string[i + 1] != "+":
          return False
      else:
        continue
    return True

string = "+a+b+c+"
print(positive_neighbors(string))
