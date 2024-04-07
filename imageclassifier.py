import streamlit as st
from identify import identify

def imageclassifier():
    st.title("Image Classifier for Numbers")

    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        identified = identify(uploaded_file)

        if identified is not None:
            st.info("Image Identified as " + str(identify(uploaded_file)))
        else:
            st.info("Image not Identified as a Number")
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)