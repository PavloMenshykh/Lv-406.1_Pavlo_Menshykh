def is_uppercase(inp):
    if any(c.islower() == True for c in inp):
        return False
    else:
        return True

#https://www.codewars.com/kata/56cd44e1aa4ac7879200010b
#Create a method is_uppercase() to see whether the string is ALL CAPS. 