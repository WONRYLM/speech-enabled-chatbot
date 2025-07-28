import streamlit as st
import pandas as pd
import joblib
import requests
import os

MODEL_URL = "https://github.com/WONRYLM/streamlit-financial-inclusion/releases/download/v1.0/financial_inclusion_model.joblib"
MODEL_PATH = "financial_inclusion_model.joblib"

# Download the model 
if not os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'wb') as f:
        f.write(requests.get(MODEL_URL).content)

# Load model
model = joblib.load(MODEL_PATH)
# Load model and encoders
clf = joblib.load('financial_inclusion_model.joblib')
le_dict = joblib.load('label_encoders.joblib')

st.title("Financial Inclusion in Africa Prediction")

# Input fields
country = st.selectbox("Country", le_dict['country'].classes_)
year = st.number_input("Year", min_value=2010, max_value=2030, value=2018)
location_type = st.selectbox("Location Type", le_dict['location_type'].classes_)
cellphone_access = st.selectbox("Cellphone Access", le_dict['cellphone_access'].classes_)
household_size = st.number_input("Household Size", min_value=1, max_value=20, value=3)
age_of_respondent = st.number_input("Age of Respondent", min_value=15, max_value=100, value=30)
gender_of_respondent = st.selectbox("Gender", le_dict['gender_of_respondent'].classes_)
relationship_with_head = st.selectbox("Relationship with Head", le_dict['relationship_with_head'].classes_)
marital_status = st.selectbox("Marital Status", le_dict['marital_status'].classes_)
education_level = st.selectbox("Education Level", le_dict['education_level'].classes_)
job_type = st.selectbox("Job Type", le_dict['job_type'].classes_)

if st.button("Predict Bank Account Ownership"):
    # Encode inputs
    def encode_feature(col, val):
        le = le_dict[col]
        return le.transform([val])[0]

    input_data = pd.DataFrame({
        'country': [encode_feature('country', country)],
        'year': [year],
        'location_type': [encode_feature('location_type', location_type)],
        'cellphone_access': [encode_feature('cellphone_access', cellphone_access)],
        'household_size': [household_size],
        'age_of_respondent': [age_of_respondent],
        'gender_of_respondent': [encode_feature('gender_of_respondent', gender_of_respondent)],
        'relationship_with_head': [encode_feature('relationship_with_head', relationship_with_head)],
        'marital_status': [encode_feature('marital_status', marital_status)],
        'education_level': [encode_feature('education_level', education_level)],
        'job_type': [encode_feature('job_type', job_type)]
    })

    prediction = clf.predict(input_data)[0]

    if prediction == 1:
        st.success("Prediction: This individual likely has a bank account.")
    else:
        st.warning("Prediction: This individual likely does NOT have a bank account.")
