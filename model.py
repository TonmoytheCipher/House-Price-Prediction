import pandas as pd
import numpy as np

df = pd.read_csv('house_data.csv')

X = df[['size_sqft', 'bedrooms', 'floors', 'age']].values
Y = df[['price_thousands']].values.reshape(-1,1)

# print(X.shape)
# print(Y.shape)
# #checking
# print("Range = ", np.max(X, axis=0) - np.min(X, axis=0))
# print("Price range: ", np.max(Y) - np.min(Y))

#z score normalization
mu = np.mean(X, axis =0)
st = np.std(X, axis = 0)
X_norm = (X-mu)/st 

# print("Range ", np.max(X_norm, axis=0) - np.min(X_norm, axis=0))
y = Y.flatten() 
w = np.zeros(X_norm.shape[1])
b = 0.0

# x = X_norm[0]
# print("Prediction = ", np.dot(X_norm,w)+b )
def compute_cost(X,y,w,b):
    m = X.shape[0]
    y1 = np.dot(X,w) + b
    j_wb = (np.sum((y1 - y)**2))/(2*m)
    return j_wb
print(compute_cost(X_norm, y , w,b))
# print(np.sum(y**2) / (2 * len(y))) 

def compute_gradient(X,y,w,b):
    m = X.shape[0]
    err = np.dot(X,w) + b - y;
    dj_dw = (np.dot(X.T,err))/m
    dj_db = np.sum(err)/m
    return dj_dw, dj_db

dj_dw,dj_db=compute_gradient(X_norm,y,w,b)
print(dj_dw.shape, dj_db)
