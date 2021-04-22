from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import pandas as pd
from .forms import AtivoForm
from .core.analise import LOGICA_CONSULTA
import json
from json import dumps
from datetime import date
from django.http import JsonResponse
import numpy as np
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objects as go

#import datetime

# Create your views here.

def index(request):

    context = {}
    if request.method == 'POST':
        form = AtivoForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True            
            ativo = form.cleaned_data['ativo']
            form = AtivoForm()       
            resultadoconsulta = LOGICA_CONSULTA.consultaacao(ativo)
            
            if resultadoconsulta.empty:
                return render(request,'empty.html')

       
        #teste = resultadoconsulta[['Date','Open', 'High', 'Low', 'Close', 'Volume']]
        #print(teste)
        
        #arrayteste = np.array(teste)
        #print(arrayteste)

#======================CRIANDO GRAFICO====================================

        plot_div = plot([Scatter(x=resultadoconsulta['Date'], y=resultadoconsulta['Close'])],output_type='div',show_link=False, link_text="", include_plotlyjs = True )

#========================FIM DO GRAFICO===================================
 #       np.set_printoptions(threshold=np.inf, linewidth=np.inf )  # turn off summarization, line-wrapping
  #      with open('SiteAnaliseAcoes/static/js/tex.json', 'w') as f:
    #        f.write(np.array2string(arrayteste, separator=', '))

        #### Parte Que forma o JSON #####
        
        resultadoconsulta.to_json('SiteAnaliseAcoes/static/js/analise.json', orient='records')

        ####Json Que Monta a Tabela DIV1 E PLOTA O GRAFICO
        json_records = resultadoconsulta.reset_index().to_json(orient='records', date_format='iso')
        dados = []
        dados = json.loads(json_records)
        context2 = {'d': dados, 'plot_div': plot_div}
        
        return render(request,'pagina.html', context2)
          
    else:
        form = AtivoForm()
        #print("Porem esta vazio")

    context['form'] = form
    return render(request,'index.html', context)

 
#def analise(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
   # return render(request,'analise.html')
