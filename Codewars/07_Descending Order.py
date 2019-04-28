def Descending_Order(num):
    nlist = []
    for number in str(num):
        nlist.append(number)

    nlist.sort(reverse=True)

    return(int("".join(nlist))) 

#https://www.codewars.com/kata/5467e4d82edf8bbf40000155