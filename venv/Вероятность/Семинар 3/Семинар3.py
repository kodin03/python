"""Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70,
75, 65, 84, 90, 150. Посчитать (желательно без использования статистических методов наподобие std, var, mean)
среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий
для данной выборки."""

import numpy as np
z = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])


sr_arithmetic = z.sum() / z.size
quadratic_dev = (np.sum((z - sr_arithmetic)**2) / z.size)**0.5
biased_var = np.sum((z - sr_arithmetic)**2) / z.size
unbiased_var = np.sum((z - sr_arithmetic)**2) / (z.size - 1)

print(f'Среднее арифметическое: {sr_arithmetic}')
print(f'Среднее квадратичное отклонение: {quadratic_dev}')
print(f'Смещенная дисперсия: {biased_var}')
print(f'Несмещенная дисперсия: {unbiased_var}')

