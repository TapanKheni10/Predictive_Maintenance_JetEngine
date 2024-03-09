import streamlit as st
from PIL import Image

## Set the streamlit page configuration
st.set_page_config(
    page_title = "Home_Page",
    page_icon = "🛩️",
    layout = "wide",
    menu_items = {
        'Get Help' : "mailto: tapankheni10304@gmail.com",
        'About' : "pages/about.py"
    }
)

## Setting the title of the page
st.title("Predictive Maintanenance", help="predicting RUL(remaining useful life) of an jet engine")


## Setting sidebar
with st.sidebar:
    # choice = st.radio("**Choose from the below options:**",["Train Model", "Performance Measure", "Prediction"],
    #                   index=None, captions=["train a model on default dataset",
    #                                         "see the performance of various ML models",
    #                                         "make prediction on your own data"], label_visibility="hidden")
    
    st.write("\n")
    st.write("\n")
    st.write("""
        Let's leverage the power of AI 🤖 to provide better maintenance scheduling to the jet engines 
        by predicting unexpected downtimes 💥 and failures.
    """)

## Load and display logo
logo = Image.open("static/logo.jpeg")
left_col, center_col, right_col = st.columns(3)
with center_col:
    st.write("\n")
    st.image(logo)

st.header("Reducing Unwanted Downtimes, Improving Saftey", divider="rainbow")

st.write("""
    Machines are critical to all business nowadays, and we expect them to operate at peak level for long time. 
    Normally, we can use corrective maintenance strategy to make the best use of machines. 
    But we could end up costing even higher due to downtime and labor. 
         
    Preventive maintenance comes in to reduce unplanned failures while businesses try to address problem in advance. 
    However, the costs could still be high. By using predictive maintenance, we can prevent those unexpected problems more efficiently. 
    We can fix the machines just in time as we monitor and predict the status of them.
        
    Failure prediction is a major topic in predictive maintenance in many industries. 
    Airlines are particularly interested in predicting equipments failures in advance 
    so that they can enhance operations and reduce flight delays.
""")

st.write("""
    Observing engine's health and condition through sensors and telemetry data is assumed 
    to facilitate this type of maintenance by predicting Time-to-Failure (TTF) or 
    Remaining Useful Life (RUL) of in-service equipment. 
""")

st.header("How it works?", divider="rainbow")

st.write("""
    Our AI model trained on datasets contain simulated aircraft engine run-to-failure events, 
    operational settings, and 21 sensors measurements are provided by NASA Ames.
""")

st.write("\n")
st.write("""
    It is assumed that the engine progressing degradation pattern is reflected in its sensor measurements.
         
    This allows our AI to:
    - Identify the patterns in the sensors that indicates potential risks.
         
    This AI-enabled solutions has the potential to:
    - Significantly decreases the number of unwanted downtimes and failures
    - Reduce the cost of aviation industry
    - Ensure passengers safety
""")

st.header("What is the approach behind it?", divider="rainbow")

st.write("""
    By exploring the aircraft engine's sensor values over time, the machine learning algorithm can learn 
    the relationship between the sensor values and changes in sensor values to the historical failures 
    in order to predict failures in the future.
         
    - Regression Modeling algorithms were used to predict the number remaining cycles before engine failure.
    - Multiclass classification algorithms were used predict in which cycles window or period will an engine will fail.
""")

st.header("Who can Benefit from it?", divider="rainbow")

st.write("""
    - Airline companies
    - Maintenance staff
    - Technical engineers
    - Pilots
""")

