# 1.  Роздрукувати всі парні числа менші 100 (написати два варіанти коду: один використовуючи цикл while, а інший з використанням циклу for).
# 1.a.

even = []

for a in range (1,101):
    if a%2 == 0:
        even.append(a)

print(even)

# 1.b.

even2 = []
cnt = 0

while cnt <= 100:
    cnt += 1
    if cnt%2 == 0:
        even2.append(cnt)

print(even2)

# 2.  Роздрукувати всі непарні числа менші 100. (написати два варіанти коду: один використовуючи оператор continue, а інший без цього оператора).

# 2.a.

odd = []

for x in range (1,101):
    if x%2 != 0:
        odd.append(x)
        continue

print(odd)

# 2.b.

odd2 = []
cnt2 = 1

while cnt2 > 0:
    odd2.append(cnt2)
    cnt2 += 2
    if cnt2 >= 100:
        break

print(odd2)

# 3.  Перевірити чи список містить непарні числа.
#          (Підказка: використати оператор break)

listnumm = (6, 4, 8, 6, 5, 4)

for y in listnumm:
    if y%2 != 0:
        print("has odd numbers")
        break
else: 
    print("has only even numbers")

# 4. Створити список, який містить елементи цілочисельного типу, потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою. 
# (Підказка: використати вбудовану функцію float ()).

listfloat = []

for innt in listnumm:
    listfloat.append(float(innt))

print(listfloat)

# 5. Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)

number1 = int(input("Enter integer number: \n"))

def addition(ll):
    return(ll[-2]+ll[-1])

fib2 = [0,1]

while fib2[-1] < number1:
    fib2.append(addition(fib2))

for fbfb in fib2:
    if fbfb > number1:
        fib2.remove(fbfb)

print("Fibbonachi numbers smaller than input number are: "+str(fib2))

# 6. Створити список, що складається з чотирьох елементів типу string. Потім, за допомогою циклу for, вивести елементи по черзі на екран.

listforprint = ["elem1","elem2","elem3","elem4"]

for el in listforprint:
    print(el)

# 7. Змінити попередню програму так, щоб в кінці кожної букви елементів при виводі додавався певний символ, наприклад “#”.

symb = "'"

for el in listforprint:
    for ee in el:
        print(ee, end=symb)
    print()