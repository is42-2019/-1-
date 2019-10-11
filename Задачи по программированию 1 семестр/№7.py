#Задача №7 из раздела Ветвления и оператор выбора
#Условие:Дано натуральное число. Определить, будет ли это число: чётным, кратным 4.
import random
A= random.randint (1,100)
print("Number:" + str(A))
if A % 2 == 0:
    print ("The number is even")
if A % 4 == 0:
    print ("The number is a multiple of 4")