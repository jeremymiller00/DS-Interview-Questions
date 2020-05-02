import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns  

data = pd.read_csv('fitness_smoking_data.csv', sep=',')
data['total'] = data.sum(axis=1)
data['prop_low'] = data['Low fitness level'] / data['total']
data['prop_med_low'] = data['Medium-low fitness level'] / data['total']
data['prop_med_high'] = data['Medium-high fitness level'] / data['total']
data['prop_high'] = data['High fitness level'] / data['total']
data_props = data[['prop_low', 'prop_med_low', 'prop_med_high', 'prop_high']]
# data_props.reset_index(inplace=True)
# data_props.rename( {'index': 'smoking_level'}, axis=1, inplace=True )
data_props.plot(kind='bar')