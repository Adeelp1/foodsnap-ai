import pickle
import numpy as np
import os
import warnings

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
warnings.filterwarnings("ignore")

import tensorflow as tf # type: ignore

BASE_DIR = os.path.dirname(__file__)
MODEL_FILE_PATH = os.path.join(BASE_DIR, "model", "model12(32).tflite")
CLASS_NAME_FILE_PATH = os.path.join(BASE_DIR, "model", "class_name.pkl")

class PredictFood:
    def __init__(self):
        self.interpreter = tf.lite.Interpreter(model_path=MODEL_FILE_PATH)
        self.classify_lite = self.interpreter.get_signature_runner('serving_default')
        self.img_height = 224
        self.img_width = 224
        with open(CLASS_NAME_FILE_PATH, "rb") as f:
            self.class_names = pickle.load(f)
    
    def convert_image_to_array(self, img):
        img = tf.keras.utils.load_img(img, target_size=(self.img_height, self.img_width))
        self.image_array = tf.keras.utils.img_to_array(img)
        self.image_array = tf.expand_dims(self.image_array, 0)
    
    def predict(self):
        predictions = self.classify_lite(keras_tensor_990=self.image_array)['output_0']
        score = tf.nn.softmax(predictions)

        return self.class_names[np.argmax(score)], 100 * np.max(score)


def find_food(img):
    pf = PredictFood()
    pf.convert_image_to_array(img)
    img_name, score = pf.predict()

    return img_name