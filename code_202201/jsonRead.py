import pandas as pd

def readRawData():
    df = pd.read_json('data.json')
    return df

def checkKeysInjson(keys):
    df = pd.read_json('data.json')
    for k in keys:
        if k in [i for i in df.columns]:
            return 'Keys Available'
