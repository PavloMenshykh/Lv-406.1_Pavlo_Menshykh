# 1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел.

number = [4,67,5,3]

def avrg(*ark):
    return(sum(*ark)/len(*ark))

print(avrg(number))

# 2.  Написати функцію, яка повертає абсолютне значення числа

number2 = -4

def absv(nn):
    if nn < 0:
        return nn*-1
    else:
        return nn

print(absv(number2))

# 3.  Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.

number3 = 3
number4 = 7

def maxn(a,b):
    """Returns the larger of 2 numbers"""

    if a>b:
        return a
    else:
        return b

print(maxn(number3,number4))

# 4.  Написати програму, яка обчислює площу прямокутника, трикутника та кола (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)

import math

type_s = int(input("Please choose your option:\n 1 for block\n 2 for triangle\n 3 for circle\n"))

def block(a, b):
    return(a*b)

def triangle(a, b, c):
    p = a+b+c
    return((p*(p-a)*(p-b)*(p-c))**0.5)

def circle(a):
    return(math.pi*(a**2))

if type_s == 1:
    vala = float(input("Please enter dimention a:\n"))
    valb = float(input("Please enter dimention b:\n"))
    print("Block area is "+str(round(block(vala,valb),2)))
elif type_s == 2:
    vala = float(input("Please enter dimention a:\n"))
    valb = float(input("Please enter dimention b:\n"))
    valc = float(input("Please enter dimention c:\n"))
    print("Triangle area is "+str(round(triangle(vala,valb,valc),2)))
elif type_s == 3:
    vala = float(input("Please enter radius:\n"))
    print("Circle area is "+str(round(circle(vala),2)))

# 5.  Написати функцію, яка обчислює суму цифр введеного числа.

number5 = input("Please enter your number:\n")

def sumn (a):
    x = 0
    for num in a:
        x += int(num)
    return x

print("Sum of numbers: "+str(sumn(number5)))

# 6.  Написати програму калькулятор, яка складається з наступних функцій: 

# головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії, калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора, після виходу, користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!

def start(a):

    while True:

        try:
            var_a = float(input("Enter number 1:\n"))
            print("number 1 is " + str(var_a))
        except:
            print("Enter a numerical value")
        else:
            break

    while True:

        try:
            var_b = float(input("Enter number 2:\n"))
            print("number 2 is " + str(var_b))
        except:
            print("Enter a numerical value")
        else:
            break

    if a == 1:
        print("addition")
        print("Result is " + str(var_a + var_b))
    if a == 2:
        print("substraction")
        print("Result is " + str(var_a - var_b))
    if a == 3:
        print("multiplication")
        print("Result is " + str(var_a * var_b))
    if a == 4:
        print("division")
        print("Result is " + str(var_a / var_b))

while True:

    try:
        var_act = int(input("What do you want to do?\n\
        1) add\n\
        2) substract\n\
        3) multiply\n\
        4) divide\n\
        5) quit program\n"))
            
    except:
        print("Enter a integer value")
        continue

    if var_act > 0 and var_act <= 4: 
        start(var_act)
    elif var_act == 5:
        print("Thank you for using our software")
        quit()
    else:
        print("Choose correct option")