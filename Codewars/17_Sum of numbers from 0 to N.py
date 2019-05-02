def show_sequence(n):
    if n < 0:
        return(str(n)+"<0")
    elif n == 0:
        return("0=0")
    else: 
        series=range(0, n+1)
        tt = 0
        listt = "0"
        for nn in series:
            tt += nn
            if nn>0:
                listt+=("+"+str(nn))
            
        return(listt+" = "+str(tt))

#https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763