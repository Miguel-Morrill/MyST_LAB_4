# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:38:33 2022

@author: theso
"""

import ccxt
import time
import threading
from datetime import datetime
from time import localtime, strftime
import pandas as pd 
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

import functions as fn
#import data as dt
#import main as mn


#def grafica_data_1_mid(dataframe): 
#    df2= dataframe[dataframe["Ticker"]=="BTC/USDT"]
#    fig=px.line(df2, x="TimeStamp", y="mid_price",color="Exchange",title=("Grafica del Middle Price de BTC/USDT"))
#    return fig.show()

def grafica_data_ABC(dataframe, graph, title_g): 
    fig=px.line(dataframe, x='TimeStamp', y= graph, color="Exchange",title=(title_g))
    return fig.show()