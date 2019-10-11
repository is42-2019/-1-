#Задача №2 из раздела Линейные алгоритмы. Условие:Даны действительные числа А, В, С. Найти максимальное и минимальное из этих чисел.

import random
A=random.randint(-100,100)
B=random.randint(-100,100)
C=random.randint(-100,100)
print("Max=" + str(max(A,B,C)))
print("Min=" + str(min(A,B,C)))