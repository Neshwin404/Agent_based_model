# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:34:10 2022

@author: neshw
"""
import pandas as pd
na=pd.read_csv("sugarscape_cg/data.csv",index_col=0)
for ii in na.index:
    print(ii)
    execfile('run.py')