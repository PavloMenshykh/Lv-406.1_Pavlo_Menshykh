#1.  Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне, чи введені дані коректні.
"""
while True:
    try:
        number = input("Please enter an integer:\n")
        number.isdigit() == True
        print(number+" is even") if int(number)%2 == 0 else print(number+" is odd")
    except ValueError:
        print("Please enter an integer")
    else:
        break
"""
#2.  Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить повідомлення про те чи вік є парним чи непарним числом. 
# Необхідно передбачити можливість введення від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію. 
# Головний код має викликати функцію, яка обробляє введену інформацію.
"""
def agetype(age):
    print(age+" is even") if int(age)%2 == 0 else print(age+" is odd")

class AgeError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

while True:

    try:
        age = input("Please enter your age as positive integer:\n")
        if age.isdigit() == True:   
            if int(age)<1 or int(age)>120:
                raise AgeError("Please enter a legit age")
            else:
                agetype(age)
        else:
            raise AgeError("Please enter a digit")
            
    except AgeError as ae:
        print(ae.data)
    else:
        break
"""
#3.  Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, 
# передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій. 
# Використати блоки else та finaly.
"""
numbers = input("Please enter two digits seperated by a coma:\n")

try:
    # vals = numbers.split(",")
    # number1 = int(vals[0])
    # number2 = int(vals[1])
    # rslt = number1%number2
    number1, number2 = eval(numbers)
    rslt = int(number1)%int(number2)
except ZeroDivisionError:
    print("Second number is zero, you can't divide by zero")
except ValueError:
    print("Please eneter digits")
else:
    print(rslt)
finally:
    print("code has been executed")
"""
#4.  Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, 
# який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) . 
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.

class WeeksError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

wdlookup = ["blank", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


while True:
    try:
        usrinpt = input("Please enter a number from 1 to 7 to find corresponding week day:\n")
        if usrinpt.isdigit() == True:
            if int(usrinpt)<1 or int(usrinpt)>7:
                raise WeeksError("Please enter a number from 1 to 7")
            else:
                print(wdlookup[int(usrinpt)])
        else:
            raise WeeksError("Please enter a number")
    except WeeksError as we:
        print(we.data)
    else:
        break