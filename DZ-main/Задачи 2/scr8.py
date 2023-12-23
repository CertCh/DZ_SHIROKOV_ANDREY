def reverser(string):
  result = ""
  for letter in string[::-1]:
    if letter.isupper():
      result += letter.lower()
    elif letter.islower():
      result += letter.upper()
    else:
      result += letter
  return result

string = "привет хахахха!"
print(reverser(string))
