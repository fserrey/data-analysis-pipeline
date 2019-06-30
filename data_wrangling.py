import pandas as pd 
import numpy as np 

def data_collect(file):
    df = pd.read_csv(file)
    return df

def putAlltogether(files_path, ext):   #ext must be a string of the extension type i.e. ".csv"
    alldocs = glob.glob(files_path + "/*" + ext)
    todf = pd.DataFrame()
    lista = []
    for doc in alldocs:
        df = pd.read_csv(doc, index_col = None, header = 0)
        lista.append(df)
    frame = pd.concat(lista, sort = True)
    cols = ['date', 'station', 'BEN', 'CH4', 'CO', 'EBE', 'MXY', 'NMHC', 'NO', 'NO_2', 'NOx', 'OXY',
       'O_3', 'PM10', 'PM25', 'PXY', 'SO_2', 'TCH', 'TOL']
    frame = frame[cols]
    return frame.sort_values(['station', 'date'])

def drop_null(df, percent):
    for column in df:
        result = (df[column].isnull().sum()/len(df))
        if result >= percent:
            del df[column]
    return df