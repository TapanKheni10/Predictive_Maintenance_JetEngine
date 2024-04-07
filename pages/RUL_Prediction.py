import streamlit as st
import numpy as np
from PredictiveMaintenance.pipeline import prediction

st.set_page_config(
    page_title="Prediction",
    page_icon="🛩️",
    layout="wide"
)

st.header("RUL (Remaining Useful Life) Predictor", divider="rainbow")
st.write("""
    Please enter the requested sensor data of the turbofan jet engine, and
    the model will predict the RUL (Remaining Useful Life) of it.
""")

choice = st.radio("**What kind of predictions you want to make?**", ["Sea Level", "Non-sea Leval"],
                  index=None, captions=["There is only one operational condition",
                                        "There are six different operational conditions"], label_visibility="hidden")

if choice=="Sea Level":
    ## Creating a data collection form
    with st.form("pred form", clear_on_submit=False, border=True):
        cycle = st.number_input("Times/ in cycle", value=None, placeholder="current operational cycle of the engine")
        LPC_temperature = st.number_input("Total LPC outlet temperature", value=None, placeholder="current LPC outlet temperature")
        HPC_temperature = st.number_input("Total HPC outlet temperature", value=None, placeholder="current HPC outlet temperature")
        LPT_temperature = st.number_input("Total LPT outlet temperature", value=None, placeholder="current LPT outlet temperature")
        bypass_pressure = st.number_input("Total bypass-duct pressure", value=None, placeholder="current bypass-duct pressure")
        HPC_pressure = st.number_input("Total HPC outlet pressure", value=None, placeholder="current HPC outlet pressure")
        physical_fan_speed = st.number_input("Physical fan speed", value=None, placeholder="current physical fan speed")
        physical_core_speed = st.number_input("Physical core speed", value=None, placeholder="current physical core speed")
        p50 = st.number_input("Engine pressure ratio(P50/P2)", value=None, placeholder="current pressure ratio")
        static_HPC_pressure = st.number_input("Static HPC outlet pressure", value=None, placeholder="current static HPC outlet pressure")
        fuel_flow_ration = st.number_input("Ratio of fuel flow to Ps30", value=None, placeholder="current fuel flow ration")
        corrected_fan_speed = st.number_input("Corrected fan speed", value=None, placeholder="current corrected fan speed")
        bleed = st.number_input("Bleed enthalpy", value=None, placeholder="current bleed enthalpy")
        LPT_coolant_bleed = st.number_input("LPT coolant bleed", value=None, placeholder="current LPT coolant bleed")

        submitted = st.form_submit_button("Make Prediction")

        if submitted:
            data = [LPC_temperature, HPC_temperature, LPT_temperature, bypass_pressure, HPC_pressure, physical_fan_speed,
                    physical_core_speed, p50, static_HPC_pressure, fuel_flow_ration, corrected_fan_speed, bleed, 
                    LPT_coolant_bleed, cycle]
            
            data = np.array(data).reshape(1, 14)

            obj = prediction.PredictionPipeline()
            predicted_RUL = obj.predict(data)

            if predicted_RUL < 20:
                st.error(f"Very soon, the engine will require maintenance.", icon='👨‍🔧')
                st.write(f"\nRemaining usefull cycles: {predicted_RUL}")
            else:
                st.success(f"The engine is healthy, no maintenance required.", icon="✅")
                st.write(f"\nRemaining usefull cycles: {predicted_RUL}")
                
if choice=="Non-sea Level":
    pass