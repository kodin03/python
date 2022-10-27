from random import randint
import itertools

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

print("Задача про многочлен: ")
k = randint(2, 4)

def get_koef(k):
    koef = [randint(0, 10) for i in range (k + 1)]
    while koef[0] == 0:
        koef[0] = randint(1, 10)
    return koef

def get_polynomial(k, koef):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(koef, var, range(k, 1, -1), fillvalue = '') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')


koef = get_koef(k)
polynom1 = get_polynomial(k, koef)
print(polynom1)

with open('Задача 3.txt', 'w') as data:
    data.write(polynom1)

# Для следующей задачи
k = randint(2, 5)

koef = get_koef(k)
polynom2 = get_polynomial(k, koef)
print(polynom2)

with open('Задача 3.2.txt', 'w') as data:
    data.write(polynom2)


