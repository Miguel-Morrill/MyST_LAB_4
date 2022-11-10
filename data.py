# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:37:30 2022

@author: theso
"""

import pandas as pd
import functions as fun

data_1 = pd.read_csv("files/DATA_A.csv")
data_2 = pd.read_csv("files/DATA_B.csv")
data_3 = pd.read_csv("files/DATA_C.csv")

# 2.2 
data_AA=fun.visMicro(data_1)
data_BB=fun.visMicro(data_2)
data_CC=fun.visMicro(data_3)