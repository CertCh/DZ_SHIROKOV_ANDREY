def dislike_6(a):
    if isinstance(a, (int, float)):
        return "Только не 6!"
    else:
        return True

print(dislike_6(6)) 
print(dislike_6("6")) 
print(dislike_6(6.4)) 
