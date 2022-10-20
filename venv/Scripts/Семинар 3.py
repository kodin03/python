
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

print("Задача про нечетные числа: ")
inp = int(input("Введите количество чисел в списке: "))
numbers = []

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

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

print("Задача про пары чисел: ")
inp = int(input("Введите количество чисел в списке: "))

def inputData(inp):
    numbers = []
    answer = []
    n = 1
    print("Введите числа через пробел: ")
    str1 = str(input())
    numbers = [int(x) for x in str1.split(" ")]

    for i in range(len(numbers)):
        if len(numbers) % 2 == 1:
            if i == len(numbers) - n:
                answer.append(numbers[i] * numbers[len(numbers) - n])
                break
            elif i < n:
                answer.append(numbers[i] * numbers[len(numbers) - n])
                n += 1
        elif len(numbers) % 2 == 0:
            if i == len(numbers) - n - 1:    # 0 3   1 2  2 1
                answer.append(numbers[i] * numbers[len(numbers) - n])
                break
            elif i < n:
                answer.append(numbers[i] * numbers[len(numbers) - n])
                n += 1
    print(f"Произведение парных чисел: {answer}")

inputData(inp)
