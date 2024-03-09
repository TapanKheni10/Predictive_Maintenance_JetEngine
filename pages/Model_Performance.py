import streamlit as st
import pandas as pd
import json

with open("artifacts/model_evaluation/metrics.json", 'r') as f:
    data = json.load(f)

df = pd.DataFrame([data])

st.dataframe(df)