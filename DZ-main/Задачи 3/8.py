def password_strength(password):
  score = 0
  conditions = [
    any(char.isdigit() for char in password),
    any(char.islower() for char in password),
    any(char.isupper() for char in password),
    any(char in "!@#$%^&*()-+" for char in password),
    len(password) >= 8
  ]
  for condition in conditions:
    if condition:
      score += 1
  return score
password = "dota222!"

print(password_strength(password))
