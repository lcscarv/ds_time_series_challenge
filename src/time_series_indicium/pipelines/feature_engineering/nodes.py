"""This is a boilerplate pipeline 'feature_engineering' generated using Kedro
0.18.4."""
import pandas as pd
import numpy as np 
import miceforest as mf 
import json

def missing_data_imputation(df, mice_groups,economic_groups,missing_countries, continents_regions):
    
    new_df = df.copy()
    new_df = new_df.astype(float)
    rel_path = 'src/time_series_indicium/pipelines/feature_engineering/json_files/'
    with open(rel_path + 'mice_groups.json', 'r') as j:
     mice_groups = json.loads(j.read())
     
    with open(rel_path + 'economic_groups.json', 'r') as j:
     economic_groups = json.loads(j.read())
     
    with open(rel_path + 'missing_countries.json', 'r') as j:
     missing_countries = json.loads(j.read())
     
    with open(rel_path + 'continents_regions.json', 'r') as j:
     continents_regions = json.loads(j.read())
     
    
    
    major_advanced_economies =  economic_groups['major_advanced_economies']
    other_advanced_economies =  economic_groups['other_advanced_economies']
    european_union = economic_groups['european_union']
    asean_5 = economic_groups['asean_5']
    euro_area = economic_groups['euro_area']
    emerging_developing_asia = economic_groups['emerging_developing_asia']
    emerging_developing_europe = economic_groups['emerging_developing_europe']
    latin_american_caribean = economic_groups['latin_american_caribean']
    middle_east_central_asia = economic_groups['middle_east_central_asia']
    sub_saharan_africa =  economic_groups['sub_saharan_africa']
    
    african_groups = mice_groups['african_groups']
    african_group_names = mice_groups['african_group_names']

    middle_east_groups = mice_groups['middle_east_groups']
    middle_east_group_names = mice_groups['middle_east_group_names']
    

    missing_african_countries = missing_countries['missing_african_countries']
    missing_middle_east_countries = missing_countries['missing_middle_east_countries']
    remaining_missing_countries = missing_countries['remaining_missing_countries']
    africa = continents_regions['africa']
    central_asia_causasus_countries = continents_regions['central_asia_causasus_countries']
    
    
    def avg_neigh_imputation(neighbours,country):
        return lambda row:np.mean([row[n] for n in neighbours]) if np.isnan(row[country]) else row[country]
    
    def mice_imputation(df,groups,group_names):
        
        df_dict = {str(key):None for key in group_names}
        i = 0
        for group in groups:
            kds = mf.ImputationKernel(
          df[group],
          save_all_iterations=True,
          random_state=42
        )
        
        # Run the MICE algorithm for 5 iterations
            kds.mice(5)

            # Return the completed dataset.
            df_imputed = kds.complete_data()
            df_imputed['Year'] = np.arange(1980,2029,1)
            df_dict[group_names[i]] = df_imputed
            i+=1
        
    
        return df_dict
    
    world_africa = ((new_df['World'] - new_df['Sub-Saharan Africa'])/new_df['World']).mean()
    world_euro = ((new_df['World'] - new_df['Euro area'])/new_df['World']).mean()
    
    new_df['Sub-Saharan Africa'] = new_df.apply(lambda row:row['World']*world_africa if np.isnan(row['Sub-Saharan Africa']) else row['Sub-Saharan Africa'],axis = 1)
    new_df['Euro area'] = new_df.apply(lambda row:row['World']*world_africa if np.isnan(row['Euro area']) else row['Euro area'],axis = 1)
    
    
    sub_saharan_dict = mice_imputation(new_df,african_groups,african_group_names)
    
    i = 0
    for country in missing_african_countries:
        new_df[country] = sub_saharan_dict[african_group_names[i]][country]
        i+=1

    middle_east_dict = mice_imputation(new_df,middle_east_groups,middle_east_group_names)
    
    j = 0
    for country in missing_middle_east_countries:
        new_df[country] = middle_east_dict[middle_east_group_names[j]][country]
        j+=1
    
    
    new_df['Africa (Region)'] = new_df.apply(avg_neigh_imputation([africa],'Africa (Region)'),axis = 1)
    
    new_df['Central Asia and the Caucasus'] = new_df.apply(avg_neigh_imputation([central_asia_causasus_countries],'Central Asia and the Caucasus'),axis = 1)
    
    new_df['Sub-Saharan Africa (Region) '] = new_df.apply(avg_neigh_imputation([sub_saharan_africa],'Sub-Saharan Africa (Region) '),axis = 1)
    
    
    other_advanced_economies.extend(['Western Europe','Eastern Europe ','Southeast Asia','South America'])
    european_union.extend(['Western Europe'])
    euro_area.extend(['Western Europe'])
    emerging_developing_asia.extend(['South Asia','Southeast Asia','Pacific Islands '])
    emerging_developing_europe.extend(['Western Europe', 'Eastern Europe '])
    latin_american_caribean.extend(['South America'])
    
    remaining_groups = [
    other_advanced_economies,
    european_union,
    euro_area,
    emerging_developing_asia,
    emerging_developing_europe,
    latin_american_caribean]

    remaining_group_names = [
    'other_advanced_economies',
    'european_union',
    'euro_area',
    'emerging_developing_asia',
    'emerging_developing_europe',
    'latin_american_caribean']
    
    remaining_groups_dict = mice_imputation(new_df,remaining_groups,remaining_group_names)
    
    #for group in remaining_groups:
    for group,country_list in remaining_missing_countries.items():
        for k in range(len(country_list)):
            new_df[country_list[k]] = remaining_groups_dict[group][country_list[k]]
    
    return new_df


def feature_engineering(df):
    forecast_df = df.query('index >= 1980 and index <= 2023')
    
    wide_forecast_df = forecast_df.T
    wide_forecast_df['Country'] = wide_forecast_df.index
    wide_forecast_df = wide_forecast_df.reset_index()
    wide_forecast_df = wide_forecast_df.drop('index',axis = 1)
    wide_forecast_df.columns.name = None
    
    years = np.arange(1980,2024,1)
    long_forecasting_df = pd.melt(wide_forecast_df, id_vars='Country', value_vars= years, var_name='ds', value_name='y')
    long_forecasting_df =long_forecasting_df.rename(columns={'Country':'unique_id'})
    
    long_forecasting_df['ds'] = pd.to_datetime(long_forecasting_df['ds'],format='%Y')
    long_forecasting_df['ds'] = long_forecasting_df['ds'].apply(lambda date: date.replace(month=12, day=31))

    # Convert back to the desired string format
    long_forecasting_df['ds'] = pd.to_datetime(long_forecasting_df['ds'])
    
    return long_forecasting_df