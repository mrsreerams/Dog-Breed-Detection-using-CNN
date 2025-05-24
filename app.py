import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load the fine-tuned model
model = tf.keras.models.load_model("best_model.h5")

# Define class names (adjust as per your dataset order)
class_names = ['Doberman', 'French Bulldog', 'German Sheperd', 'Golden Retriever', 'Labrador',
               'Pitbull', 'Pomeranian', 'Pug', 'Siberian Husky']

# Breed-specific food suggestions
food_suggestions = {
    'Doberman': "Purina Pro Plan Sport",
    'French Bulldog': "Royal Canin French Bulldog",
    'German Sheperd': "Hill's Science Diet Large Breed",
    'Golden Retriever': "Blue Buffalo Life Protection Formula",
    'Labrador': "Royal Canin Labrador Retriever",
    'Pitbull': "Taste of the Wild High Prairie",
    'Pomeranian': "Wellness Complete Health Small Breed",
    'Pug': "Wellness CORE Small Breed",
    'Siberian Husky': "Taste of the Wild High Prairie"
}

# Fun facts
dog_facts = [
    "Dogs' noses are as unique as human fingerprints!",
    "The Basenji is the only barkless dog.",
    "A dog’s sense of smell is 40x better than a human’s.",
    "Dogs can learn over 1000 words and gestures.",
    "Dalmatians are born completely white and develop spots as they age."
]

# Custom styles
st.markdown("""
    <style>
        .main-title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #2C3E50;
            text-align: center;
        }
        .sub-text {
            text-align: center;
            font-size: 1.1rem;
            color: #34495E;
        }
        .result-box {
            background-color: #ecf0f1;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            color: #2C3E50;
            margin-top: 20px;
        }
        .highlight-question {
            font-size: 1.2rem;
            font-weight: bold;
            color: #e74c3c;
        }
    </style>
""", unsafe_allow_html=True)

# Title and instructions
st.markdown("<div class='main-title'>Dog Breed Classifier</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-text'>Upload an image of a dog and click Predict to identify its breed.</div>", unsafe_allow_html=True)

# Upload image
uploaded_file = st.file_uploader("Upload Dog Image", type=["jpg", "jpeg", "png"])

# Predict button logic
if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        # Preprocess
        img_resized = img.resize((224, 224))
        img_array = image.img_to_array(img_resized) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        prediction = model.predict(img_array)
        predicted_class = class_names[np.argmax(prediction)]
        confidence = np.max(prediction) * 100

        st.markdown(f"<div class='result-box'>Predicted Breed: {predicted_class}<br>Confidence: {confidence:.2f}%</div>", unsafe_allow_html=True)

        # Ask user if the dog has eaten
        st.markdown("<div class='highlight-question'>Has your dog eaten today?</div>", unsafe_allow_html=True)
        food_status = st.radio("", ("Yes", "No"), horizontal=True)

        if food_status == "Yes":
            st.success("🐶 Great! Your dog is happy and healthy. Keep up the good care!")
        elif food_status == "No":
            suggestion = food_suggestions.get(predicted_class, "Try high-quality dog food suited for your breed.")
            st.warning(f"🍽 Don't forget to feed your dog! Try this: {suggestion}")

        # Show a fun fact
        st.markdown("<hr><h4>🐾 Dog Fact</h4>", unsafe_allow_html=True)
        st.info(np.random.choice(dog_facts))

else:
    st.info("Please upload an image to get started.")
