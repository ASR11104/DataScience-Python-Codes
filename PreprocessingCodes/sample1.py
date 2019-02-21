#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:38:08 2019

@author: akhilsr
"""


import pandas as pd




train_df = pd.read_csv("/home/akhilsr/FinalYearProject/rossmann-store-sales/new.csv")




file_name = "train_store"

for i in range(1,1116):
    df = train_df[train_df['Store']==i]
    
    df.to_csv("/home/akhilsr/FinalYearProject/rossmann-store-sales/train_dataset/"+file_name+str(i)+".csv",index=False)

#print(df.head)

