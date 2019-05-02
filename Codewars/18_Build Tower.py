def tower_builder(n_floors):
    block = "*"
    start = "'"
    
    twr = []
    
    cnt = n_floors
    while cnt > 0:
        twr.append(" "*(cnt-1)+block*(1+(n_floors-cnt)*2)+" "*(cnt-1))
        cnt -= 1
        
    return(twr)

#https://www.codewars.com/kata/576757b1df89ecf5bd00073b