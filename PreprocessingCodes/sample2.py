#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:31:13 2019

@author: akhilsr
"""

import pandas as pd


train = pd.read_csv('/home/akhilsr/FinalYearProject/rossmann-store-sales/train.csv')
new = train
# train.head()
#train.dtypes
i=0
for df in new['StateHoliday']:
    
    if df == 0:
        new['StateHoliday'][i] = 'z'
    i+=1
 
    
    
new.to_csv('/home/akhilsr/FinalYearProject/rossmann-store-sales/new1.csv',index=False)
#train['StateHoliday'][1] = 10
#print(train['StateHoliday'][1])
#print(train.index)
#print(train.head(5))