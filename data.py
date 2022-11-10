# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:37:30 2022

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

data_1 = pd.read_csv("files/DATA_A.csv")
data_2 = pd.read_csv("files/DATA_B.csv")
data_3 = pd.read_csv("files/DATA_C.csv")