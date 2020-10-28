import pandas as pd
# leitura dos dados csv
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")

def getDataHead(n):
    # visualizando as primeiras n linhas
    return df.head(n)

def getDescribe():

    # estatísticas básicas
    return df.describe()

def getInfo():

    # dataframe info
    df.info()