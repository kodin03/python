
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

inp1 = int(input("Введите количество чисел в списке: "))
numbers = []

def fun(inp1):
    summa = 0
    print("Введите числа через пробел: ")
    input_numbers = str(input())
    input_numbers = [int(x) for x in input_numbers.split(" ")]
    for i in range(len(input_numbers)):
        if input_numbers[i] % 2 == 1:
            summa += input_numbers[i]
    print(f"Сумма нечетных элементов: {int(summa)}")

fun(inp1)