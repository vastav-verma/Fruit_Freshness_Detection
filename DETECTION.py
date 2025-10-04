import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Fruit Freshness Detector", page_icon="🍎", layout="wide")

# Load external CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")  # Assumes style.css is in the root directory

# Load model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("models/fruit_classifier_model.h5")

model = load_model()

# Constants
IMAGE_SIZE = (150, 150)
OUTPUT_FILE = "prediction_results.csv"

# ---------------------------
# Title Section
# ---------------------------
st.markdown("<h1 class='title-text'>🍎 Fruit Freshness Detector</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>Upload fruit images to check if they are <b>Fresh</b> or <b>Rotten</b>!</p>", unsafe_allow_html=True)

# Add a subtle horizontal separator
st.markdown("<hr class='soft-line'>", unsafe_allow_html=True)

# ---------------------------
# Prediction Logic
# ---------------------------
uploaded_files = st.file_uploader(
    label="📸 Upload Fruit Images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

results_list = []

if uploaded_files:
    st.info(f"Total images uploaded: {len(uploaded_files)}")

    cols = st.columns(3)  # show results in grid
    for idx, uploaded_file in enumerate(uploaded_files):
        with cols[idx % 3]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)

            image = Image.open(uploaded_file).convert("RGB")
            display_image = image.resize((200, 200))
            st.image(display_image, caption=f"{uploaded_file.name}", use_container_width=True)

            # Preprocess
            img = image.resize(IMAGE_SIZE)
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            # Prediction
            prediction = model.predict(img_array)[0][0]
            is_fresh = prediction < 0.5
            label = "Fresh 🍏" if is_fresh else "Rotten 🍂"
            confidence = (1 - prediction) if is_fresh else prediction

            st.markdown(
                f"<h3 class='{ 'fresh' if is_fresh else 'rotten' }'>{label}</h3>",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<p style='font-size:15px;'>Confidence: <b>{confidence * 100:.2f}%</b></p>",
                unsafe_allow_html=True
            )
            st.progress(float(confidence))

            st.markdown("</div>", unsafe_allow_html=True)

            results_list.append({
                "Image Name": uploaded_file.name,
                "Prediction": label,
                "Confidence (%)": round(float(confidence * 100), 2)
            })

    # Save and display CSV
    if results_list:
        df = pd.DataFrame(results_list)
        df.to_csv(OUTPUT_FILE, index=False)
        st.success(f"✅ Results saved to **{OUTPUT_FILE}** in project folder!")

        st.dataframe(df)

        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Results as CSV",
            data=csv_data,
            file_name="prediction_results.csv",
            mime="text/csv"
        )
else:
    st.markdown("<p class='upload-note'>👆 Please upload one or more fruit images to begin.</p>", unsafe_allow_html=True)
