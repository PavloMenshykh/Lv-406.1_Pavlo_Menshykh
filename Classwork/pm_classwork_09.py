"""
import random 
names = ['Sam', 'Don', 'Sid'] 
secret_names = map(lambda x: random.choice(['Iron', 'Batman', 'Capitan']), names)

import random
names = ['Sam', 'Don', 'Sid'] 
code_names = ['Iron', 'Batman', 'Capitan'] 
for i in range(len(names)): 
    names[i] = random.choice(code_names) 
print(names)
"""


#1.  Спробуйте переписати наступний код через map. Він приймає список реальних імен і замінює їх прізвищами, використовуючи  більш надійний метод.
"""
names = ['Sam', 'Don', 'Daniel'] 
surnames = map(hash, names)
print(list(surnames))
"""
#2.  Вивести список кольору "red”, який найчастіше зустрічається в даному списку  
# ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"] використовуючи функцію filter.
#colorlist = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
#numred = filter(lambda col: )

#3. Всі ці числа в списку мають стрічковий тип даних, наприклад  
# [‘1’,’2’,’3’,’4’,’5’,’7’], перетворити цей список  в список, 
# всі числа якого мають тип даних integer:
#1)  використовуючи метод  append
#2)  використовуючи метод  map

numlist = ["1", "2", "3", "4", "5", "6", "7"]
listint = [int(num) for num in numlist]
print(listint)
listint2 = list(map(lambda num: int(num), numlist))
print(listint2)