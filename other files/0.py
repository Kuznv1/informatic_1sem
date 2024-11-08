import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.figure(figsize=(8,5), dpi=100)

pos = 0
 
# параметр отвечающий за разброс
scale = 10
 
# размер массива случайных чисел (сколько их сгенерируем)
size = 10000
 
# используем функцию из подраздела random библиотеки numpy и передадим наши параметры
values = np.random.normal(pos, 10, size)
 
# строим гистограмму с 100 блоков
plt.hist(values, 100, color='green', label='trying')

plt.legend()

plt.show()