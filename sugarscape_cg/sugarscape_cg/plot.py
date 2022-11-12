# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 13:02:02 2022

@author: neshw
"""

import pandas as pd
import numpy as np
import time
import seaborn as sns
sns.set()
from plotly.offline import plot
data=pd.read_csv(r"C:/Users/neshw/OneDrive/CAS project/new/sugarscape_cg/temp_data.csv")
    # df = px.data.tips()
data[data.Step==1].Wealth
import plotly.graph_objects as go
import plotly.express as px
df = px.data.tips()
fig = go.Figure()
fig1 = go.Figure()
for i in range(0,200):
    # list(data[data.Step==200].Wealth)
    time.sleep(1) 
    # import plotly.express as px
    # df = px.data.tips()
    # fig = px.histogram( list(data[data.Step==200].Wealth))
    # # print(len(list(data[data.Step==200].Wealth)))
    # plot(fig)
    # fig = px.histogram(data[data.Step==200], x="total_bill", y="Wealth", color="sex",
    #                marginal="box", # or violin, rug
    #                hover_data=df.columns)
    # fig.show()
    if i % 20 == 0 or i==1:  
        print(i)
        liata=(list(data[data.Step==i].Wealth))
        liata.sort(reverse=True)

        fig = go.Figure()
        fig.add_trace(go.Box(y=liata))
        # plot(fig)
        dts=data[data.Step==i]
 
        sns.displot(dts, x="Wealth")
    #     fig.update_traces(boxpoints='all', jitter=0)
    # # if i % 10 == 0:
    #     print('number is multiple of 10')
    # if i==99:
        # ta=((data[data.Step==i]))
        # X_lorenz = ta.Wealth.cumsum() / ta.Wealth.sum()
        # fig1.add_trace(go.Scatter( y=X_lorenz,
        #                     mode='lines',
        #                     name='lines'))
        # fig1.add_trace(go.Scatter( y=np.arange(X_lorenz.size)/(X_lorenz.size-1),
        #                     mode='lines',
        #                     name='lines'))

        X_lorenz = data[data.Step==i].Wealth.sort_values(ascending=True).cumsum() / data[data.Step==i].Wealth.sum()
        # X_lorenz = asi.cumsum() / asi.sum()
        # fig = go.Figure()
        fig1.add_trace(go.Scatter( y=X_lorenz,
                            mode='lines',
                            name=i))
        sns.kdeplot(data[data.Step==i].Wealth, shade=True)
        plot(fig)
fig1.add_trace(go.Scatter( y=np.arange(X_lorenz.size)/(X_lorenz.size-1),
                    mode='lines',
                    name='lines'))
# plot(fig)
plot(fig)
time.sleep(1) 
plot(fig1)
    #     # sns.kdeplot(data[data.Step==i].Wealth)
    #     sns.displot(data[data.Step==i].Wealth)
    # sns.distplot(data['y']);

fig1 = go.Figure()
fig.add_trace(go.Scatter( y=X_lorenz,
                    mode='lines',
                    name='lines'))
fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                    mode='lines+markers',
                    name='lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                    mode='markers', name='markers'))

fig.show()
if 100 % 10 == 0:
    print('number is multiple of 10')
import time
import seaborn as sns
sns.set()
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left');
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
for col in 'xy':
    sns.kdeplot(data[data.Step==200].Wealth, shade=True)
# while True:
#     try:
#         time.sleep(1) 


import numpy as np
import matplotlib.pyplot as plt

# data = np.load('pop2010.npy')

X_lorenz = data[data.Step==1].Wealth.sort_values(ascending=True).cumsum() / data[data.Step==1].Wealth.sum()
# X_lorenz = asi.cumsum() / asi.sum()
fig = go.Figure()
fig.add_trace(go.Scatter( y=X_lorenz,
                    mode='lines',
                    name='lines'))
fig.add_trace(go.Scatter( y=np.arange(X_lorenz.size)/(X_lorenz.size-1),
                    mode='lines',
                    name='lines'))
plot(fig)
# np.arange(X_lorenz.size)/(X_lorenz.size-1)
X_lorenz = np.insert(X_lorenz, 0, 0)

fig, ax = plt.subplots(figsize=[6,6])
## scatter plot of Lorenz curve
ax.scatter(np.arange(X_lorenz.size)/(X_lorenz.size-1), X_lorenz, 
           marker='x', color='darkgreen', s=100)
## line plot of equality
ax.plot([0,1], [0,1], color='k')


# set the labels for x, y, and title
ax.set_xlabel("Countries")
ax.set_ylabel("Wealth")
ax.set_title("Population-Lorenz Curve") 

plt.show()

# save plot as png file
plt.savefig('population-lorenz.png', dpi = 200)


dts=data[data.Step==i]
penguins = sns.load_dataset("penguins")
sns.displot(dts, x="Wealth")