def first_last(letter, st):
    letter = letter.lower()
    st = st.lower()
    first = None
    last = None
    for i in range(len(st)):
        if st[i] == letter:
            if first is None:
                first = i
            last = i
    return (first, last)
print(first_last("a", "Abracadabra")) 
print(first_last("z", "sdfsdf")) 
