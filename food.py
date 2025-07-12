import pickle
import numpy as np
import os
import warnings
from config import (MODEL_FILE_PATH, CLASS_NAME_FILE_PATH)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
warnings.filterwarnings("ignore")

import tensorflow as tf # type: ignore

class PredictFood:

    interpreter = tf.lite.Interpreter(model_path=MODEL_FILE_PATH)
    with open(CLASS_NAME_FILE_PATH, "rb") as f:
            class_names = pickle.load(f)

    def __init__(self) -> None:
        self.classify_lite = self.interpreter.get_signature_runner('serving_default')
        self.img_height = 224
        self.img_width = 224
    
    def convert_image_to_array(self, img: str) -> tf.Tensor:
        """
        Generate an array of an image
            
        Args:
            img (str): Path of the image
            
        Returns:
            tf.Tensor: The image as a 4D tensor (1, height, width, channels)
        """
        img = tf.keras.utils.load_img(img, target_size=(self.img_height, self.img_width))
        image_array = tf.keras.utils.img_to_array(img)
        image_array = tf.expand_dims(image_array, 0)

        return image_array
    
    def predict(self, image_array: tf.Tensor) -> tuple[str, float]:
        """
        Predict the food item from the given image tensor. 

        Args:
            image_array (tf.Tensor): A 4D image tensor (1, height, width, channels)

        Returns:
            tupe[str, float]: A tuple containing:
                -Predicted food name as string
                -Confidence score as a float (percentage)
        """
        predictions = self.classify_lite(keras_tensor_990=image_array)['output_0']
        score = tf.nn.softmax(predictions)

        return self.class_names[np.argmax(score)], 100 * np.max(score)


def find_food(img: str) -> str:
    pf = PredictFood()
    img_array = pf.convert_image_to_array(img)
    img_name, score = pf.predict(img_array)

    return img_name