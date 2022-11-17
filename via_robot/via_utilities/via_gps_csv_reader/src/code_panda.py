import numpy as np
import pandas as pd

data = pd.read_csv("Teste3.csv")
data2 = pd.read_csv('Teste3.csv',usecols=['Latitude'])

print('Number of lines = ',len(data),'\n')
print('Dimensions = ',np.shape(data),'\n')
print('Type = ',type(data),'\n')
print(data)

#print('\n','\n','First line = ',data[:,1])