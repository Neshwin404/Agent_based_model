# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 13:43:39 2022

@author: neshw
"""
import  pandas as pd
xls = pd.ExcelFile('out_put.xlsx')
data = pd.read_excel(xls, 'second4')

def gini(x):
    total = 0
    for i, xi in enumerate(x[:-1], 1):
        total += np.sum(np.abs(xi - x[i:]))
    return total / (len(x)**2 * np.mean(x))
fig = go.Figure()
fig1x = go.Figure()

fig = go.Figure()
fig.add_trace(go.Scatter( y=np.arange(X_lorenz.size)/(X_lorenz.size-1),
                        mode='lines',
                        name='lines2'))

for i in data.Step.unique():
    data[data.Step==i].Wealth
    X_lorenz = data[data.Step==i].Wealth.sort_values(ascending=True).cumsum() / data[data.Step==i].Wealth.sum()
    fig.add_trace(go.Scatter( y=X_lorenz,
                        mode='lines',
                        name=str(i)))
    # incomes = np.array(data[data.Step==i].Wealth)
    # gini(incomes)
    # fig.add_trace(go.Scatter( y=np.arange(X_lorenz.size)/(X_lorenz.size-1),
    #                     mode='lines',
    #                     name='lines2'))
    # fig1x.add_trace(go.Histogram(x=list(data[data.Step==i].Wealth)))
    # fig1x.update_layout(barmode='overlay')
plot(fig)
fig1x = go.Figure()
fig1x.add_trace(go.Histogram(x=list(data[data.Step==99].Wealth)))
plot(fig1x)
plot(figx)
ginis=[]
for i in data.Step.unique():
    incomes = np.array(data[data.Step==i].Wealth)
    gini(incomes)
    ginis.append(gini(incomes))
fig = go.Figure()
fig.add_trace(go.Scatter( y=ginis,
                        mode='lines',
                        name='lines2'))    
plot(fig)    


def compare(scenario_list):
    fig = go.Figure()
    for sc in scenario_list:
        print(sc)
        data = pd.read_excel(xls, sc)
        ginis=[]
        for i in data.Step.unique()[0:20]:
            incomes = np.array(data[data.Step==i].Wealth)
            gini(incomes)
            ginis.append(gini(incomes))
        # fig = go.Figure()
        fig.add_trace(go.Scatter( y=ginis,
                                mode='lines',
                                name=sc))    
    plot(fig)    
  
# import numpy as np
# import matplotlib.pyplot as plt

# # data = np.load('pop2010.npy')

# X_lorenz = data[data.Step==1].Wealth.sort_values(ascending=True).cumsum() / data[data.Step==1].Wealth.sum()
# # X_lorenz = asi.cumsum() / asi.sum()
# fig = go.Figure()
# fig.add_trace(go.Scatter( y=X_lorenz,
#                     mode='lines',
#                     name='lines1'))
# fig.add_trace(go.Scatter( y=np.arange(X_lorenz.size)/(X_lorenz.size-1),
#                     mode='lines',
#                     name='lines2'))
# plot(fig)
# # np.arange(X_lorenz.size)/(X_lorenz.size-1)
# X_lorenz = np.insert(X_lorenz, 0, 0)

# fig, ax = plt.subplots(figsize=[6,6])
# ## scatter plot of Lorenz curve
# ax.scatter(np.arange(X_lorenz.size)/(X_lorenz.size-1), X_lorenz, 
#            marker='x', color='darkgreen', s=100)
# ## line plot of equality
# ax.plot([0,1], [0,1], color='k')


# # set the labels for x, y, and title
# ax.set_xlabel("Countries")
# ax.set_ylabel("Wealth")
# ax.set_title("Population-Lorenz Curve") 

# plt.show()

# # save plot as png file
# plt.savefig('population-lorenz.png', dpi = 200)


# dts=data[data.Step==i]
# penguins = sns.load_dataset("penguins")
# sns.displot(dts, x="Wealth")