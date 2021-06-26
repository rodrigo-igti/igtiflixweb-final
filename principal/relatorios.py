import matplotlib.pyplot as plt
import io
from serie.models import Serie
from django.db.models import Count

def gera_grafico_pontos():

    x = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111,
         0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]
    y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657,
         1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, 'o', label='dados originais')
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()

    imagem_io = io.StringIO()
    plt.savefig(imagem_io, format='svg')

    return imagem_io.getvalue()

def gera_grafico_barras():

    result = Serie.objects.values('idGenero__descricao').annotate(total=Count('idGenero')).order_by('-total')

    generos =[elemento['idGenero__descricao']for elemento in result]
    totais = [elemento['total']for elemento in result]

    plt.figure(figsize=(7, 3.5))
    plt.bar(generos, totais, width=0.4)
    plt.xlabel("Gêneros")
    plt.ylabel("Total de Séries")

    imagem_io = io.StringIO()
    plt.savefig(imagem_io, format='svg')

    return imagem_io.getvalue()