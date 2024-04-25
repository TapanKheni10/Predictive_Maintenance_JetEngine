import streamlit as st
import numpy as np
from PredictiveMaintenance.pipeline.model_1 import prediction_1
from PredictiveMaintenance.pipeline.model_2 import prediction_2

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

choice = st.radio("**What kind of predictions you want to make?**", ["Sea Level", "Non-sea Level"],
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

            obj = prediction_1.PredictionPipeline()
            predicted_RUL = obj.predict(data)

            if predicted_RUL < 20:
                st.error(f"Very soon, the engine will require maintenance.", icon='👨‍🔧')
                st.write(f"\nRemaining usefull cycles: {predicted_RUL}")
            else:
                st.success(f"The engine is healthy, no maintenance required.", icon="✅")
                st.write(f"\nRemaining usefull cycles: {predicted_RUL}")
                
if choice=="Non-sea Level":
    with st.form("pred form", clear_on_submit=False, border=True):
        setting_1 = st.number_input("Altitude(Setting_1)", value=None, placeholder="current value of settings 1")
        LPC_outlet_temperature = st.number_input("Total LPC outlet temperature", value=None, placeholder="current LPC outlet temperature")
        HPC_outlet_temperature = st.number_input("Total HPC outlet temperature", value=None, placeholder="current HPC outlet temperature")
        LPT_outlet_temperature = st.number_input("Total LPT outlet temperature", value=None, placeholder="current LPT outlet temperature")
        bypass_pressure = st.number_input("Total bypass-duct pressure", value=None, placeholder="current bypass-duct pressure")
        HPC_outlet_pressure = st.number_input("Total HPC outlet pressure", value=None, placeholder="current HPC outlet pressure")
        physical_fan_speed = st.number_input("Physical fan speed", value=None, placeholder="current physical fan speed")
        physical_core_speed = st.number_input("Physical core speed", value=None, placeholder="current physical core speed")
        static_HPC_outlet_pressure = st.number_input("Static HPC outlet pressure", value=None, placeholder="current static HPC outlet pressure") 
        fuel_flow_Ps30 = st.number_input("Ratio of fuel flow to Ps30", value=None, placeholder="current ratio of fuel flow to Ps30")
        corrected_fan_speed = st.number_input("corrected fan speed", value=None, placeholder="current corrected fan speed")
        corrected_core_speed = st.number_input("corrected_core_speed", value=None, placeholder="current corrected fan speed")
        bypass_ratio = st.number_input("bypass ratio", value=None, placeholder="current bypass ratio")
        HPT_coolant_bleed = st.number_input("HPT coolant bleed", value=None, placeholder="current HPT coolant bleed")
        LPT_coolant_bleed = st.number_input("LPT coolant bleed", value=None, placeholder="current LPT coolant bleed")

        submitted = st.form_submit_button("Make Prediction")

        if submitted:
            data = [setting_1, LPC_outlet_temperature, HPC_outlet_temperature, LPT_outlet_temperature, bypass_pressure,
                    HPC_outlet_pressure, physical_fan_speed, physical_core_speed, static_HPC_outlet_pressure, fuel_flow_Ps30,
                    corrected_fan_speed, corrected_core_speed, bypass_ratio, HPT_coolant_bleed, LPT_coolant_bleed]
            
            data = np.array(data).reshape(1, 15)

            obj = prediction_2.PredictionPipeline()
            predicted_RUL = obj.predict(data)

            if predicted_RUL < 20:
                st.error(f"Very soon, the engine will require maintenance.", icon='👨‍🔧')
                st.write(f"\nRemaining usefull cycles: {predicted_RUL}")
            else:
                st.success(f"The engine is healthy, no maintenance required.", icon="✅")
                st.write(f"\nRemaining usefull cycles: {predicted_RUL}")