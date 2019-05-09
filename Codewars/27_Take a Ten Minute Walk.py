def isValidWalk(walk):
    vert = 0
    hor = 0
    if len(walk)!=10:
        return False
    else:
        for wk in walk:
            if wk == "n":
                vert += 1
            if wk == "s":
                vert -= 1
            if wk == "w":
                hor += 1
            if wk == "e":
                hor -= 1
        if vert == 0 and hor == 0:
            return True
        else:
            return False

#https://www.codewars.com/kata/54da539698b8a2ad76000228