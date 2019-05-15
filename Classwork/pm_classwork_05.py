import pyowm
city=input("What city you are interested:\n")
owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')    

observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature=w.get_temperature('celsius')['temp']

print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius")
print("In this city "+ w.get_detailed_status()+", wind speed is "+str(w.get_wind()["speed"])+"m/s, humidity is "+str(w.get_humidity())+"%.")


# 1.  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 
# і пропонує користувачу вгадати це число. Програма зчитує числа, які вводить користувач і 
# видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем. 
# Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, тоді друкує повідомлення привітання. 
# (для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())


print("Greetings, a random integer from 1 to 100 has been generated, can you guess it ?\n")

import random

zahadka = random.randint(1, 101)

while True:
    value = int(input("Enter your number:\n"))
    if value==zahadka:
        print("You have guessed correctly !! number is "+str(zahadka))
        break
    elif value>zahadka:
        print("Try a smaller number")
    elif value<zahadka:
        print("Try a larger number")


# 2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
#(для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).

from math import pow
from math import pi

type_s = int(input("Please choose your option:\n 1 for block\n 2 for triangle\n 3 for circle\n"))

def block(a, b):
    return(a*b)

def triangle(a, b, c):
    p = a+b+c
    return((p*(p-a)*(p-b)*(p-c))**0.5)

def circle(a):
    return(pi*(a**2))

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