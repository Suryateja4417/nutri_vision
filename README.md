# 🥗 Nutri-Vision: Food Nutrition AI

## 📌 Overview

Nutri-Vision is an AI-powered web application that predicts fruits and vegetables from images and provides their nutritional values.

The system uses a deep learning model (MobileNetV2) for image classification and integrates USDA food data to display real-time nutrition information.

---

## 🚀 Features

* Image-based food recognition (fruits & vegetables)
* Deep Learning model (MobileNetV2)
* Nutrition data lookup (USDA dataset)
* Clean Streamlit UI
* Real-time prediction with confidence score

---

## 🧠 Tech Stack

* Python
* TensorFlow / Keras
* Streamlit
* NumPy
* PIL
* USDA FoodData Central JSON

---

## 📂 Project Structure

```
├── Main1_app.py              # Streamlit application
├── fruit_veg_mobilenetv2.keras  # Trained CNN model
├── FoodData_Central_foundation_food_json_2025-12-18.json  # Nutrition dataset
├── season5.ipynb            # Model training notebook
└── README.md
```

---

## ⚙️ How It Works

1. User uploads an image of a fruit or vegetable
2. Image is preprocessed and passed to the CNN model
3. Model predicts the food label
4. The system matches the label with USDA dataset
5. Nutrition details are displayed per 100g

---

## 📊 Sample Output

* Predicted Label
* Confidence Score
* Nutrition Info:

  * Energy
  * Protein
  * Fat
  * Carbohydrates
  * Fiber
  * Vitamins & Minerals

---

## ▶️ Run Locally

### Step 1: Clone Repository

```
git clone https://github.com/your-username/nutri-vision.git
cd nutri-vision
```

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

### Step 3: Run Application

```
streamlit run Main1_app.py
```

---

## 📦 Dataset

Nutrition data sourced from USDA FoodData Central
File: 

---

## ⚠️ Limitations

* Works only on trained classes (fruits & vegetables)
* Nutrition mapping depends on label matching (not exact)
* Accuracy varies based on image quality

---

## Output

<img width="1280" height="720" alt="Screenshot 2026-04-19 193342" src="https://github.com/user-attachments/assets/562e720e-4815-45bb-98ab-934bd1a64678" />

<img width="1280" height="720" alt="Screenshot 2026-04-19 193352" src="https://github.com/user-attachments/assets/52a4ee78-9e5f-47d3-9beb-4db80d09cd1e" />

check nv_output.pdf

---

## 🔮 Future Improvements

* Add more food categories
* Improve matching algorithm (fuzzy search)
* Deploy on cloud (Streamlit Cloud)
* Add calorie estimation for mixed meals



