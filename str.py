import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

st.title("🔢 Digit Prediction App")
st.write("Upload a digit image (28x28) and the model will predict it.")

# Load MNIST model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("mnist_model.h5")

model = load_model()

# Upload image
uploaded = st.file_uploader("Upload Digit Image", type=["png", "jpg", "jpeg"])

if uploaded:
    img = Image.open(uploaded).convert("L")  # grayscale
    st.image(img, caption="Uploaded Image", width=200)

    # Preprocess
    img = img.resize((28, 28))
    img = np.array(img)
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)

    # Predict
    prediction = model.predict(img)
    digit = np.argmax(prediction)

    st.subheader(f"Predicted Digit: **{digit}**")
    st.bar_chart(prediction[0])
    
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.utils import to_categorical

# Load Data
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Build Model
model = Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train
model.fit(x_train, y_train, epochs=5, validation_split=0.1)

# Save Model
model.save("mnist_model.h5")
print("Model saved successfully!")


  
