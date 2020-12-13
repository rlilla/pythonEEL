import eel
import pandas as pd
from win32api import GetSystemMetrics

largura = GetSystemMetrics(0)
altura = GetSystemMetrics(1)

eel.init('web')
df=pd.read_csv("C://temp//teste.txt",sep=";")

@eel.expose
def teste(var1):
    print(var1)
@eel.expose
def consultar(descricao):
    x = df[df['descricao'].str.contains(descricao) | df['codigo'].str.contains(descricao)].to_dict()
    y=[10,20]
    print(x)
    return x


eel.start('main.html',size=(largura, altura))
