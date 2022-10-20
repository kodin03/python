
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

print("Задача про нечетные числа: ")
inp = int(input("Введите количество чисел в списке: "))
numbers = [inp]

def fun(inp):
    summa = 0
    print("Введите числа через пробел: ")
    str1 = str(input())
    numbers = [int(x) for x in str1.split(" ")]

    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            summa += numbers[i]
    print(f"Сумма нечетных элементов: {int(summa)}")

fun(inp)
