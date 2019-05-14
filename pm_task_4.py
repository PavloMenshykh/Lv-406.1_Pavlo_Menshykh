#Задано чотирицифрове натуральне число. 
#Знайти добуток цифр цього числа.
#Записати число в реверсному порядку.
#Посортувати цифри, що входять в дане число

number = int(input("Enter your number as int:\n"))

splitstr = list(str(number))
splitstr.reverse()
st = "".join(splitstr)

intlist = []
for xx in str(number):
    intlist.append(int(xx))
intlist.sort()
strlist = []
for y in intlist:
    strlist.append(str(y))

sorted = "".join(strlist)

sum1 = 0
for x in str(number):
    sum1 += int(x)

print("Sorted digits are "+sorted)
print("Summ of numbers digits is "+str(sum1))
print("Reverse order is "+st)