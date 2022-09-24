import streamlit as st
import numpy as np
from pickle import load

scaler = load(open('models/scaler.pkl', 'rb'))
knn_regressor = load(open('models/knn_model.pkl', 'rb'))

st.set_page_config(page_title="Predict", page_icon="✨")
st.title(" 💠 Lets Predict Diamond Price 💠")
st.subheader("Select the features of the Diamond:")

carat = st.slider("Select the Carat", 0.00, 6.00)
cut = st.selectbox("Select the Cut", ("Ideal", "Premium", "Very Good", "Good", "Fair"))
color = st.selectbox("Select the Color", ("D", "E", "F", "G", "H", "I","J"))
clarity = st.selectbox("Select the Clarity", ("I1", "IF", "SI1", "SI2", "VS1", "VS2", "VVS1", "VVS2"))
x = st.slider("Select the Length", 0.00, 15.00)
y = st.slider("Select the Width", 0.00, 65.00)
z = st.slider("Select the Depth", 0.00, 35.00)
btn_click = st.button("Price?")

if btn_click == True:
    if carat and cut and color and clarity and x and y and z:
        label_cut = {'Ideal':2, 'Premium':3, 'Very Good':4, 'Good':1, 'Fair':0}
        label_color = {'G':3, 'E':1, 'F':2, 'H':4, 'D':0, 'I':5, 'J':6}
        label_clarity = {'SI1':2, 'VS2':5, 'SI2':3, 'VS1': 4, 'VVS2':7, 'VVS1':6, 'IF':1, 'I1':0}
        cut_newlabel = label_cut[cut]
        color_newlabel= label_color[color]
        clarity_newlabel = label_clarity[clarity]
        query_point = np.array([carat, cut_newlabel, color_newlabel, clarity_newlabel, x, y, z])
        query_point = query_point.reshape(1, -1)
        query_point_transformed = scaler.transform(query_point)
        prediction = knn_regressor.predict(query_point_transformed)
        st.text("The Price of your diamond is : ")
        st.success(prediction)
        st.balloons()
    else:
        st.error("Enter the values properly!")
        st.snow()