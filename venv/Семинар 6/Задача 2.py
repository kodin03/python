inp3 = int(input("Введите количество чисел в списке: "))

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.

inp = int(input("Введите количество чисел в списке: "))


def difference(inp):
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

difference(inp)