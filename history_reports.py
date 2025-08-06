import streamlit as st
import pandas as pd
import os
from fpdf import FPDF
from data_dict import data_dict  # for sample_image_path

HISTORY_FILE = "history.csv"

def generate_pdf(disease_names, plant, symptoms, causes, remedies, date, accuracy, image_dirs):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Plant Disease Diagnosis Report", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Date: {date}", ln=True)
    pdf.cell(200, 10, txt=f"Disease(s): {', '.join(disease_names)}", ln=True)
    pdf.cell(200, 10, txt=f"Plant: {plant}", ln=True)
    pdf.cell(200, 10, txt=f"Accuracy: {accuracy}%", ln=True)

    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Symptoms: {symptoms}")
    pdf.multi_cell(0, 10, f"Causes: {causes}")
    pdf.multi_cell(0, 10, f"Remedies: {remedies}")

    # Add sample images for each disease
    pdf.ln(5)
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Sample Images:", ln=True)

    for img_dir in image_dirs:
        if os.path.exists(img_dir):
            images = os.listdir(img_dir)[:3]  # First 3 images only
            for img in images:
                img_path = os.path.join(img_dir, img)
                try:
                    pdf.image(img_path, w=60)
                except:
                    pass

    file_name = f"{'_'.join(disease_names)}_{date.replace(':', '-')}.pdf"
    pdf.output(file_name)
    return file_name

def history_reports():
    st.header("📜 Upload History & Reports")

    if not os.path.exists(HISTORY_FILE):
        st.info("No history found yet.")
        return

    df = pd.read_csv(HISTORY_FILE)

    if df.empty:
        st.info("No history found yet.")
        return

    st.dataframe(df)

    selected_index = st.selectbox("Select a record to download PDF:", df.index)

    if selected_index is not None:
        row = df.iloc[selected_index]

        # Support multiple diseases separated by commas in history
        disease_names = [d.strip() for d in row["Disease Name"].split(",")]

        image_dirs = []
        for disease in disease_names:
            for key, val in data_dict.items():
                if val["disease_name"] == disease:
                    image_dirs.append(val["sample_image_path"])
                    break

        file_path = generate_pdf(
            disease_names,
            row["Plant"],
            row["Symptoms"],
            row["Causes"],
            row["Remedies"],
            row["Date"],
            row["Accuracy"],
            image_dirs
        )

        with open(file_path, "rb") as f:
            st.download_button(
                label="📄 Download PDF Report",
                data=f,
                file_name=file_path,
                mime="application/pdf"
            )
