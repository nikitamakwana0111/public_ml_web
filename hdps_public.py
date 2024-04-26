# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:28:35 2024

@author: BHUMI
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Heart Disease Prediction System',
                          ['Heart Disease Prediction'],
                          icons=['heart'],
                          default_index=0)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # page title
    st.title('Heart Disease Prediction using ML')

    # Input fields for user data
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('trestbps')
        fbs = st.text_input('fbs > 120 mg/dl')
        restecg = st.text_input(' restecg')
        oldpeak = st.text_input('oldpeak')
        ca = st.text_input('ca')

    with col2:
        sex = st.text_input('Sex')
        chol = st.text_input('Chol in mg/dl')
        thalach = st.text_input('thalach')
        exang = st.text_input('exang')
        slope = st.text_input('lope')

    with col3:
        cp = st.text_input('Chest Pain types')
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # Convert input values to numeric types
    try:
        age = float(age)
        sex = float(sex)
        cp = float(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = float(fbs)
        restecg = float(restecg)
        thalach = float(thalach)
        exang = float(exang)
        oldpeak = float(oldpeak)
        slope = float(slope)
        ca = float(ca)
        thal = float(thal)
    except ValueError:
        st.error('Please enter valid numeric values for all input fields.')
        st.stop()

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
