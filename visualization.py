import pandas as pd  
import matplotlib.pyplot as plt  

data = pd.read_csv('processed_data.csv')  
plt.scatter(data['porosity'], data['permeability'])  
plt.xlabel('Porosity')  
plt.ylabel('Permeability')  
plt.title('Reservoir Rock Properties')  
plt.savefig('reservoir_plot.png')  
plt.show()  