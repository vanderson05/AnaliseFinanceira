import pandas as pd 
from pandas_datareader import data as web
import plotly.graph_objects as go
#import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import time
from datetime import date, datetime

import plotly
import plotly.offline as py
import plotly.graph_objs as go

class LOGICA_CONSULTA:
    def consultaacao(ativo):      
      try:
        df = pd.DataFrame()
        #dt_inicio = datetime.strptime(dt_inicio,'%m-%d-%Y')
        #dt_inicio.strftime('%Y-%m-%d')
        dt_inicio = '2020-03-01'
        df = web.DataReader(ativo, data_source='yahoo', start=dt_inicio, ).round(2).reset_index()

        
        #print(df,'\n''Deu certo')         
        return(df)
      except (IOError, KeyError):
        print('nao deu certo')
        return(df)
    #Variavel Teste Funçao
    #consultaacao('OIBR3.SA')
  

    







