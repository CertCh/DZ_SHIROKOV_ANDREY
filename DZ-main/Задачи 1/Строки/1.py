def search_substr(subst, st):
    subst = subst.lower()
    st = st.lower()
    if subst in st:
        return "Есть контакт!"
    else:
        return "Мимо!"
print(search_substr("дз", "дз по прогг")) 
print(search_substr("алгебра", "дз по прогг")) 
