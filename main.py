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
    return x
@eel.expose
def consultarNCM(codigo):
    x = df1[df1['NCM']==codigo].to_dict()
    print(x)
    return x

consultarNCM(1012100)
eel.start('main.html',size=(largura, altura))
