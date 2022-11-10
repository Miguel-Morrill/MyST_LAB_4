# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:38:12 2022

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
#import data as dt
#import main as mn
import visualizations as vs

def OrderBook(exchanges,symbol_1,symbol_2,symbol_3,limit):
    inicio=time.time()
    data_inicio_A = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tiempo=0
    
    info1=open("files\DATA_A.csv","w")
    info1.truncate()
    info1.close()
    
    info2=open("files\DATA_B.csv","w")
    info2.truncate()
    info2.close()
    
    info3=open("files\DATA_C.csv","w")
    info3.truncate()
    info3.close()
    
    while tiempo <= 60:
        for i in range(len(exchanges)):
            OB1 = exchanges[i].fetch_order_book(symbol_1,limit)
            OB1_time=OB1["datetime"]
            OB1_ask=pd.DataFrame(OB1["asks"],columns=["Ask","AVolume"])
            OB1_bid=pd.DataFrame(OB1["bids"],columns=["Bid","BVolume"])
            data1 = pd.concat([OB1_ask,OB1_bid],axis=1)
            data1["Exchange"]=exchanges[i]
            data1["Ticker"]=symbol_1
            data1["Timestamp"]=OB1_time
            data1["Spread"]=(data1.Ask-data1.Bid)
            tiempo=int(time.time()-inicio)/60
            DATA1=pd.DataFrame(data1)
            DATA1.to_csv("files\DATA_A.csv",index=False,header=False, mode="a")
            
            OB2 = exchanges[i].fetch_order_book(symbol_2,limit)
            OB2_time=OB2["datetime"]
            OB2_ask=pd.DataFrame(OB2["asks"],columns=["Ask","AVolume"])
            OB2_bid=pd.DataFrame(OB2["bids"],columns=["Bid","BVolume"])
            data2 = pd.concat([OB2_ask,OB2_bid],axis=1)
            data2["Exchange"]=exchanges[i]
            data2["Ticker"]=symbol_2
            data2["Timestamp"]=OB2_time
            data2["Spread"]=(data2.Ask-data2.Bid)
            tiempo=int(time.time()-inicio)/60
            DATA2=pd.DataFrame(data2)
            DATA2.to_csv("files\DATA_B.csv",index=False,header=False, mode="a")
            
            OB3 = exchanges[i].fetch_order_book(symbol_3,limit)
            OB3_time=OB3["datetime"]
            OB3_ask=pd.DataFrame(OB3["asks"],columns=["Ask","AVolume"])
            OB3_bid=pd.DataFrame(OB3["bids"],columns=["Bid","BVolume"])
            data3=pd.concat([OB3_ask,OB3_bid],axis=1)
            data3["Exchange"]=exchanges[i]
            data3["Ticker"]=symbol_3
            data3["Timestamp"]=OB3_time
            data3["Spread"]=(data3.Ask-data3.Bid)
            tiempo=int(time.time()-inicio)/60
            DATA3=pd.DataFrame(data3)
            DATA3.to_csv("files\DATA_C.csv",index=False,header=False, mode="a")
            
            time.sleep(10)
    return data1


