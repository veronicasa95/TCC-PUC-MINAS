# -*- coding: utf-8 -*-
### Bibliotecas

import pandas as pd
import glob

caminho_acidentes = r'C:\Users\Verônica Sá\Documents\TCC_PUC_MINAS\TCC-PUC-MINAS\files\acidentes_antt' 
path = r'C:\Users\Verônica Sá\Documents\TCC_PUC_MINAS\TCC-PUC-MINAS\files\acidentes_antt' # use your path

def mergeMultipleCsvs(path):
    
'''
all_files = glob.glob(path + "/*.csv")
li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0, delimiter = ";", encoding="iso8859-1")
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)


pd.DataFrame.to_csv(frame,r"C:\Users\Verônica Sá\Documents\TCC_PUC_MINAS\TCC-PUC-MINAS\files\acidentes_antt\acidentes_total.csv",index=False)
'''

def acidente(caminho):
    df = pd.read_csv(caminho)
    ## tratamento
    return df

df_acidente = acidente(caminho_acidentes)