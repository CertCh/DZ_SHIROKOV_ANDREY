button_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
def button_presses(message):
  message = message.upper()
  presses = []
  for letter in message:
    if letter in button_dict:
      presses.append(button_dict[letter])
    elif letter == " ":
      presses.append(0)
    else:
      pass
  return presses
message = "Hello World"

print(button_presses(message))
