import streamlit as st
 
st.title("Housing Prices Prediction")
 
st.write("""
### Project description
        Welcome!!!
We have trained several models to predict the price of a house based on features such as the area of the house and the condition and quality of their different rooms. 
 
""")


import pickle
model = pickle.load(open('projects/iter-5/housing_iter5_KNN.ipynb', 'rb'))
 
LotArea = st.number_input("Lot Area")
TotalBsmtSF = st.number_input("Basement Square Feet")
BedroomAbvGr = st.number_input("Number of Bedrooms")
GarageCars = st.number_input("Car spaces in Garage")
 
import pandas as pd
new_house = pd.DataFrame({
    'LotArea':[LotArea],
    'TotalBsmtSF':[TotalBsmtSF], 
    'BedroomAbvGr':[BedroomAbvGr], 
    'GarageCars':[GarageCars]
})
 

prediction = model.predict(new_house)
 
st.write("The price of the house is:", prediction)
