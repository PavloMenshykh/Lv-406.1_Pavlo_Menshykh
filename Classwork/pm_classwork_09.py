#1.  Спробуйте переписати наступний код через map. Він приймає список реальних імен і замінює їх прізвищами, використовуючи  більш надійний метод.
"""
names = ['Sam', 'Don', 'Daniel'] 
surnames = map(hash, names)
print(list(surnames))
"""
#2.  Вивести список кольору "red”, який найчастіше зустрічається в даному списку  
# ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"] використовуючи функцію filter.
"""
colorlist = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
numred = filter(lambda col: col == "red", colorlist)
print(list(numred))
"""
#3. Всі ці числа в списку мають стрічковий тип даних, наприклад  
# [‘1’,’2’,’3’,’4’,’5’,’7’], перетворити цей список  в список, 
# всі числа якого мають тип даних integer:
#1)  використовуючи метод  append
#2)  використовуючи метод  map
"""
numlist = ["1", "2", "3", "4", "5", "6", "7"]
listint = [int(num) for num in numlist]
print(listint)
listint2 = list(map(lambda num: int(num), numlist))
print(listint2)
"""
#4. Перетворити список, який містить милі ,  в список, який містить кілометри (1 миля=1.6 кілометра)
# a) використовуючи функцію map
# b) використовуючи функцію map та lambda
"""
def kilom(mile):
    return mile/1.6
lengthlist = [1.7, 7, 8.5]
listkilom1 = list(map(kilom, lengthlist))
print(listkilom1)
listkilom2 = list(map(lambda length: length/1.6, lengthlist))
print(listkilom2)
"""
#5. Перепишіть наступний код, використовуючи map, reduce і filter. 
# Filter приймає функцію і колекцію. Повертає колекцію тих елементів, для яких функція повертає True.
# people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}] 
# height_total = 0 
# height_count = 0 
# for person in people: 
#     if 'height' in person: 
#         height_total += person['height'] 
#         height_count += 1 
# print(height_total)
# # => 240
"""
from functools import reduce

people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}] 
ifheight = list(filter(lambda x: len(x)>1, people))
filtering = list(map(lambda x: x['height'], ifheight))
summ = reduce(lambda x, y: x+y, filtering)
print(summ)
"""

#6. 7. Використовуючи декілька декораторів створіть сендвіч, який складається з листя салату, помідорів та мяса.
#  <\^^^^^^^/>
#   #tomatos#
#   --meat--
#   ~salad~
# <\______/>
"""
def topping(func):
    def extras():
        print("<\^^^^^^^/>\n tomatos \n --meat-- \n ~salad~") 
        func()
    return extras

@topping
def sandwitch():
    print("<\______/>")

sandwitch()
"""
#7. Cтворити просту функцію-генератор, аналогічну роботі ітератора range.

def rangegen(num1, num2, step=1):
    while num1 < num2:
        yield num1
        num1 += step

print(list(rangegen(2, 15)))