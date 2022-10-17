# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
"""
print("Задача про вещественное число: ")
inp = float(input("Введите число: "))
def sum(n):
    summa = 0
    if n >= 1:
        n = n * 10
        while n % 10 != 0:
            n = n * 10
        while n > 0:
            count = n % 10
            summa = count + summa
            n = n // 10
        print(f"Сумма цифр: {int(summa)}")
    elif n < 1:
        n = n * 10
        while n % 10 != 0:
            n = n * 10
        while n > 0:
            count = n % 10
            summa = count + summa
            n = n // 10
        print(f"Сумма цифр: {int(summa)}")

sum(inp)
"""
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

print("Задача про набор чисел: ")
n = int(input("Введите число: "))
f = 1
while n > 1:
    f = n * f
    n -= 1
    print (f"Набор ( {f} )")
