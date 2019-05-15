def areYouPlayingBanjo(name):
    if name[0] == "r" or name[0] == "R":
        name+=" plays banjo" 
    else:
        name+=" does not play banjo"
    return name

#https://www.codewars.com/kata/53af2b8861023f1d88000832
#Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!