"""This is a boilerplate pipeline 'preprocessing' generated using Kedro
0.18.4."""
import pandas as pd 
import json
import numpy as np
def preprocessing(df):
    
    change_names_dict = {'Russian Federation': 'Russia',"China, People's Republic of":'China',"Korea, Republic of":"Korea",'North Macedonia ':'North Macedonia',
                     "Micronesia, Fed. States of":'Micronesia',"Türkiye, Republic of":'Türkiye',"South Sudan, Republic of":'South Sudan',"Bahamas, The":'The Bahamas','Netherlands':'The Netherlands',
                    "Congo, Dem. Rep. of the": 'Democratic Republic of the Congo', "Congo, Republic of ":'Republic of Congo',"Gambia, The":'The Gambia'}
    df = df.dropna()
    df = df.replace('no data', np.nan)
    
    new_df = df.transpose()
    new_df.columns = new_df.iloc[0]
    new_df = new_df.iloc[1:]
    
    new_df.columns.name = None
    new_df.rename(columns=change_names_dict, inplace=True)

    return new_df

