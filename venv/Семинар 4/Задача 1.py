

# Вычислить число c заданной точностью d

print("Задача про точность числа: ")
d = float(input("Задайте точность: "))
pi = 3.141592653589793238462643

def accurary(d):
    num = 0
    if d < 0:
        print("Введена отрицательная точность. Задайте положительную")
    else:
        while d < 1:
            d *= 10
            num += 1
        print(format(pi, "." + str(num) + "f"))

accurary(d)