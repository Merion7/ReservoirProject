import pandas as pd  

data = pd.read_csv('reservoir_data.csv')  
data['permeability_log'] = data['permeability'].apply(lambda x: x * 0.1)  
data.to_csv('processed_data.csv', index=False)  
print("Data processed! Check processed_data.csv")  