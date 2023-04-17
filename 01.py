import numpy as np
from scipy.stats import shapiro, bartlett, f_oneway
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 1. Провести дисперсионный анализ для определения того, есть ли различия
# среднего роста среди взрослых футболистов, хоккеистов и штангистов.

# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

f = np.array([173, 175, 180, 178, 177, 185, 183, 182])
h = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
b = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

# проверка на нормальность:

print(shapiro(f))
print(shapiro(h))
print(shapiro(b))

# т.к. pvalue у всех выборок > стат.значимости a = 0.05, то
# все они имеют нормальное распределение.

# проверка на однородность дисперсий с помощью Барлетт-теста:

print(bartlett(f, h, b))

print(f_oneway(f, h, b))

# т.к. pvalue очень маленькое, то принимаем альтернативную гипотезу
# о наличии статистических различий между группами, значит, что влияние
# вида спорта на рост спортсмена присутствует.

print(np.mean(f))
print(np.mean(h))

f1 = np.array([173, 175, 180, 178, 177, 185, 183, 182, 179.125, 179.125, 179.125])
h1 = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180, 178.67, 178.67])
b1 = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

df = pd.DataFrame({"height": [173, 175, 180, 178, 177, 185, 183, 182, 179.125,
                              179.125, 179.125, 177, 179, 180, 188, 177, 172,
                              171, 184, 180, 178.67, 178.67, 172, 173, 169, 177,
                              166, 180, 178, 177, 172, 166, 170],
                   "sport": np.repeat(["f1", "h1", "b1"], repeats =11)})
tukey = pairwise_tukeyhsd(df["height"],
                          df["sport"],
                          alpha=0.05)
print(tukey)

# статистически значимые различия обнаружены между штангистами и футболистами,
# и между штангистами и хоккеистами.