#Задача №35 из раздела Циклические алгоритмы. Обработка последовательностей и одномерных массивов
#Условие:Дан одномерный массив числовых значений, насчитывающий N элементов. Поменять местами группу из M элементов, начинающихся с позиции K с группой из M элементов, начинающихся с позиции P.
import random

M = random.randint(1,5)
K = random.randint(1,5)
P = random.randint(5,10)
N = random.randint(1,15)

arr = [random.randint(1,100) for i in range(N)]
print("N= " + str(N))
print("K= " + str(K))
print("P= " + str(P))
print("M= " + str(M))
print(arr)

arr[K : M + K + 1] , arr[P : M+P+1] = arr[P : M+P+1] , arr[K : M+K+1]
print(arr)