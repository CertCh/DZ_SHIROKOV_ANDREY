def useless(s):
  if len(s) > 0:
    max_s = max(s)
    result = max_s / len(s)
    return result
  else:
    return None

test_s = [1, 2, 3, 4, 5]
print(useless(test_s))
