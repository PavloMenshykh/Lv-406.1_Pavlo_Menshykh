def round_to_next5(n):
    if n == 0:
        pass
    elif abs(n)%5 == 0:
        pass
    else:
        n =  n - n%5 + 5
    return n

#https://www.codewars.com/kata/55d1d6d5955ec6365400006d