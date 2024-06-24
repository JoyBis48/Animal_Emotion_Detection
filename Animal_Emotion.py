# type: ignore

# Importing the libraries
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import warnings
import tkinter as tk
from tkinter import Label, Button, filedialog
from PIL import Image, ImageTk
import numpy as np

warnings.filterwarnings("ignore")

# Loading the model 
base_dir = os.getcwd()
model_path_dir = os.path.join(base_dir, 'saved_model')

loaded_model = load_model(model_path_dir)

# Printing the model summary
loaded_model.summary()

# Defining emotions list as per the trained model
emotions_list = ['Angry', 'Sad', 'happy']

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((128, 128), Image.Resampling.BICUBIC)
    img_array = np.array(img)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    return np.expand_dims(img_array, axis=0) #adding a batch dimension

# Function to upload image
def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(( (window.winfo_width()/2.25) , (window.winfo_height()/2.25) ))
        im = ImageTk.PhotoImage(uploaded)
        uploaded_image_label.configure(image=im)
        uploaded_image_label.image = im
        emotion_label.config(text='')
        detect_button.config(state="normal", command=lambda: detect_emotion(file_path))
    except Exception as e:
        print(e)

# Function to detect emotion
def detect_emotion(file_path):
    try:
        # Preprocessing the image
        processed_image = preprocess_image(file_path)
        # Predicting emotion
        pred = emotions_list[np.argmax(loaded_model.predict(processed_image))]
        # Updating label with predicted emotion
        emotion_label.config(text="The Predicted Emotion is --> " + pred)
    except:
        # If unable to detect, update label accordingly
        emotion_label.config(text="Unable to detect emotion")

# GUI Layout
# Initialize Tkinter
window = tk.Tk()
window.geometry('800x600')
window.title('Emotion Detector')
window.configure(background='LightGray')

heading_label = Label(window, text='Animal Emotion Detector', pady=20, font=('Arial', 25, 'bold'), bg='LightGray', fg='DarkSlateBlue')
heading_label.pack()

uploaded_image_label = Label(window)
uploaded_image_label.pack(expand=True)

detect_button = Button(window, text="Detect Emotion", padx=10, pady=5, bg="DarkSlateBlue", fg='white', font=('Arial', 12, 'bold'), state="disabled")
detect_button.pack(pady=10)

emotion_label = Label(window, font=('Calibri', 14), bg='LightGray')
emotion_label.pack()

upload_button = Button(window, text="Upload Image", command=upload_image, padx=10, pady=5, bg="DarkSlateBlue", fg='white', font=('Arial', 14, 'bold'))
upload_button.pack(side='bottom', pady=50)

window.mainloop()