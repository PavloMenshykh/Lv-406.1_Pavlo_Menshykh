def filter_words(st):
    lr = st.lower()
    lr2 = lr.upper()[0]+lr[1:]
    lr3 = lr2.split()
    return " ".join(lr3)

#https://www.codewars.com/kata/587a75dbcaf9670c32000292