def remove_enemies(names, enemies):
  result = []
  for name in names:
    if name not in enemies:
      result.append(name)
  return result

names = ["Andrey", "Bob", "Stepa", "David", "Krriss"]
enemies = ["Bob", "Krriss"]

print(remove_enemies(names, enemies))
