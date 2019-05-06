# 1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

listnn = input("Enter list of int numbers seperated by commas:\n")

listn = listnn.split(",")
print("Max number="+str(max(listn))+", min number="+str(min(listn)))

# 2.  В інтервалі від 1 до 10 визначити числа 
#  парні, які діляться на 2,
#  непарні, які діляться на 3, 
#  числа, які не діляться на 2 та 3.

base = range(11)
even = [x for x in base if x%2==0]
oddmul3 = [x for x in base if x%3==0]
other = [x for x in base if x%2!=0 and x%3!=0]

print(even)
print(oddmul3)
print(other)

# 3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції) 

inputn = int(input("Enter an integer value > 0:\n"))
if inputn < 0:
    print("Enter a valid number next time")
elif inputn == 0:
    print("Factorial is 1")
else:
    fact = [x for x in range(0,inputn+2)]

    i = 0
    factorial = [1]
    while i < inputn:
        factorial.append(factorial[i]*fact[i+1])
        i += 1

    print("Factorial is "+str(max(factorial))) 

# 4.  Напишіть скрипт, який перевіряє логін, який вводить користувач. 
#Якщо логін вірний (First), то привітайте користувача. 
#Якщо ні, то виведіть повідомлення про помилку. 
#(використайте цикл while)

while True:
    login = input("Please enter your login:\n")
    if login == "First":
        print("Greetings "+login)
        break
    else:
        print("Enter a valid login")

# 5.  Перший випадок. 
#Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число. При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

while 2 > 1:
    if int(input("Please enter your number:\n"))>0:
        pass
    else:
        break

# 6.  Другий випадок. 
# На початку на вхід подається кількість елементів послідовності, а потім самі елементи. При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

numofelem = int(input("Please enter quantity of numbers:\n"))
i =0
while i < numofelem:
    i+=1
    if int(input("Please enter your number:\n"))>0:
        pass
    else:
        break

# 7.  Знайти прості числа від 10 до 30, а всі решта чисел представити у вигляді добутку чисел 
#(наприклад 10 equals 2 * 5
#                    11 is a prime number
#                    12 equals 2 * 6
#                    13 is a prime number
#                    14 equals 2 * 7
#                     ………………….)

mylist = range(10, 31)

valuest = []

for x in mylist:
    valuest.append(x)

for x in valuest:
    if x%2 != 0:
        print(str(x)+" is a prime number")
    elif x%8 == 0:
        print(str(x)+" equals "+str(2)+" * "+str(2)+" * "+str(2)+" * "+str(x//8))
    elif x%4 == 0:
        print(str(x)+" equals "+str(2)+" * "+str(2)+" * "+str(x//4))
    else:
        print(str(x)+" equals "+str(2)+" * "+str(x//2))

# 8.  Відсортувати слова в реченні в порядку їх довжини (використати List Comprehensions)

sentence = "Although that way may not be obvious at first unless you're Dutch."

words = sentence.split(" ")
length = []
for word in words:
    length.append(len(word))

myset = dict(zip(length, words))

wordssorted = []

for srt in sorted(myset):
    wordssorted.append(myset[srt])

print(" ".join(wordssorted))




