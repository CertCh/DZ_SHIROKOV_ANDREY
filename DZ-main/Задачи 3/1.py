def rock_paper_scissors(player1, player2):
  rules = {"камень": "ножницы", "ножницы": "бумага", "бумага": "камень"}
  if player1 == player2:
    return "Ничья"
  elif rules[player1] == player2:
    return "Победил первый игрок"
  elif rules[player2] == player1:
    return "Победил второй игрок"
  else:
    return "Ошибка: неверные знаки"

player1 = "камень"
player2 = "бумага"

print(rock_paper_scissors(player1, player2))
