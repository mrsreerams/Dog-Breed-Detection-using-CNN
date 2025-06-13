# 🐶 Dog Breed Classifier

A fun and interactive Streamlit web app that allows users to upload an image of a dog, automatically detect its breed using a fine-tuned deep learning model, and interact with playful, pet-care-inspired features!

---

## ✨ Features

- 🧠 **Deep Learning Model**  
  Classifies dog breeds with high accuracy using a trained Keras MobileNetV2 model.

- 🖼 **Image Upload**  
  Supports JPG, JPEG, and PNG formats for easy uploads.

- 📊 **Breed Prediction with Confidence**  
  Displays the most likely breed and the model’s confidence score.

- 🐾 **Interactive Follow-Up**  
  Asks the user a fun question: _"Has your dog eaten today?"_

- 🍗 **Feed Your Dog Button**  
  If the answer is "No", click the "Feed Your Dog" button to simulate feeding. Animations or text updates follow.

- 🎉 **Fun Dog Facts**  
  Displays a random fun fact about dogs after prediction. Keeps things educational and enjoyable!

- 💅 **Custom Styling**  
  Includes hover effects, button styles, animated text, and aesthetic layout with Streamlit components and CSS hacks.

---

## 🧠 Model Info

- **Base Model**: MobileNetV2 (pretrained on ImageNet)
- **Framework**: TensorFlow/Keras
- **Classes**: 9 dog breeds
- **Training**:
  - Image size: 224x224
  - Loss: Categorical Crossentropy
  - Optimizer: Adam

---

## 🛠 Tech Stack

- 🐍 **Python 3.8+**
- 🧠 **TensorFlow / Keras**
- 🌐 **Streamlit**
- 📦 **NumPy, Pillow, random, os**
- 🎨 **Custom CSS styling (Streamlit hacks)**

---

## 📁 Project Structure

dog-breed-classifier/
├── app.py                  # Main Streamlit app
├── dog_breed_model.h5      # Trained deep learning model
├── utils.py                # Image preprocessing & prediction helpers
├── dog_facts.py            # Stores fun dog facts
├── images/                 # Sample images or assets
├── requirements.txt        # Project dependencies
└── README.md               # You're here!
🚀 Run the App Locally
Clone the repository:

git clone https://github.com/mrsreerams/dog-breed-classifier.git
cd dog-breed-classifier
Install dependencies:

pip install -r requirements.txt
Launch the Streamlit app:

streamlit run app.py
Open http://localhost:8501 in your browser.

✅ To Do
Add sound effects when "feeding the dog" 🐕🍽

Enable breed-specific tips (grooming, nutrition, etc.)

Add webcam capture option

Add user input tracking/logs (optional)

🧑‍💻 Author
Venkata Sreeram Pachipulusu
📧 [venkatasreeramlti@gmail.com]
