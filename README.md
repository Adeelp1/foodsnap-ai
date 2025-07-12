# 🍱 Food Classification & Nutrition Prediction
A deep learning model that classifies food from images using EfficientNetB0 and returns nutritional facts using a SQLite3 database.

## 🚀 Features
- Image classification with **EfficientNetB0** pretrained on **ImageNet**

- **Transfer learning with fine-tuning** for improved accuracy

- Nutrition info retrieval from a **SQLite3 database**

- Exported model in both **`.keras`** and **`.tflite`** formats

## 🖼️ Dataset
- 12 custom food categories

- 1200+ images

## 🧠 Model Architecture
- Base model: EfficientNetB0 (ImageNet weights)

- Layers: Base model, GlobalAveragePooling, Dense, Softmax

- Loss: sparse_categorical_crossentropy

- Optimizer: Adam

## 🧪 Results
- Training Accuracy: ~97%

- Validation Accuracy: ~98%

## 💾 Model Export

- `.tflite`

## 🛠️ Tools & Frameworks
- `Python` | `TensorFlow` | `Keras` | `EfficientNet` | `SQLite3` | `Google Colab` | `NumPy`

## 📦 Nutrition Database (Example)
| Food   | Calories | Protein | Fat  |
| ------ | -------- | ------- | ---- |
| Apple  | 52       | 0.3g    | 0.2g |
| Samosa | 262      | 4g      | 17g  |
| Banana | 96       | 1.3g    | 0.3g |

## Set Up and Run Locally

Clone repository
```bash
git clone https://github.com/Adeelp1/foodsnap-ai.git
cd foodsnap-ai
```
Checkout branch
```bash
git checkout feature/adeelp1
```

Install dependencies:
```bash
pip install -r requirements.txt
```
Make sure you have all dependencies installed, then run the program using:
```bash
python main.py
```

## 📌 Future Improvements
- Add more food categories

- Integrate speech/text query input

- Deploy on mobile/web app

