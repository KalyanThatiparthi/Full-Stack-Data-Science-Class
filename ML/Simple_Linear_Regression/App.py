import os
os.getcwd()
import streamlit as st
import pickle
import numpy as np

# Load the model from the file
file_path = 'linear_regression_model.pkl'
with open(file_path, 'rb') as file:
    loaded_model = pickle.load(file)
#    model = pickle.load(open(r'C:\Users\Jagatjyoti\Jagat_Code\06-05-2026\linear_regression_model.pkl', 'rb'))
# Create a Streamlit app
st.title("Salary Prediction Based on Years of Experience")
# Input for years of experience
years_experience = st.number_input("Enter years of experience:", min_value=0.0, step=0.1, max_value=50.0)
# Predict salary when the button is clicked
if st.button("Predict Salary"):
    # Reshape the input for prediction
    experience_input_data = np.array([[years_experience]])
    # Make the prediction using the loaded model
    predicted_salary = loaded_model.predict(experience_input_data)
    # Display the predicted salary
    st.write(f"Predicted Salary: ${predicted_salary[0]:.2f}")       
    
    st.write("The model was Trained using a dataset of 30 employees with varying years of experience and their corresponding salaries. The model is a simple linear regression that captures the relationship between years of experience and salary. The coefficient and intercept of the model indicate how much the salary is expected to increase for each additional year of experience.")
    