#«аписати в стр≥чку ф≥лософ≥ю ѕайтона 
#«найти в задан≥й стр≥чц≥ к≥льк≥сть входжень сл≥в (better, never, is)
#¬ивести весь текст у верхньому рег≥стр≥ (вс≥ велик≥ л≥тери)
#«ам≥нити вс≥ входженн€ символу У≥Ф на У&Ф

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