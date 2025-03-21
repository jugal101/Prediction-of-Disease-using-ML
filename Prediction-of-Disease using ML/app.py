import os
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction ',
                   layout='wide',
                   page_icon="🧑‍⚕️")

diabetes_model = pickle.load(open("./Saved-models/diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"./Saved-models/heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"./Saved-models/parkinson_model.sav", 'rb'))

with st.sidebar:
    selected = option_menu('Prediction of disease outbreak system',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson Disease Prediction'],
                           menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

def validate_input(inputs):
    try:
        return [float(x) for x in inputs]
    except ValueError:
        st.error("Please enter valid numeric values.")
        return None

if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction using ML")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')
    
    if st.button('Diabetes Test Result'):
        user_input = validate_input([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        if user_input:
            diab_prediction = diabetes_model.predict([user_input])
            st.success('The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic')

elif selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction Using ML")
    cols = st.columns(3)
    labels = ['Age', 'Sex (0: Female, 1: Male)', 'Chest Pain Type (0-3)', 'Resting Blood Pressure (mm Hg)',
              'Cholesterol level', 'Fasting Blood Sugar', 'ECG Results', 'Max Heart Rate Achieved',
              'Exercise-Induced Angina (1: Yes, 0: No)', 'ST Depression', 'ST Slope', 'Major Vessels', 'Thalassemia']
    inputs = [col.text_input(label) for col, label in zip(cols * 5, labels)]
    
    if st.button('Heart Disease Test Result'):
        user_input = validate_input(inputs)
        if user_input:
            heart_prediction = heart_disease_model.predict([user_input])
            st.success('The person has heart disease' if heart_prediction[0] == 1 else 'The person has no heart disease')

elif selected == "Parkinson Disease Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    cols = st.columns(5)
    labels = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
              'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
              'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR',
              'HNR', 'RPDE', 'DFA', 'Spread1', 'Spread2', 'D2', 'PPE']
    inputs = [col.text_input(label) for col, label in zip(cols * 5, labels)]
    
    if st.button("Parkinson's Test Result"):
        user_input = validate_input(inputs)
        if user_input:
            parkinsons_prediction = parkinsons_model.predict([user_input])
            st.success("The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease")
