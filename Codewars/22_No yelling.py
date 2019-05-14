def filter_words(st):
    lr = st.lower()
    lr2 = lr.upper()[0]+lr[1:]
    lr3 = lr2.split()
    return " ".join(lr3)

#https://www.codewars.com/kata/587a75dbcaf9670c32000292
#Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing. String should be capitalized and properly spaced. Using re and string is not allowed.