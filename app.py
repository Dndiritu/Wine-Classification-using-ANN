import streamlit as st
import joblib
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
#load the pre-trained model
model=load_model('wine_model.keras')
scaler=joblib.load('scalerrr.pkl')

st.write('Wine Quality Prediction')
st.write('Enter the features of the wine to predict its quality')

#input fields for the features
feature_names = [
    'alcohol',
    'malic_acid',
    'ash',
    'alcalinity_of_ash',
    'magnesium',
    'total_phenols',
    'flavanoids',
    'nonflavanoid_phenols',
    'proanthocyanins',
    'color_intensity',
    'hue',
    'od280/od315_of_diluted_wines',
    'proline'
]
inputs=[st.number_input(f"{feature}",min_value=0.0,step=0.1) for feature in feature_names]

if st.button('predict'):
    #create a Dataframe for the inputs
    input_data = pd.DataFrame([inputs], columns=feature_names)

    #scale the input data
    scaled_data = scaler.transform(input_data)

    #Make prediction
    prediction = model.predict(scaled_data)

    #Display the prediction
    st.write(f'Predicted Wine Quality: {np.argmax(prediction) +1 }')  #assuming quality 1-10
