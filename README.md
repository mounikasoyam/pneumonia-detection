
# 🩺 Pneumonia Detection using Deep Learning

A Deep Learning-based web application that detects **Pneumonia** from chest X-ray images using a trained **CNN model**, built with **TensorFlow** and deployed using **Streamlit**.

---

## 🌟 Features

- 📷 Upload chest X-ray images.
- 🧠 Trained Convolutional Neural Network (CNN) model.
- 🖥️ Interactive and user-friendly Streamlit interface.
- ✅ Provides quick and reliable Pneumonia prediction results.

---

## 📂 Project Structure
📁 Pneumonia_Project/
├── 📁 app/ # Streamlit frontend app
│ └── app.py
├── 📁 pneumonia_detection_dataset/ # Dataset folder
│ └── chest_xray.zip (large file - not pushed to GitHub)
├── 📄 model.h5 # Trained model file (not pushed to git)
├── 📄 requirements.txt # Python dependencies
├── 📄 Pneumonia_Algorithm_Presentation.pptx
├── 📄 Pneumonia_Detection_Result_Document.docx
└── 📄 README.md


---

## 🚀 Deployment

To run the Streamlit app locally:

```bash
pip install -r requirements.txt
streamlit run app/app.py

Dataset
The model was trained on the Chest X-ray dataset from Kaggle.
Note: Due to GitHub's file size limit, the dataset is not included in the repository.

📥 You can download it from this link and extract it into the project folder:
drive link:https://drive.google.com/file/d/16RM_AofKg2PGMC0Hl4x5HcZQQFi6RA_T/view?usp=drive_link

Model Info
CNN architecture built with TensorFlow/Keras.

Achieved high accuracy on validation/test data.

Optimized with image preprocessing and data augmentation.

⚠️ The model.h5 file (~55MB) is also excluded from GitHub.
drive link:https://drive.google.com/file/d/1NsV7FzFu9fjtOAaU9nq7da67kxCEDtaB/view?usp=drive_link





