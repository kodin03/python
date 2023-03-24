"""Посчитать коэффициент линейной регрессии при заработной плате (zp),
используя градиентный спуск (без intercept)."""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.linear_model import LinearRegression

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

x = zp.reshape((10, 1))
y = ks.reshape((10, 1))
X = np.hstack([np.ones((10, 1)), x])
alpha = 1e-6
B1 = 0.1
n = 10

def mse_(B1, y = y, x = x, n = 10):
    return np.sum((B1 * x - y)**2) / n

mse = (2/n) * np.sum((B1 * X - y) * X)

for i in range(10):
    B1 -= alpha * (2/n) * np.sum((B1 * x - y) * x)
    print('B1 = {}'.format(B1))

for i in range(2000):
    B1 -= alpha * (2/n) * np.sum((B1 * x - y) * x)
    if i % 400 == 0:
        print(f'Integration = {i}, B1 = {B1}, mse = {mse}'.format(i = i, B1 = B1, mse = mse_(B1)))

print(mse_(5.8898))

# Немного не понял, почему бета в примере семинара отличалось только тысячными, а у меня увеличивается
# Также не понял, почему mse такое большое и отрацательное, а также не сходится с mse_