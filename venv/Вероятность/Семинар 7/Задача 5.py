"""Задача 5. Заявляется, что партия изготавливается со средним арифметическим 2,5 см. Проверить
данную гипотезу, если известно, что размеры изделий подчинены нормальному закону
распределения. Объем выборки 10, уровень статистической значимости 5%
2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34"""

import numpy as np
from scipy import stats

x = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
average = 2.5
n = 10
alpha = 0.05
"""H0: average = 2.5
   H1: sr_arithmetic_x = 2.53 -> критическая область одностороняя"""
unbiased_var = np.sum((x - average)**2) / (x.size - 1)
sigma = np.sqrt(unbiased_var)
sr_arithmetic_x = np.sum(x) / x.size # 2.53
t1 = stats.norm.ppf(1 - alpha) # 1.6448536269514722

z = (sr_arithmetic_x - average) / (sigma / np.sqrt(n))
p_right = 1 - stats.norm.cdf(z)

print(f"t1 = {t1}\nz = {z}\np_right = {p_right}\n\nt1 (1.64) > z (0.55) -> Нулевая гипотеза не отвергается,\nзначит партия изготавливается из изделий в среднем 2,5 см")



