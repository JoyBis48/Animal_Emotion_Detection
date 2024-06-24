# Animal Emotion Detector

This project aims to detect emotions in animals using a trained Convolutional Neural Network model. It leverages the use of MobileNetV2 CNN architecture pretrained on ImageNet which was then finetuned for emotion detection, and provides a simple GUI for users to upload images of animals and view the predicted emotions.
The model currently predicts only three type of emotions with significant confidence, namely Angry, Happy and Sad. The dataset for the training consisted of a variety of different animals, with a special focus on cats and dogs.

## Features

- **Emotion Detection**: Utilizes a pre-trained CNN model followed by finetuning to predict emotions in animals from uploaded images.
- **Graphical User Interface**: A user-friendly GUI built with Tkinter for easy interaction with the application.
- **Image Preprocessing**: Images are preprocessed to meet the input requirements of the MobileNetV2 model.

## Installation

To run this code, you need to have Python installed on your system. The project has been tested on Python 3.8. Follow these steps to set up the project:

1. **Clone the repository**: git clone <https://github.com/JoyBis48/Animal_Emotion_Detection.git>
2. **Navigate to the project directory**
3. **Install the required dependencies**: pip install -r requirements.txt
4. **To start the application, run the `Animal_Emotion.py` script from the terminal**

This will launch the GUI where you can upload images of animal faces to detect their emotions.

## How It Works

- **Model Training**: The application uses a model trained with TensorFlow and MobileNetV2 on a dataset of animal images labeled with emotions. The training process, covered in the `Animal_Emotion_Detection.ipynb` notebook, involves using the MobileNetV2 architecture and fine-tuning it for emotion detection.
- **Image Preprocessing**: Uploaded images are resized and preprocessed to match the input format expected by the MobileNetV2 model. This is achieved through the `preprocess_image` function, which resizes the image to 128x128 pixels, applies the necessary preprocessing steps for MobileNetV2, and adds a batch dimension.
- **Emotion Prediction**: The preprocessed image is fed into the trained model, which predicts the emotion displayed by the animal. The model outputs a prediction corresponding to the emotions it has been trained on.
- **GUI Interaction**: Users interact with the application through a GUI built with Tkinter, uploading images and viewing the predicted emotions. The GUI allows users to upload an image through the `upload_image` function, which then displays the image and predicts the emotion.

## Dependencies

- TensorFlow
- Tkinter
- PIL 
- Numpy

