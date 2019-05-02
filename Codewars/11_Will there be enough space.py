def enough(cap, on, wait):
    return(int(0 if cap-on-wait>0 else abs(cap-on-wait)))

#https://www.codewars.com/kata/5875b200d520904a04000003