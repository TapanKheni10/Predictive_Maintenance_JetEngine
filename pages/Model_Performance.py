import streamlit as st
import pandas as pd
import json

with open("artifacts/model_1/model_evaluation/metrics.json", 'r') as f:
    data_1 = json.load(f)

with open("artifacts/model_2/model_evaluation/metrics.json", 'r') as f:
    data_2 = json.load(f)

df_1 = pd.DataFrame([data_1])
df_2 = pd.DataFrame([data_2])

st.dataframe(df_1)

st.dataframe(df_2)