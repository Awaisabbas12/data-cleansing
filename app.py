# Importing modules
import pandas as pd
import numpy as np
import math
data = pd.read_excel('F:\pythonclass\module2\class4\SaleData.xlsx')
data
# Adding a column
data['faltu'] = [math.sqrt(a) for a in range(45)]
data
data['Tax'] = [(a*0.10) for a in data['Sale_amt']]
data
df = data.copy()
del df['faltu']
df
# Fancy Inexing
data[1:20,'Region':'SalesMan']
data.loc[1:20,'Region':'SalesMan']
data.columns
data.loc[4:30,'Manager':'Item']
data.loc[1:10,['Item','SalesMan']]
data.iloc[1:10,1:5]
data.iloc[:,1:5]
data.iloc[1:10,:]
# Data Cleansing
df = pd.read_csv('F:\pythonclass\module2\Class6\car_data.csv')
df
df.head()
df.info()
df.shape()
df.shape
df.columns
df.name.isnull().sum()
df[df.year.str.isnumeric()]
df[~df.year.str.isnumeric()]
df.isnull().sum()
df.duplicated().sum()
df[df.duplicated()]
df.dropna(inplace = True)
df
df.info()
df.drop_duplicates(inplace = True)
df.info()
df.name = df.name.str.split(' ').str[0:2].str.join(' ')
df.name
df.company.unique()
df.year=df.year.astype('int')
df
df.info()
df.year.value_counts()
df.columns
df.Price.unique()
df.Price.value_counts()
df = df[df.Price!='Ask For Price']
df
df.Price.value_counts()
df.Price = df.Price.str.replace(',','').astype('int')
df.Price
df.columns
df.kms_driven
df.kms_driven = df.kms_driven.str.replace('kms','').str.replace(',','').astype('float')
df.fuel_type.unique()
df.info()
df.to_csv("cleaned_data.csv")
