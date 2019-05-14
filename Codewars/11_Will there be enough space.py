def enough(cap, on, wait):
    return(int(0 if cap-on-wait>0 else abs(cap-on-wait)))

#https://www.codewars.com/kata/5875b200d520904a04000003
#You have to write a function that accepts three parameters:
#cap is the amount of people the bus can hold excluding the driver.
#on is the number of people on the bus.
#wait is the number of people waiting to get on to the bus.
#If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.