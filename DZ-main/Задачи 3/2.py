def divide_coins(coins):
  total = sum(coins)
  if total % 3 == 0:
    return True
  else:
    return False

coins = [1, 2, 3, 4, 5, 6]
print(divide_coins(coins))
