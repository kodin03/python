# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import re
import itertools


file1 = 'Задача 3.txt' return f
#print(f"Считанный файл 1: {read_file(file1)}")
#print(f"Считанный файл 2: {read_file(file2)}")

# Получение списка кортежей каждого (<коэффициент>, <степень>)

def convert_file(f):
    f = f.replace('= 0', '')
    f = re.sub("[*|^| ]", " ", f).split('+')
    #print(f"Замена * ^: {f}")
    f = [char.split(' ') for char in f]
    #print(f"Разделение: {f}")
    f = [[x for x in list if x] for list in f]
    #print(f"Убираем пробелы: {f}")
    for i in f:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    f = [tuple(int(x) for x in j if x != 'x') for j in f]
    #print(f"int: {f}")
    return f

# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)

def fold_fs(f1, f2):
    x = [0] * (max(f1[0][1], f2[0][1] + 1))
    for i in f1 + f2:
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    #print(f"Res {res}")
    res.sort(key = lambda r: r[1], reverse = True)
    #print(f"Перевернутый {res}")
    return res

# Составление итогового многочлена

def get_sum_f(f):
    var = ['*x^'] * len(f)
    koefs = [x[0] for x in f]
    degrees = [x[1] for x in f]
    new_f = [[str(a), str(b), str(c)] for a, b, c in (zip(koefs, var, degrees))]
    #print(f"Новая f: {new_f}")
    for x in new_f:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': x[1:], x[1:][1:]
        if len(x) > 1 and x[-1] == '1':
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_f = list(itertools.chain(*new_f))
    new_f[-1] = ' = 0'
    #print("".join(map(str, new_f)))
    return "".join(map(str, new_f))

def write_to_file(file, f):
    with open(file, 'w') as data:
        data.write(f)


f1 = read_file(file1)
f2 = read_file(file2)
f_1 = convert_file(f1)
f_2 = convert_file(f2)
sum = get_sum_f(fold_fs(f_1, f_2))

write_to_file(file_sum, sum)

print(f"Первое исходное уравнение: {f1}")
print(f"Второе исходное уравнение: {f2}")
print(f"Сумма: {sum}")

