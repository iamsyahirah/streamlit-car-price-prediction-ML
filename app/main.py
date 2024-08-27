import pickle
import streamlit as st

model = pickle.load(open('data/car_prediction.sav','rb'))

st.title('Predicting the Price of a Car')

year = st.number_input('Car Year Input')
mileage = st.number_input('Car KM Input')
tax = st.number_input('Car Tax Input')
mpg = st.number_input('Distance Car Input')
engineSize = st.number_input('Engine Size Input')

predict = ''

if st.button('Predict Price'):
    predict = model.predict(
        [[year,mileage, tax, mpg, engineSize]]
    )
    st.write('Prediction for car price in pounds: ', predict)
    st.write('Prediction for car price in MYR: ', predict*5.72)