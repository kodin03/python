"""Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
   Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
   Используя эти данные построить 95% доверительный интервал для разности среднего
роста родителей и детей."""

import numpy as np
from scipy import stats

a = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
b = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])

X1 = np.mean(a)
X2 = np.mean(b)
delta = np.abs(X1 - X2)

D1 = np.var(a, ddof=1)
D2 = np.var(b, ddof=1)
D = (D1 + D2) / 2

SE = np.sqrt(D/10 + D/10)

ta = stats.t.ppf(0.975, 18)

answer1 = delta - ta * SE
answer2 = delta + ta * SE
print(f"P -> ({answer1}; {answer2})")