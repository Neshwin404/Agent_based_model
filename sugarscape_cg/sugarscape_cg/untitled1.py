# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 10:22:27 2022

@author: neshw
"""

def Check_Income_tax(self,val):
    import numpy as np
    # this_cell = self.model.grid.get_cell_list_contents([pos])
    # for agent in this_cell:
    #     if type(agent) is Sugar:
    #         return agent
    # income=list(np.unique(self.model.sdist))
income=[0,1,2,3,4]
index = income.index(val)
tax_slab=[0,0,5,10,15]
# print(val,tax_slab[index])
indn=index
income_tax_collected=0
for i in range(index):
    # print(tax_slab[indn])
    # print(income[indn])
    taxable=income[indn]-income[indn-1]
    income_tax_collected=tax_slab[indn]/100*taxable+income_tax_collected
    # print('tax',tax_slab[indn]/100*taxable,income_tax_collected)
    indn=indn-1
return income_tax_collected