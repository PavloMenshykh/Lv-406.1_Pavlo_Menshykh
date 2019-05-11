def sqInRect(lng, wdth):
    if  lng == wdth:
        return None
    else:
        squares = []
        while wdth != lng:
            if wdth>lng:
                wdth -= lng
                squares.append(lng)
            if lng>wdth:
                lng -= wdth
                squares.append(wdth)
        squares.append(wdth)
        
        return squares    

#https://www.codewars.com/kata/55466989aeecab5aac00003e