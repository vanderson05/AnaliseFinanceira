import pandas as pd 
from pandas_datareader import data as web
import plotly.graph_objects as go
#import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import time

import matplotlib.pyplot as plt
import plotly
import plotly.offline as py
import plotly.graph_objs as go
from datetime import date, datetime


#class consultayahoo:
#    ativo = ['OIBR3.SA', 'OIBR4.SA']
#    prices = yf.download(ativo, start='2021-03-01', rounding=True)['Adj Close']
#    retorno = prices.pct_change().dropna().round(2)
#    ativos = retorno.columns.to_list()
#    #print(retorno)

#    def calcula_carteira(df, w1):
#        pesos = [w1,(1-w1)]  
#        df2 = df.dot(pesos).copy()
#        return  df2.mean() * 252, df2.std() * np.sqrt(252)

#        carteira = pd.DataFrame()
#        for i in np.linspace(0,1, 101):

#            media, std = calcula_carteira(retorno,i)
#            carteira.at[i,'retorno'] = media
#            carteira.at[i,'volatilidade'] = std
#            print(carteira)

#        carteira
        
    





    #def consultaacao(ativo, dt_inicio):      
     #   try:
      #      dt_inicio = datetime.strptime(dt_inicio, '%d-%m-%Y')
       #     dt_inicio.strftime('%Y-%m-%d')
        #    tickers = [ativo]
         #   prices = yf.download(tickers, start=dt_inicio, rounding=True)
          #  
           # print(prices,'\n''Deu certo')  
            
            #return(prices)
       # except (IOError, KeyError):
         #   print('nao deu certo')
          #  return(prices)
    #consultaacao('OIBR3.SA', '01-01-2021')
