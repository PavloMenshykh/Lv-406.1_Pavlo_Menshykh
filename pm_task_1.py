#Створіть скрипт, який би запитував у користувача:
#Його ім'я: "What is your name?"
#Вік: "How old are you?"
#Місце проживання: "Where do you live?"
#А потім виводив наступні рядки
#“Hello, ім'я!"
#“Your age is вік"
#“You live in місце проживання"
#(замість слів ім'я, вік, місце проживання повинні бути відповідні дані, що введені користувачем).

name_user = input ("What is your name?:\n")
age = input ("How old are you?:\n")
location = input  ("Where do you live?:\n")

print ("Hello, "+name_user+"!")
print ("Your age is "+age)
print ("You live in "+location)
