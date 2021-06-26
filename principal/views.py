from django.shortcuts import render
from . import relatorios

def index(request):
   return render(request,'principal/index.html')

def relatorio(request):
   data_dict = {'grafico': relatorios.gera_grafico_barras()}
   return render(request,'principal/relatorio.html', data_dict)