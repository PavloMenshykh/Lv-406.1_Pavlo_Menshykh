def encrypter(strng):
    lookup = "abcdefghijklmnopqrstuvwxyz"
    rotted = lookup[13:] + lookup[:13]

    rslt = ""

    for cc in strng:
        if cc.isalpha() == True:
            nn = rotted.find(cc.lower())
            if cc.isupper() == True:
                rslt += lookup[nn].upper()
            else:
                rslt += lookup[nn]
        else:
            rslt += cc

    rslt2 = ""

    for c in rslt:
        if c.isalpha() == True:
            n = lookup.find(c.lower())
            if c.isupper() == True:
                rslt2 += lookup[-n-1].upper()
            else:
                rslt2 += lookup[-n-1]
        else:
            rslt2 += c

    return rslt2

#https://www.codewars.com/kata/56fb3cde26cc99c2fd000009