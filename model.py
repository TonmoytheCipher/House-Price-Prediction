import pandas as pd
import numpy as np

df = pd.read_csv('house_data.csv')

X = df[['size_sqft', 'bedrooms', 'floors', 'age']].values
Y = df[['price_thousands']].values.reshape(-1,1)

print(X.shape)
print(Y.shape)

