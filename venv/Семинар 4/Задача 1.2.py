

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print("Задача про точность числа: ")
N = int(input("Введите натуральное число: "))

def multi(N):
    num = 2
    answer = []
    if N <= 0:
        print("Введено не натуральное число.")
    else:
        while N > 1:
            if (N % num) == 0:
                N = N / num
                answer.append(num)
            else:
                num += 1
        print(answer)

multi(N)