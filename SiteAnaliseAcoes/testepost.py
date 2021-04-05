
import pandas as pd 
from pandas_datareader import data as web
import plotly.graph_objects as go
import yfinance as yf


class LOGICA_CONSULTA:
    def consultaacao(ativo):
        try:
            df = pd.DataFrame()
            df = web.DataReader(ativo, data_source='yahoo', start='01-01-2021').round(2).tail(10)
            print('\n' 'Deu certo')
            return(df)

        except (IOError, KeyError):
            print('nao deu certo')
            msg = 'Não encotrado dados para este ativo'
            return(df)
            

    #consultaacao('tes.SA')


