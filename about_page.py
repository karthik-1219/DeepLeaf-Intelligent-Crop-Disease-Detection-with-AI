import streamlit as st

def about_page():
    st.header("About")
    st.markdown("""
                ### About Dataset
                TThe dataset used in this project has been carefully curated through offline augmentation of the original dataset, which is publicly available on GitHub. It contains a comprehensive collection of approximately 87,000 RGB images of crop leaves, encompassing both healthy and diseased conditions.

                These images are categorized into 38 distinct classes, covering a wide range of plant species and disease types. The dataset is structured to support supervised learning tasks and has been split into training and validation sets using an 80:20 ratio, while preserving the original directory hierarchy.
                Additionally, a separate test set comprising 33 images has been created to evaluate prediction performance.


                ### Dataset Structure
                1. **Training Set** : 70,295 images
                2. **Validation Set** : 17,572 images
                3. **Test Set** : 33 Images (used for real-time prediction)

                This dataset serves as the foundation for training and evaluating our plant disease recognition model, enabling robust classification and detection across multiple plant types.
    """)
