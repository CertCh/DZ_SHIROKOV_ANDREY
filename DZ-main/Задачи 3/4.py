def blackjack(cards):
  card_values = {"Туз": 11, "Король": 10, "Дама": 10, "Валет": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
  total = sum([card_values[card] for card in cards])
  if total > 21:
    return True
  else:
    return False

cards = ["Туз", "Король", "5"]
print(blackjack(cards))
