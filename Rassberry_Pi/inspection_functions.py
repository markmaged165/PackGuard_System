import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

MODEL_PATH = '/home/mark_pi/project/ai/final_product_model.h5'
IMG_SIZE = (150, 150)

# ... inside inspection_functions.py ...

try:
    # ADD compile=False HERE
    AI_MODEL = load_model(MODEL_PATH, compile=False) 
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    

def inspect_product(image):
    try:
        # Preprocess the image
        img = cv2.resize(image, IMG_SIZE)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        
        # Get the score
        prediction = AI_MODEL.predict(img, verbose=0)[0][0]
        
        print(f"DEBUG: AI Confidence Score is: {prediction:.4f}")
        
        # --- YOUR REQUESTED LOGIC ---
        # This checks if the number is bigger than 3.75 AND smaller than 0.1
        if .04 < prediction < 0.1:
            return True  # Good
        else:
            return False # Defect

    except Exception as e:
        print(f"Inspection Error: {e}")
        return False