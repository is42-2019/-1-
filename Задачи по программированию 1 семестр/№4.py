#Задача №4 из раздела Линейные алгоритмы
#Условие:Задан вес в граммах. Определить вес в тоннах и килограммах.
import random
Gr=random.randint(1,999)
Kg= Gr/1000.0
T= Kg/1000.0
print("Gram="+ str(Gr))
print("Kilogram="+ str(Kg))
print("Tone="+ str(T))