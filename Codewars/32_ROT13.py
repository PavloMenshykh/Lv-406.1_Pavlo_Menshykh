def rot13(message):
    lookup = "abcdefghijklmnopqrstuvwxyz"
    rotted = lookup[13:] + lookup[:13]

    rslt = ""

    for cc in message:
        if cc.isalpha() == True:
            nn = rotted.find(cc.lower())
            if cc.isupper() == True:
                rslt += lookup[nn].upper()
            else:
                rslt += lookup[nn]
        else:
            rslt += cc

    return rslt

#https://www.codewars.com/kata/52223df9e8f98c7aa7000062