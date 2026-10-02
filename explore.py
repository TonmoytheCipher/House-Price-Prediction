import pandas as pd

# data = {
#     "size_sqft": [1000, 1500, 2000, 2500, 3000],
#     "bedrooms":  [2,    3,    3,    4,    4   ],
#     "age_years": [20,   10,   5,    2,    1   ],
#     "price_usd": [200000, 280000, 350000, 430000, 500000]
# }
# df = pd.DataFrame(data)
# print(df)
# print(f"dataset shape = {df.shape}" )
# print(df.describe())
# print(df.dtypes)
# X = df[["size_sqft","bedrooms",  "age_years" ]]
# y = df["price_usd"]
# print("X_features : ")
# print(X)
# print("Y-features : ")
# print(y)

# print("\n X.shape  = ", X.shape)
# print("\n Y.shape = ", y.shape)
# print(df.isnull().sum()) #check for null data

df = pd.read_csv("house_data.csv")
# df = pd.read_csv("house_data.csv", usecols=["size_sqft","age", "price_thousands"]) //for specific attributes
print(df.sample())
# print(df)
# print(df.isnull().sum()) 