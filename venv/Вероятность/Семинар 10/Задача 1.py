"""Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых
футболистов, хоккеистов и штангистов.
Даны значения роста в трех группах случайно выбранных спортсменов:

Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.

Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.

Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

footbal = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
barbel = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

print(stats.shapiro(footbal))
print(stats.shapiro(hockey))
print(stats.shapiro(barbel))

print('\nДисперсии однородны, так как p-value всех трех выборок больше 0.05\n')
print(f"Проверка на равенство дисперсий: \n{stats.bartlett(footbal, hockey, barbel)}")
print(f"Дисперсионный анализ: \n{stats.f_oneway(footbal, hockey, barbel)}\n")

df1 = pd.DataFrame({"score": footbal, "group": np.repeat("footbal", repeats=8)})
df2 = pd.DataFrame({"score": hockey, "group": np.repeat("hockey", repeats=9)})
df3 = pd.DataFrame({"score": barbel, "group": np.repeat("barbel", repeats=11)})

df = df1.append(df2).append(df3)

tukey = pairwise_tukeyhsd(df["score"], df["group"], alpha=0.05)
print(f"Тест: \n{tukey} \nРазлилия в росте есть")
