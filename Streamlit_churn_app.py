# Streamlit application for predicting customer churn using a pre-trained model
# This app allows users to input customer data and get churn predictions
import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('expresso_churn_model.pkl')

st.title("📱 Expresso Churn Prediction App")
st.write("Fill in the client's data below to predict churn probability.")

# Input fields - Must match the training features exactly
region = st.selectbox('Region', [0, 1, 2, 3])
tenure = st.number_input('Tenure (months)', min_value=0, max_value=1000, value=24)
montant = st.number_input('Montant (Top-up amount)', min_value=0.0, value=1000.0)
frequence_rech = st.number_input('Recharge Frequency', min_value=0, value=5)
revenue = st.number_input('Monthly Revenue', min_value=0.0, value=1000.0)
arpu_segment = st.number_input('ARPU Segment', min_value=0.0, value=500.0)
frequence = st.number_input('Frequency', min_value=0, value=10)
data_volume = st.number_input('Data Volume', min_value=0.0, value=500.0)
on_net = st.number_input('On-Net Calls', min_value=0.0, value=200.0)
orange = st.number_input('Orange Calls', min_value=0.0, value=150.0)
tigo = st.number_input('Tigo Calls', min_value=0.0, value=100.0)
regularity = st.number_input('Regularity', min_value=0.0, value=20.0)
freq_top_pack = st.number_input('Top Pack Frequency', min_value=0, value=3)
top_pack = st.selectbox('Top Pack Type (encoded)', [0, 1, 2, 3])  
freq = st.number_input('Freq', min_value=0, value=5)

# Arrange the features in the exact same order as in model training
features = np.array([[region, tenure, montant, frequence_rech, revenue,
                      arpu_segment, frequence, data_volume, on_net,
                      orange, tigo, regularity, freq_top_pack, top_pack, freq]])

# Prediction
if st.button('Predict Churn'):
    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1]

    if prediction[0] == 1:
        st.error(f"🚨 The client is likely to churn. Probability: {probability:.2%}")
    else:
        st.success(f"✅ The client is unlikely to churn. Probability: {probability:.2%}")
