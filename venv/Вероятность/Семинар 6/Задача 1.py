"""Известно, что генеральная совокупность распределена нормально
со средним квадратическим отклонением, равным 16.
Найти доверительный интервал для оценки математического ожидания с надежностью
0.95, если выборочная средняя M = 80, а объем выборки n = 256."""

import numpy as np

M = 80
n = 256
sigma = 16
za = 1.96 # так как z от 0.05/2 = 1.96

answer1 = M - za * sigma / np.sqrt(n)
answer2 = M + za * sigma / np.sqrt(n)
print(f"P -> ({answer1}; {answer2})")