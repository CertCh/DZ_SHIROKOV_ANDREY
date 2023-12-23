def two(word):
  for i in range(len(word) - 1):
    if word[i] == word[i + 1]:
      return True
  return False

word1 = "кот"
word2 = "конь"
word3 = "конный"

print(two(word1)) 
print(two(word2)) 
print(two(word3)) 
