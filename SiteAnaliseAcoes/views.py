from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import pandas as pd
from .forms import AtivoForm
from .core.analise import LOGICA_CONSULTA

#import datetime

# Create your views here.

def index(request):

    context = {}
    if request.method == 'POST':
        form = AtivoForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True            
            ativo = form.cleaned_data['ativo']
            #date = form.cleaned_data['date']    
            form = AtivoForm()       
            resultadoconsulta = LOGICA_CONSULTA.consultaacao(ativo)
            #print('\n'"Deu Certo")  

            if resultadoconsulta.empty:
                return render(request,'empty.html')

        pd.set_option('colheader_justify', 'center')
        html_string ='''
                <!DOCTYPE html>
                <html lang="pt">                 
                <title> ANALISE </title>
                <head>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width" />
                <script src="https://code.jquery.com/jquery-3.1.1.min.js"
                integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8="
                crossorigin="anonymous"></script>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js" integrity="sha384-SR1sx49pcuLnqZUnnPwx6FCym0wLsk5JZuNx2bPPENzswTNFaQU1RDvt3wT4gWFG" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.min.js" integrity="sha384-j0CNLUeiqtyaRmlzUHCPZ+Gy5fQu0dQ6eZ/xAww941Ai1SxSY+0EQqNXNE6DZiVc" crossorigin="anonymous"></script>
                <link rel="stylesheet" href="static/style.css">
                </head>                           
                    <body>
                        <div id="includedContent"></div>                                                                                  
                    <div class="container-fluid">
                    <div class="row">
                        <div class="col-md-12">     
                            <h3>Historico</h3><br>
                            <input type="button" value="Voltar" onClick="history.go(-1)"><b>                                
                            </button>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-6">
                            <span class="badge badge-default">Label</span>
                            {table} 
                        </div>
                        <div class="col-md-6">
                            <span class="badge badge-default">Label</span>
                            <img src="static/img/Grafico.png" alt="Girl in a jacket" width="500" height="600">
                        </div>
                    </div>
                </div>
                </body>
                </html>
                '''
		# OUTPUT AN HTML FILE
        with open('SiteAnaliseAcoes/template/analise.html', 'w') as f:
            f.write(html_string.format(table=resultadoconsulta.to_html(classes='mystyle', index=False))) 

        return render(request,'analise.html')
          
    else:
        form = AtivoForm()
        #print("Porem esta vazio")

    context['form'] = form
    return render(request,'index.html', context)
 
def analise(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'analise.html')












 