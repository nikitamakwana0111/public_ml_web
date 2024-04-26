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
if (selected == 'Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age')

    with col2:
        sex = st.selectbox('Sex', ['0', '1'])

    with col3:
        cp = st.selectbox('Chest Pain types', ['0', '1', '2', '3'])

    with col1:
        trestbps = st.number_input('Resting Blood Pressure')

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['0', '1'])

    with col1:
        restecg = st.selectbox('Resting Electrocardiographic results', ['0', '1', '2'])

    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.selectbox('Exercise Induced Angina', ['0', '1'])

    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')

    with col2:
        slope = st.selectbox('Slope of the peak exercise ST segment', ['0', '1', '2'])

    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.selectbox('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', ['0', '1', '2'])

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, int(sex), int(cp), trestbps, chol, int(fbs), int(restecg), thalach, int(exang), oldpeak, int(slope), ca, int(thal)]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

        st.success(heart_diagnosis)
