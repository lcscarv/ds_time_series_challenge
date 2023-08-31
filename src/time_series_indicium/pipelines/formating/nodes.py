"""This is a boilerplate pipeline 'serving' generated using Kedro 0.18.4."""
import pandas as pd

def long_to_wide_df(best_model_df,long_forecasting_df):
    
    best_model_df =best_model_df.reset_index()
    best_model_df = best_model_df.rename(columns = {'best_model':'y'}) 
    
    best_model_df.columns.name = None
    
    complete_long_df = pd.concat([long_forecasting_df,best_model_df], ignore_index = True)

    complete_long_df.columns = ['Country','Year','GDP index']

    complete_long_df['Year'] = complete_long_df['Year'].dt.strftime('%Y')
    
    wide_df = pd.pivot(complete_long_df, index= 'Country', columns= 'Year', values= 'GDP index')
    
    return wide_df

def final_format(wide_df,imf_dm_pp_df):
    reorder_list = list(imf_dm_pp_df.columns[1:229])
    
    final_df = wide_df.copy()
    final_df = final_df.reindex(reorder_list); final_df.columns.name = None
    
    final_df = final_df.reset_index(); final_df = final_df.rename(columns = {'Country':'Real GDP growth (Annual percent change)'})
    
    
    return final_df