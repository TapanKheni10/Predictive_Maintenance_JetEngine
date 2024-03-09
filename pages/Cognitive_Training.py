import streamlit as st
import subprocess

st.set_page_config(
    page_title="RUL training",
    page_icon="🛩️",
)

st.header("Model Training", divider="rainbow")
st.write("""
    Initiate the model training process by clicking the 'Start' button. 
    Please be aware that the duration of this training may vary, depending on the performance specifications of your device. 
    
    Thank you for your patience..
""")

if st.button("Start"):
    st.write("Magic is happening.......")

    subprocess.run(["python","main.py"])

    st.write("Model training completed.")