#Записати в стрічку філософію Пайтона 
#Знайти в заданій стрічці кількість входжень слів (better, never, is)
#Вивести весь текст у верхньому регістрі (всі великі літери)
#Замінити всі входження символу “і” на “&”

import this
import codecs

zen = codecs.encode(this.s, 'rot13')

#task 1.a
homeworkcount = ("better", "never", "is")
print("Occurences of "+str(homeworkcount[0])+" = "+str(zen.count(homeworkcount[0]))+" times")
print("Occurences of "+str(homeworkcount[1])+" = "+str(zen.count(homeworkcount[1]))+" times")
print("Occurences of "+str(homeworkcount[2])+" = "+str(zen.count(homeworkcount[2]))+" times")

#task 1.b
print(zen.upper())

#task 1.c
print(zen.replace("i","&"))
