# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 21:14:37 2022

@author: neshw
"""

class Run(mesa.Model):
    """
    Sugarscape 2 Constant Growback
    """
    import pandas as pd
    # import xlrd, xlwt
    # from xlutils.copy import copy as xl_copy
    from openpyxl import load_workbook
    verbose = True  # Print-monitoring
    main_data=pd.read_csv("sugarscape_cg/data.csv",index_col=0)
    pop=main_data.loc['fourth'].population
    
    def __init__(self, width=50, height=50, initial_population=pop):
        import pandas as pd