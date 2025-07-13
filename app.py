import streamlit as st
from model import make_pred

st.set_page_config(
    page_title = " Predict your Diabetes "
)

st.title('Diabetes Prediction')
st.header('Input your head: ')

glucose = st.number_input('Glucose', min_value = 0, max_value = 400, value = 100 )
blood_pressure = st.number_input('Blood Pressure', 50,300,120)
dfp = st.number_input('DFP',0,10,0)
age = st.number_input('Age', 20,80,40)


if st.button('Predict'):
    input = [glucose,blood_pressure,dfp,age]
    prediction = make_pred(input)

    if prediction[0] == 1:
        st.error('High Risk Catagory')
        st.write('See a Doctor')
    
    else:
        st.success('low risk of diabetes')