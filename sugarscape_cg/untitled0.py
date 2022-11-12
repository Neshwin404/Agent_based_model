# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 13:47:56 2022

@author: neshw
"""
import seaborn as sns
import numpy as np
import pandas as pd

sns.set()
planets = sns.load_dataset('planets')
planets.head()

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

for col in 'xy':
    sns.kdeplot(data[col], shade=True)