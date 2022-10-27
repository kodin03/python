
import random
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

print("Задача про последовательность чисел: ")
N = []
for i in range(5):
    N.append(random.randint(0, 4))
print(f"Изначальный список: {N}")

def repeat(N):
    answer = []
    if len(N) == 0:
        print("Список пуст.")
    else:
        for el in N:
            while el not in answer:
                answer.append(el)
        print(f"Конечный список: {answer}")

repeat(N)