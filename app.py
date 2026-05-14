import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("AI Intrusion Detection System")

st.write("Enter sample input (comma separated numbers):")

input_data = st.text_input("Input Data")

if st.button("Predict"):
    try:
        data = np.array([list(map(float, input_data.split(",")))])
        prediction = model.predict(data)

        if prediction[0] == 0:
            st.success("Normal Traffic ✅")
        else:
            st.error("Attack Detected ⚠️")

    except:
        st.warning("Invalid Input ❌")