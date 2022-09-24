import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Loading the dataset
df = pd.read_csv("dataset/diamonds.csv")
target_df = df[['price']]
df = df.drop('price', axis = 1)
df = pd.concat([df, target_df], axis = 1)
df[['x','y','z']] = df[['x','y','z']].replace(0, np.NaN)
df.dropna(inplace = True)

#Functions for plots 
def distPlot(x):
    fig = plt.figure(figsize=(10, 4))
    sns.distplot(df.x)
    st.pyplot(fig)
    
def countPlot(x):
    fig = plt.figure(figsize=(10, 4))
    sns.countplot(x = x, data = df)
    st.pyplot(fig)
    

#Heatmap
df_corr = df.corr()
fig, ax = plt.subplots(figsize=(12,8))
ax = sns.heatmap(df_corr , xticklabels = df_corr.columns , yticklabels = df_corr.columns , annot=True)

# Splitting the target and independent columns
X = df[['carat', 'cut', 'color', 'clarity', 'x', 'y', 'z']]
y = df[['price']]

# Splitting data into train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 4)

# Label Encoding
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelEncoder
# For train data
lae = LabelEncoder()
X_train['cut']=lae.fit_transform(X_train['cut'])
X_train['color']=lae.fit_transform(X_train['color'])
X_train['clarity']=lae.fit_transform(X_train['clarity'])
# For test data
X_test['cut']=lae.fit_transform(X_test['cut'])
X_test['color']=lae.fit_transform(X_test['color'])
X_test['clarity']=lae.fit_transform(X_test['clarity'])

# Standardization
# Data preprocessing on training data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_rescaled = pd.DataFrame(scaler.fit_transform(X_train),
                                columns = X_train.columns,
                                index = X_train.index)

# Data preprocessing on testing data
X_test_rescaled = pd.DataFrame(scaler.transform(X_test),
                               columns = X_test.columns,
                               index = X_test.index)

### STREAMLIT CODE ###

st.set_page_config(page_title="Welcome", page_icon="🔹")
st.title(" Diamond 💎")

# display the whole dataset
if(st.checkbox("Dataset")):
    st.write(df)
    
option = st.selectbox(
     'What information you want from dataset',
     ('Head', 'Tail', 'describe','Check null values'))
if option == 'Head':
    st.write(df.head())
if option == 'Tail':
    st.write(df.tail())
if option == 'Check null values':
    st.write(df.isnull().sum())
if option == 'describe':
    st.write(df.describe())

st.subheader("Visualization")

visual = st.radio(
     "What do you want to visualize",
     ('Price', 'Carat','Cut','Clarity','Color'))

if visual == 'Price':
    distPlot('price')
if visual == 'Carat':
    distPlot('carat')  
if visual == 'Cut':
    countPlot('cut')
if visual == 'Clarity':
    countPlot('clarity')
if visual == 'Color':
    countPlot('color')
    
# correlation between features
if(st.checkbox("Correlation between features")):
    st.pyplot(fig)
    st.write("Carat, x(Length), y(Width) and z(Depth) are highly correlated with price")
    st.write("So we will not be using table and depth (Percentage) for Price Prediction")

