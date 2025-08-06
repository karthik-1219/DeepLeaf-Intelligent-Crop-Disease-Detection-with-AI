import streamlit as st

def home_page():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.header("DeepLeaf : Intelligent Crop Disease Detection")
    image_path = "home_page.jpeg"
    st.image(image_path,use_container_width=True)
    st.markdown("""
    ### 🌿 Plant Disease Recognition System
    
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### Project Objective
    The Plant Disease Recognition System aims to assist farmers, researchers, and agricultural professionals by leveraging deep learning to automatically detect diseases in plants through image analysis. Our goal is to empower users with timely and accurate information to prevent crop loss and enhance agricultural productivity.
                
    ### How the System Works ?

    1. **Image Upload** : Users navigate to the **Disease Recognition** module and upload an image of a plant leaf suspected of infection.
    2. **Intelligent Analysis** : Our system processes the image using advanced convolutional neural networks (CNNs) trained on a diverse dataset of plant diseases. It identifies visible symptoms and predicts the disease with high accuracy.
    3. **Result Display** : The detected disease name and recommended actions are promptly displayed, allowing users to make informed decisions for treatment or further action.

    ### Key Features 
    - **High Accuracy** : Utilizes state-of-the-art deep learning models for precise detection of a wide range of plant diseases.
    - **User-Friendly Interface** : Designed with a clean and intuitive interface to ensure ease of use for users with minimal technical expertise.
    - **Rapid Diagnosis** : RImage processing and prediction occur within seconds, ensuring fast turnaround for critical decisions.
    - **Scalable & Modular** : Built to be easily extended with new plant species and diseases as required.

    ### Get Started
    Ready to see it in action?
    Head to the **Disease Recognition** section, upload a leaf image, and experience how AI is transforming agriculture !!!

    ### About the Team
    We are a group of passionate computer science students focused on building intelligent solutions that solve real problems. This project is a culmination of our efforts to blend domain knowledge in agriculture with cutting-edge technology in machine learning.

    To learn more about our goals and journey, visit the **About page** of the application.
    """)
