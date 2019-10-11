#Задача №18 из раздела Ветвления и оператор выбора
#Условие:Имеются две ёмкости: кубическая с ребром A, цилиндрическая с высотой H и радиусом основания R. Определить, можно ли заполнить жидкостью объёма M первую ёмкость, вторую, обе.
import random
import math

A = random.randint(1, 10)
Cube = A ** 3
print("V Cube = " + str(Cube))

H = random.randint(1, 10)
R = random.randint(1, 10)
pi = math.pi
Cylinder = pi * R ** 2 * H
print("V Cylinder = " + str(Cylinder))

M = random.randint(1, 400)
print("V Woter = " + str(M))

if Cube == M:
    print("Water filled cube")
elif Cube != M:
    print("Water not filled cube")

if Cylinder == M:
    print("Water filled cube")
elif Cylinder != M:
    print("Water not filled Cylinder")

if Cube == M and Cylinder == M:
    print("Water filled cube and cylinder")

if Cube != M and Cylinder != M:
    print("Water not filled cube and cylinder")