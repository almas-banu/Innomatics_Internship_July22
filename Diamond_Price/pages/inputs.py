import streamlit as st

st.title("Diamond dataset")

st.subheader("INPUT TO BE GIVEN TO GET PRICE")

st.write("carat ")
st.write("cut  (Fair, Good, Very Good, Premium, Ideal)")
st.write("Fair - 1, Good - 2, Very Good - 3, Premium - 4, Ideal - 5")
st.write("color ") 
st.write(" 'E' : 1,'I' : 2,'J' : 3,'H' : 4,'F' : 5,'G' : 6,'D' : 7") 
st.write("clarity") 
st.write(" 'SI2' : 1,'SI1' : 2,'VS1' : 3,'VS2' : 4,'VVS2' : 5,'VVS1' : 6,'I1' : 7,'IF' : 8")
st.write("Instead of taking x,y and z values this app is taking volume so enter volume")
st.write("depth  ")
st.write("table ")

st.subheader("About the diamond dataset")
st.write('''
    1. Title : Diamonds Dataset
    2. The seventh column 'price' is the values to be predicted.
    3. Data Type : Mixed ( Numerical + Categorical)
    4. Dataset has nearly 54000 instances.
    5. It has 10 features.
    6. Features
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

