def multiplication_table(row,col):
    table = []
    first_row = []
    
    for i in range(1, col+1):
        first_row.append(i)
    
    for q in range(1, row+1):
        row = []
        for el in first_row:
            row.append(el*q)
        table.append(row)
        
    return table   

#https://www.codewars.com/kata/5432fd1c913a65b28f000342
#Create a function that accepts dimensions, of Rows x Columns, as parameters in order to create a multiplication table sized according to the given dimensions. **The return value of the function must be an array, and the numbers must be Fixnums, NOT strings.

