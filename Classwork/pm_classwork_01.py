#1.  Написати скрипт, який з двох введених чисел визначить, яке з них більше, а яке менше.

number1 = float(input("input number 1:\n"))
number2 = float(input("input number 2:\n"))

if number1 == number2:
    print("Values are equal")
else:
    print(str(number1)+" is bigger" if number1>number2  else str(number2)+" is bigger")
    
#2.  Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне повідомлення.

number = int(input("Enter your number:\n"))

print(str(number)+" is even" if number/2 == number//2  else str(number)+" is odd")

#3.  Написати скрипт, який обчислить факторіал введеного числа.

#with import

from math import factorial
print("Number factorial is "+str(factorial(int(input("Enter your number as int:\n")))))

#with loop

numlist = range(int(input("Enter your number as int:\n"))+1)[1::]
result = numlist[0]

for x in numlist: 
     result = result * x  
print("Number factorial is "+str(result)) 

#4.  Написати скрипт, який знайде найбільший спільний дільник НСД та найменше спільне кратне НСК двох чисел.

number1 = int(input("Enter your number as int:\n"))
number2 = int(input("Enter your number as int:\n"))

def nsd1(num):
    listd = []
    for x in range(1,num+1):
        if num%x == 0:
            listd.append(x)
    return(listd)

nsd2 = []
for xx in nsd1(number1):
    if xx in nsd1(number2):
        nsd2.append(xx)

print("Largest common divider is "+str(max(nsd2)))
print("Smallest common multiple is "+str(int((number1*number2)/max(nsd2))))