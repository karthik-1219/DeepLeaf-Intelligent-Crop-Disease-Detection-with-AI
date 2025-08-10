import streamlit as st
import tensorflow as tf
import numpy as np
import os
from openai import OpenAI
from data_dict import get_disease_details
from deep_translator import GoogleTranslator
import pandas as pd
from datetime import datetime
from io import BytesIO
import os
from PIL import Image

from gtts import gTTS
import streamlit as st
import os
import uuid

import base64
import gdown

MODEL_FILE_ID = "1T71U3f3mwh_jQCrgvD445WfsatQ4vr_S"
MODEL_URL = f"https://drive.google.com/uc?id={MODEL_FILE_ID}"
MODEL_PATH = "trained_plant_disease_model.keras"


HISTORY_FILE = "history.csv"
TRAIN_DIR = r"C:\Users\karthik\OneDrive\Desktop\3-1 Project\Deep Leaf Project\train"

def generate_audio(text, lang_code):
    tts = gTTS(text=text, lang=lang_code)
    filename = f"audio_{uuid.uuid4().hex}.mp3"
    tts.save(filename)
    return filename

def play_audio(file_path):
    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

# Load custom CSS
# with open("styles.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# OpenAI client
client = OpenAI(api_key=st.secrets["api_key"])



# ---------------- Helper Functions ----------------
def save_to_history(disease_list, plant_list, symptoms, causes, remedies, accuracy="N/A"):
    """Save detection history to CSV."""
    new_entry = pd.DataFrame([{
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Disease Name": ", ".join(disease_list),
        "Plant": ", ".join(set(plant_list)),
        "Symptoms": symptoms,
        "Causes": causes,
        "Remedies": remedies,
        "Accuracy": accuracy
    }])

    if os.path.exists(HISTORY_FILE):
        existing = pd.read_csv(HISTORY_FILE)
        updated = pd.concat([existing, new_entry], ignore_index=True)
    else:
        updated = new_entry

    updated.to_csv(HISTORY_FILE, index=False)

def get_disease_info(disease_name):
    """Fetch AI disease details, fallback to error message if failed."""
    prompt = f"Explain the plant disease '{disease_name}' in 3-4 lines, including causes and basic remedies."
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a plant pathology expert."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error retrieving info: {e}"

# Load the model only once for speed
def is_valid_model_file(path):
    return os.path.exists(path) and os.path.getsize(path) > 10 * 1024 * 1024  # 10 MB min

@st.cache_resource
def load_model():
    if not is_valid_model_file(MODEL_PATH):
        with st.spinner("Downloading model, please wait..."):
            gdown.download(MODEL_URL, MODEL_PATH, quiet=False, fuzzy=True)
    
    size_mb = os.path.getsize(MODEL_PATH) / (1024*1024)
    st.write(f"Model file size: {size_mb:.2f} MB")

    if not is_valid_model_file(MODEL_PATH):
        st.error("Downloaded model file is invalid or corrupted.")
        return None

    try:
        model = tf.keras.models.load_model(MODEL_PATH)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None
    
    return model



def model_prediction(test_image):
    model = load_model()
    if model is None:
        st.error("Model could not be loaded. Prediction aborted.")
        return None

    if hasattr(test_image, "read"):
        image_data = BytesIO(test_image.read())
    else:
        image_data = test_image

    try:
        image = tf.keras.preprocessing.image.load_img(image_data, target_size=(128, 128))
        input_arr = tf.keras.preprocessing.image.img_to_array(image)
        input_arr = np.expand_dims(input_arr, axis=0)  # batch dimension

        predictions = model.predict(input_arr)[0]
        return predictions
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None


def translate_text(text, lang_code):
    """Translate text to selected language."""
    try:
        return GoogleTranslator(source='auto', target=lang_code).translate(text)
    except:
        return text

