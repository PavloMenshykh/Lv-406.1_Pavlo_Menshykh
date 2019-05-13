def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list

#https://www.codewars.com/kata/55ca43fb05c5f2f97f0000fd