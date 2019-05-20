def expanded_form(num):
    number = str(num)[::-1]
    
    zeros = 0
    numbers = []
    
    for nn in number:
        numbers.append(nn+"0"*zeros)
        zeros += 1
    
    numbcor = numbers[::-1]
    clean = numbcor[0]
        
    for n in numbcor[1:]:
        if int(n) != 0:
            clean += " + "+n
     
    return clean

#https://www.codewars.com/kata/5842df8ccbd22792a4000245
#You will be given a number and you will need to return it as a string in Expanded Form.