# ---------------- Main Function ----------------
def disease_recognition():

    st.header("🌿 Disease Recognition")

    # Choose input method
    option = st.radio("Select Image Source:", ["Upload Image", "Use Camera"])

    test_image = None
    if option == "Upload Image":
        test_image = st.file_uploader("Choose an Image:", type=["jpg", "jpeg", "png"])
    elif option == "Use Camera":
        test_image = st.camera_input("Take a picture")

    # if st.button("Show Image"):
    #     if test_image is None:
    #         st.warning("#### Please Upload or Capture an Image")
    #         st.stop()
    #     if "leaf" not in test_image.name.lower():
    #         st.error("#### Upload leaf image only")
    #         st.stop()
    #     st.image(test_image, use_container_width=True)

    if st.button("Show Image"):
        if test_image is None:
            st.warning("#### Please Upload or Capture an Image")
            st.stop()

        # Check if it's from file uploader
        if option == "Upload Image":
            if "leaf" not in test_image.name.lower():
                st.error("#### Upload leaf image only")
                st.stop()

        # Show the image for both upload and camera
        st.image(test_image, use_column_width=True)

    if st.button("Predict"):
        if test_image is None:
            st.error("Please upload or capture an image first.")
            st.stop()
 

        predictions = model_prediction(test_image)

        class_name = [
            'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
            'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
            'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
            'Corn_(maize)___Commonw_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
            'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
            'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
            'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
            'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
            'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
            'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot',
            'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
            'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
            'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
            'Tomato___healthy'
        ]

        top_indices = np.argsort(predictions)[::-1]
        selected_indices = [i for i in top_indices if predictions[i] >= 0.1][:3]

        detected_diseases = [class_name[i] for i in selected_indices]
        detected_probs = [predictions[i] * 100 for i in selected_indices]

        # Store everything in session state
        st.session_state.detected_diseases = detected_diseases
        st.session_state.class_name = class_name
        st.session_state.details_list = []

        all_plants, all_symptoms, all_causes, all_remedies = [], [], [], []

        for idx, disease in enumerate(detected_diseases):
            details = get_disease_details(disease)
            all_plants.append(details['plant'])
            all_symptoms.append(details['symptoms'])
            all_causes.append(details['causes'])
            all_remedies.append(details['remedies'])

            st.session_state.details_list.append(
                (disease, details['plant'], details['symptoms'], details['causes'], details['remedies'], detected_probs[idx])
            )



        save_to_history(detected_diseases, all_plants,
                        symptoms=" | ".join(all_symptoms),
                        causes=" | ".join(all_causes),
                        remedies=" | ".join(all_remedies),
                        accuracy="N/A")

    # Always show results if available

    TRAIN_DATASET_PATH = r"C:\Users\karthik\OneDrive\Desktop\3-1 Project\Deep Leaf Project\train"

    if "details_list" in st.session_state and st.session_state.details_list:
        for idx, item in enumerate(st.session_state.details_list):
            if len(item) == 6:
                disease, plant, symptoms, causes, remedies, prob = item
            else:
                disease, plant, symptoms, causes, remedies = item
                prob = 0

            st.success(f"Prediction {idx+1}: **{disease}** ({prob:.2f}%)")

            # Show 3 training images related to the disease
            disease_folder = os.path.join(TRAIN_DATASET_PATH, disease)
            if os.path.exists(disease_folder):
                sample_imgs = os.listdir(disease_folder)[:3]  # Pick first 3 images
                cols = st.columns(len(sample_imgs))
                for col, img_file in zip(cols, sample_imgs):
                    img_path = os.path.join(disease_folder, img_file)
                    col.image(Image.open(img_path), caption=f"{disease} example", use_container_width=True)
            else:
                st.info(f"No images found in training dataset for {disease}.")

            # Show disease details
            st.markdown("### 🧠 Disease Info (English)")
            st.write(f"**Plant Affected:** {plant}")
            st.write(f"**Symptoms:** {symptoms}")
            st.write(f"**Causes:** {causes}")
            st.write(f"**Remedies:** {remedies}")

    # if "details_list" in st.session_state and st.session_state.details_list:
    #     for idx, item in enumerate(st.session_state.details_list):
    #         if len(item) == 6:
    #             disease, plant, symptoms, causes, remedies, prob = item
    #         else:  # old data without probability
    #             disease, plant, symptoms, causes, remedies = item
    #             prob = 0

    #         st.success(f"Prediction {idx+1}: **{disease}** ({prob:.2f}%)")
    #         st.markdown("### 🧠 Disease Info (English)")
    #         st.write(f"**Plant Affected:** {plant}")
    #         st.write(f"**Symptoms:** {symptoms}")
    #         st.write(f"**Causes:** {causes}")
    #         st.write(f"**Remedies:** {remedies}")


        # Translation choice appears here
        st.markdown("---")
        translate_choice = st.radio("Do you want to translate?", ["No", "Yes"], key="translate_choice_after_predict")

        if translate_choice == "Yes":
            lang_map = {"Hindi": "hi", "Telugu": "te", "Tamil": "ta"}
            selected_lang = st.radio("Select Language", list(lang_map.keys()), key="lang_choice")
            lang_code = lang_map[selected_lang]

            for disease, plant, symptoms, causes, remedies, _ in st.session_state.details_list:
                st.markdown(f"### 🌐 {disease} ({selected_lang})")

                # Prepare translated sections
                plant_text = f"{translate_text('Plant Affected :', lang_code)} {translate_text(plant, lang_code)}"
                symptoms_text = f"{translate_text('Symptoms :', lang_code)} {translate_text(symptoms, lang_code)}"
                causes_text = f"{translate_text('Causes :', lang_code)} {translate_text(causes, lang_code)}"
                remedies_text = f"{translate_text('Remedies :', lang_code)} {translate_text(remedies, lang_code)}"

                # Display translations
                st.write(f"**{plant_text}**")
                st.write(f"**{symptoms_text}**")
                st.write(f"**{causes_text}**")
                st.write(f"**{remedies_text}**")

                # Audio content
                full_text = f"{plant_text}. {symptoms_text}. {causes_text}. {remedies_text}"
                if st.button(f"🔊 Listen ({disease})", key=f"audio_{disease}"):
                    audio_path = generate_audio(full_text, lang_code)
                    play_audio(audio_path)
                    os.remove(audio_path)

        # Compare section at the end
        if st.button("Compare Healthy vs Diseased"):
            for disease in st.session_state.detected_diseases:
                plant_name = disease.split("___")[0]
                healthy_class = [cls for cls in st.session_state.class_name if "healthy" in cls.lower() and plant_name.lower() in cls.lower()]

                st.markdown(f"## 🔍 Comparison for {disease}")
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Diseased Samples")
                    diseased_dir = os.path.join(TRAIN_DIR, disease)
                    if os.path.exists(diseased_dir):
                        diseased_imgs = os.listdir(diseased_dir)[:3]
                        for img in diseased_imgs:
                            st.image(os.path.join(diseased_dir, img), use_container_width=True)

                with col2:
                    st.subheader("Healthy Samples")
                    if healthy_class:
                        healthy_dir = os.path.join(TRAIN_DIR, healthy_class[0])
                        if os.path.exists(healthy_dir):
                            healthy_imgs = os.listdir(healthy_dir)[:3]
                            for img in healthy_imgs:
                                st.image(os.path.join(healthy_dir, img), use_container_width=True)
