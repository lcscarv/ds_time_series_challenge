"""This is a boilerplate pipeline 'training' generated using Kedro 0.18.4."""
import numpy as np
from statsforecast import StatsForecast
from statsforecast.models import (
    AutoARIMA,
    AutoETS,
    SimpleExponentialSmoothingOptimized,
    HistoricAverage,
    RandomWalkWithDrift
)
import json

def forecasting(long_forecasting_df):
    rel_path = 'src/time_series_indicium/pipelines/training/json_files/'
    
    with open(rel_path + 'best_models.json', 'r') as j:
     best_model_dict = json.loads(j.read())
     
    models = [
    AutoARIMA(season_length=1),
    AutoETS(season_length=1),
    SimpleExponentialSmoothingOptimized(),
    HistoricAverage(),
    RandomWalkWithDrift()
]

    sf = StatsForecast(
    df=long_forecasting_df, 
    models=models,
    freq='A', 
    n_jobs=-1
    )
    forecasts_df = sf.forecast(h=5)
    
    best_model_df = forecasts_df.copy()

    # Iterate through the dictionary and update values with the best model predictions
    for index, best_model in best_model_dict.items():
        best_model_df.loc[best_model_df.index == index, list(forecasts_df.drop('ds',axis =1).columns)] = float('NaN') # Set all predictions to nan
        best_model_df.loc[best_model_df.index == index, best_model] = forecasts_df.loc[forecasts_df.index == index, best_model].values

    def combine_models(row):
        non_nan_values = [val for val in row[list(forecasts_df.drop('ds',axis = 1).columns)] if np.isnan(val) == False]
        if len(non_nan_values) == 1:
            return non_nan_values[0]
        return non_nan_values

    best_model_df['best_model'] = best_model_df.apply(combine_models, axis = 1)
    best_model_df = best_model_df.drop(list(forecasts_df.drop('ds',axis = 1).columns),axis = 1)
    
    
    return best_model_df
