import os

BASE_DIR = os.path.dirname(__file__)

# model path
MODEL_FILE_PATH = os.path.join(BASE_DIR, "model", "model12(32).tflite")
CLASS_NAME_FILE_PATH = os.path.join(BASE_DIR, "model", "class_name.pkl")

# database path
DB_PATH = os.path.join(BASE_DIR, "database", "nutrition.db")