
import streamlit as st
from home_page import home_page
from about_page import about_page
from disease_recognition import disease_recognition
from disease_search import disease_search
from history_reports import history_reports

st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox(
    "Select Page", 
    ["Home", "About the Project", "Plant Disease Detection", "Disease Information", "History & Reports"]
)

if app_mode == "Home":
    home_page()
elif app_mode == "About the Project":
    about_page()
elif app_mode == "Plant Disease Detection":
    disease_recognition()
elif app_mode == "Disease Information":
    disease_search()
elif app_mode == "History & Reports":
    history_reports()


