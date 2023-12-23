def al_eq(lst):
    max_len = max(len(s) for s in lst)
    new_lst = [s + "_" * (max_len - len(s)) for s in lst]
    return new_lst

print(al_eq(["всем", "привет", "hello"])) 
