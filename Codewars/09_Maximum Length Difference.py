def mxdiflg(a1, a2):
    if len(a1) == 0 or len(a2) == 0:
        return -1
    else:
        xmx = max(len(x1) for x1 in a1)
        xmn = min(len(x1) for x1 in a1)
        ymx = max(len(y1) for y1 in a2)
        ymn = min(len(y1) for y1 in a2)

        return max(xmx-ymn, ymx-xmn)

#https://www.codewars.com/kata/5663f5305102699bad000056