import streamlit as st
import numpy as np
from pickle import load

scaler = load(open('models/scaler.pkl','rb'))
final_model = load(open('models/model.pkl','rb'))


st.header("Diamond Price Prediction")

car = st.text_input("Carat ", placeholder="Enter the carat")
cut = st.slider("Select the Cut",1,5)
colr = st.slider("Select the Color",1,7)
clar = st.slider("Select the Clarity",1,8)
dept = st.text_input("Depth", placeholder="Enter the depth")
tabl = st.text_input("Table", placeholder="Enter the table")
vol = st.text_input("Volume", placeholder="Enter the volume(in mm)")

btn_click = st.button("Predict")

if btn_click == True:
    if car and cut and colr and clar and dept and tabl and vol:
        query_point = np.array([float(car),float(cut),float(colr),float(clar),float(dept),float(tabl),float(vol)]).reshape(1,-1)
        query_point_transformed = scaler.transform(query_point)
        prediction = final_model.predict(query_point_transformed)
        st.text("The Price of your diamond is $ {:.2f}".format(prediction[0]))
        st.balloons()
    else:
        st.error("Enter the values properly.")
        st.snow()