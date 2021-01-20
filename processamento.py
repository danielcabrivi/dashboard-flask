import pandas as pd
import datetime as dt



def getDescribe():
    df = pd.read_csv("D:/Projetos/igti/flask/files/temperature.csv")
    return df.describe().round(2)

def getListTemp():
    df = pd.read_csv("D:/Projetos/igti/flask/files/temperature.csv")
    return df['temperatura'].values.tolist()

def getListDate():
    df = pd.read_csv("D:/Projetos/igti/flask/files/temperature.csv")
    return pd.to_datetime(df['date']).dt.strftime('%m/%d/%Y').values.tolist()

def getHead(qtd):
    df = pd.read_csv("D:/Projetos/igti/flask/files/temperature.csv")
    return df.head(qtd)