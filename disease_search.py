import streamlit as st
import os
from data_dict import data_dict

def disease_search():
    st.header("🔍 Search Plant Disease")

    # Choose search type
    search_type = st.radio("Search by:", ["Plant Name", "Disease Name"])

    if search_type == "Plant Name":
        # Get unique plant names from data_dict
        plant_list = sorted(set(details['plant'] for details in data_dict.values()))
        selected_plant = st.selectbox("Select or Search Plant:", plant_list)

        if selected_plant:
            st.subheader(f"🌱 Plant Name : {selected_plant}")

            # Filter all diseases for the selected plant
            diseases_for_plant = [
                (disease_key, details) 
                for disease_key, details in data_dict.items() 
                if details['plant'].lower() == selected_plant.lower()
            ]

            if diseases_for_plant:
                for disease_key, details in diseases_for_plant:
                    st.markdown(f"### 📌 Disease Name : {details['disease_name']}")

                    # Show sample images
                    img_dir = details['sample_image_path']
                    if os.path.exists(img_dir):
                        images = os.listdir(img_dir)[:3]
                        img_cols = st.columns(len(images))
                        for idx, img_file in enumerate(images):
                            img_path = os.path.join(img_dir, img_file)
                            with img_cols[idx]:
                                st.image(img_path, use_container_width=True)
                    else:
                        st.warning("No sample images found for this disease.")

                    # Show info
                    st.write(f"**Plant Affected :** {details['plant']}")
                    st.write(f"**Symptoms :** {details['symptoms']}")
                    st.write(f"**Causes :** {details['causes']}")
                    st.write(f"**Remedies :** {details['remedies']}")
                    st.markdown("---")
            else:
                st.warning("No diseases found for this plant.")

    elif search_type == "Disease Name":
        disease_list = sorted(data_dict.keys())
        selected_disease = st.selectbox("Select or Search Disease:", disease_list)

        if selected_disease:
            details = data_dict[selected_disease]
            st.markdown(f"### 📌 Disease Name : {details['disease_name']}")

            img_dir = details['sample_image_path']
            if os.path.exists(img_dir):
                images = os.listdir(img_dir)[:3]
                img_cols = st.columns(len(images))
                for idx, img_file in enumerate(images):
                    img_path = os.path.join(img_dir, img_file)
                    with img_cols[idx]:
                        st.image(img_path, use_container_width=True)
            else:
                st.warning("No sample images found for this disease.")

            st.write(f"**Plant Affected :** {details['plant']}")
            st.write(f"**Symptoms :** {details['symptoms']}")
            st.write(f"**Causes :** {details['causes']}")
            st.write(f"**Remedies :** {details['remedies']}")
