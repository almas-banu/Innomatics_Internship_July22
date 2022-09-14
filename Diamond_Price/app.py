import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




st.set_page_config(page_title="Diamond", page_icon="💎")
#Loading the dataset
df=pd.read_csv('dataset/diamonds.csv')

st.title("Diamond")
st.header("Home Page")

def distPlot(x):
    fig = plt.figure(figsize=(10, 4))
    sns.distplot(df.x)
    st.pyplot(fig)
    
def countPlot(x):
    fig = plt.figure(figsize=(10, 4))
    sns.countplot(x = x, data = df)
    st.pyplot(fig)
    

st.sidebar.success("Select Your Page")

option = st.selectbox(
     'What information you want from dataset',
     (' ','Head', 'Tail', 'describe','Check null values'))

if option == ' ':
    pass
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
     (' ','Price', 'Carat','Cut','Clarity','Color'))

if visual == ' ':
    pass
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

st.subheader("Bivariate Analysis")
option = st.selectbox(
     'Select',
     (' ','Correlation', 'Heatmap'))

if option == ' ':
    pass
if option == 'Correlation':
    st.write(df.corr())
if option == 'Heatmap':
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), ax=ax)
    st.write(fig)




