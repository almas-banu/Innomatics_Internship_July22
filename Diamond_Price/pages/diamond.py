import streamlit as st
st.set_page_config(page_title="Diamond", page_icon="🔹")
st.header("Models 💠")
st.subheader("About the diamond dataset")
st.text('''
    • The seventh column 'price' is the values to be predicted.
    • Data Type : Mixed ( Numerical + Categorical)
    • Dataset has nearly 54000 instances.
    • It has 10 features.
    • Features
        price : price in US dollars ($ 326 -  $ 18,823)    
        carat : weight of the diamond   (0.2--5.01)
        cut   : quality of the cut    (Fair, Good, Very Good, Premium, Ideal)
        color : diamond colour, from J (worst) to D (best)    
        clarity : a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))    
        x : length in mm (0 - 10.74)   
        y : width in mm (0 - 58.9)    
        z : depth in mm (0 - 31.8)    
        depth : total depth percentage = z / mean(x, y) = 2 * z / (x + y) (43 -- 79)
        table : width of top of diamond relative to widest point (43 -- 95)
    ''')

st.subheader("Which Model is used for Prediction?")
model = st.radio(
     "Accuracy of Models",
     ('Linear Regression Model','Decision Tree Regressor Model','KNN Model','Random Forest Regression Model'))

if model == "Linear Regression Model":
    st.success("R2 Score:  0.89")
if model == "Decision Tree Regressor Model":
    st.success("R2 Score:  0.96")
if model == "KNN Model":
    st.success("R2 Score:  0.97")
if model == "Random Forest Regression Model":
    st.success("R2 Score:  0.98")

if(st.checkbox("Model Selected for Prediction")):
    st.subheader("KNN Model 💎")
    if(st.button("Why")):
        st.write("Though RandomForestRegressor model has more accuracy but it is large model to store(large file size) so KNN Model is selected for prediction")


