"""Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату
(то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная).
Произвести расчет как с использованием intercept, так и без."""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.linear_model import LinearRegression

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

x = zp.reshape((10, 1))
y = ks.reshape((10, 1))
X = np.hstack([np.ones((10, 1)), x])
B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T @ y)

x1 = zp.reshape(-1, 1)
y1 = ks.reshape(-1, 1)
model = LinearRegression()
model.fit(x1, y1)

plt.plot(x1, x1 * model.coef_[0] + model.intercept_, color='red')
plt.scatter(x1, y1)
plt.show()

print(f"Путем математических вычислений: {B}")
print(f"Путем применения intercept: {model.intercept_, model.coef_}")

