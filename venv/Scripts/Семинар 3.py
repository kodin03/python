import math
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

"""print("Задача про нечетные числа: ")
inp1 = int(input("Введите количество чисел в списке: "))
numbers = []

def fun(inp1):
    summa = 0
    print("Введите числа через пробел: ")
    str1 = str(input())
    numbers = [int(x) for x in str1.split(" ")]

    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            summa += numbers[i]
    print(f"Сумма нечетных элементов: {int(summa)}")

fun(inp1)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

print("Задача про пары чисел: ")
inp2 = int(input("Введите количество чисел в списке: "))

def multi(inp2):
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
            if i == len(numbers) - n - 1:
                answer.append(numbers[i] * numbers[len(numbers) - n])
                break
            elif i < n:
                answer.append(numbers[i] * numbers[len(numbers) - n])
                n += 1
    print(f"Произведение парных чисел: {answer}")

multi(inp2)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.

print("Задача про вещественные числа: ")
inp3 = int(input("Введите количество чисел в списке: "))

def difference(inp3):
    diff = 0
    dec = 0
    num = 0
    decimal = []
    print("Введите числа через пробел: ")
    str1 = str(input())
    numbers = [float(x) for x in str1.split(" ")]
    for i in range(len(numbers)):
        dec = divmod(numbers[i], 1)
        num = round(list(dec)[1], 10)
        decimal.append(num)

    diff = abs(max(decimal) - min(decimal))
    print(f"max: {max(decimal)}")
    print(f"min: {min(decimal)}")
    print(f"Разница дробной части max и min: {diff}")

difference(inp3)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

print("Задача про перевод числа в двоичное: ")
inp4 = int(input("Введите число: "))

def dec_bin(inp4):
    bin = ""
    res = ""
    while inp4 >= 1:
        res = str(math.floor(inp4 % 2))
        bin = "".join([bin, res])
        inp4 = inp4 / 2

    res = ''.join(reversed(bin))
    print(f"Число в двоичном виде: {res}")

dec_bin(inp4)"""

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

print("Задача про числа Фибоначчи: ")
n = int(input("Введите число: "))

def fibonacci(n):
    square = 2 * n
    fib = [1 for i in range(square + 1)]
    fib[n] = 0
    num = 1
    for i in range(n + 2, square + 1):
        num = -num
        fib[i] = fib[i - 1] + fib[i - 2]
        fib[square - i] = fib[i] * num
    return fib

print(f"Список чисел Фибоначчи: {fibonacci(n)}")