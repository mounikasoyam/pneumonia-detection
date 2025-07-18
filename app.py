import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Page settings
st.set_page_config(page_title="Pneumonia Detection", page_icon="🩺", layout="centered")

# Custom CSS for background and styling
st.markdown("""
    <style>
    body {
        background-color: #eef5ff;
    }
    .reportview-container {
        background: #eef5ff;
        padding: 2rem;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
    }
    .title {
        background-color: #4B9CD3;
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        color: #888;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# Layout container
with st.container():
    st.markdown('<div class="title">🩺 Pneumonia Detection from Chest X-Ray</div>', unsafe_allow_html=True)
    st.write("Upload a chest X-ray image (JPG or PNG), and the model will predict whether it shows Pneumonia or Normal lungs.")

# Load trained model
model = load_model("model.h5")

# Upload image
uploaded_file = st.file_uploader("📤 Upload Chest X-ray Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="🖼️ Uploaded Image", use_column_width=True)

    # Preprocess image
    img = img.resize((150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Make prediction
    prediction = model.predict(img_array)[0][0]
    label = "Pneumonia" if prediction > 0.5 else "Normal"
    confidence = prediction if prediction > 0.5 else 1 - prediction

    # Display result
    st.success(f"✅ Prediction: **{label}**")
    st.info(f"📊 Confidence Score: `{confidence:.2f}`")

# Footer
st.markdown('<div class="footer">✨ "Combining Medicine with Machine Intelligence — Because every pixel matters in saving a life."</div>', unsafe_allow_html=True)
