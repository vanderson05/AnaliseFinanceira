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
        dt_inicio = '2021-03-01'
        df = web.DataReader(ativo, data_source='yahoo', start=dt_inicio).round(2).reset_index()     
        #print(df,'\n''Deu certo')         
        return(df)
      except (IOError, KeyError):
        print('nao deu certo')
        return(df)
    #Variavel Teste Funçao
    #consultaacao('OIBR3.SA')
  
    #======funçao calculo de media===========

    def calcularmedia(ativo):      
      try:   
        
        dados = web.DataReader(ativo, data_source='yahoo', start='01-03-2021').round(2).reset_index()
        df = pd.DataFrame(dados)

        NewDF = pd.DataFrame(columns=["MediaAlta", "MediaBaixa", "MediaOpen", "MediaClose"])
        #NewDF = NewDF.append(NewDF)
        mediaAlta = df['High'].mean().round(2)
        mediaBaixa = df['Low'].mean().round(2)
        mediaOpen = df['Open'].mean().round(2)
        mediaClose = df['Close'].mean().round(2)
        #print(mediaAlta,'\n', mediaBaixa,'\n',mediaOpen,'\n', mediaClose,'\n')
        #.loc[i]
        for i in NewDF:
          NewDF.loc[i] = [mediaAlta,mediaBaixa, mediaOpen, mediaClose]
          #print(NewDF)
        NewDF = ({
          "MediaAlta": mediaAlta,
          "MediaBaixa": mediaBaixa,
         "MediaOpen": mediaOpen,
          "MediaClose": mediaClose
        })
        #print(NewDF)  

        return(mediaAlta)

      except (IOError, KeyError):
        print('nao deu certo Media')
        return(media)
    
    #Variavel Teste Funçao
    calcularmedia('B3SA3.SA')

  #========================================================Calcular Historico==============================
    def calcularhistorico(ativo):      
        try:           
          dados = web.DataReader(ativo, data_source='yahoo', start='01-03-2021').round(2).reset_index()
          df = pd.DataFrame(dados)
          NewDF = pd.DataFrame(df,columns=['Date', 'Close'])

          
          return(NewDF)
        except (IOError, KeyError):
          print('nao deu certo Media')
          return(NewDF)    
      #Variavel Teste Funçao
    calcularhistorico('B3SA3.SA')

    







