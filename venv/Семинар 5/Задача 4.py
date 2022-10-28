
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('Задача 4 вход.txt', 'r') as data:
    file1 = data.read()


def encode_rle(f):
    str_code = ''
    prev_char = ''
    count = 1
    for char in f:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code


str_code = encode_rle(file1)
print(str_code)

with open('Задача 4 выход.txt', 'r') as data:
    file2 = data.read()


def decoding_rle(f: str):
    count = ''
    str_decode = ''
    for char in f:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


str_decode = decoding_rle(file2)
print(str_decode)