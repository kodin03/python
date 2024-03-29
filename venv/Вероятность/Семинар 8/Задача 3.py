"""Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности, равной 25 кв.см.
Объем выборки равен 27, среднее выборочное составляет 174.2.
Найдите доверительный интервал для математического ожидания с надежностью 0.95."""

import numpy as np
from scipy import stats

D = 25
n = 27
avg = 174.2
alpha = 0.95

sigma = np.sqrt(D)
koef = sigma / np.sqrt(n)

answer1 = avg - 1.96 * koef
answer2 = avg + 1.96 * koef
print(f"Доверительный интервал: [{answer1}, {answer2}]")
