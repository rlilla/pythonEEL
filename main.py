import eel
import pandas as pd
from win32api import GetSystemMetrics

largura = GetSystemMetrics(0)
altura = GetSystemMetrics(1)

eel.init('web')
df=pd.read_csv("C://temp//teste.txt",sep=";")
df1=pd.read_excel("NCM.xls",header=[1])

@eel.expose
def teste(var1):
    print(var1)
@eel.expose
def consultar(descricao):
    x = df[df['descricao'].str.contains(descricao) | df['codigo'].str.contains(descricao)].to_dict()
    print (x)
    return x
@eel.expose
def consultarNCM(codigo):
    xx = df1[df1['NCM']==codigo]
    print(xx['Categoria'][0])
    y=dict()
    y['cat'] = xx['Categoria'][0]
    y['valor'] = 10
    print(y)
    return y


eel.start('main.html',size=(largura, altura))
