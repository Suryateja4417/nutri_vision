import streamlit as st
import tensorflow as tf
import json
import numpy as np
from PIL import Image
from pathlib import Path
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "fruit_veg_mobilenetv2.keras"
CLASS_PATH = BASE_DIR / "class_names.json"
USDA_PATH = BASE_DIR / "FoodData_Central_foundation_food_json_2025-12-18.json"

st.set_page_config(page_title="Food Nutrition AI", layout="centered")


# Load CNN Model


def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()


# Load Class Names

with open(CLASS_PATH, "r", encoding="utf-8") as f:
    idx_to_class = json.load(f)


# Load USDA JSON
@st.cache_data
def load_usda():
    with open(USDA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["FoundationFoods"]

foods = load_usda()


# Build Nutrition Database

def extract(food):
    nutrients = {}
    for item in food.get("foodNutrients", []):
        name = item["nutrient"]["name"]
        nutrients[name] = {
            "value": item.get("amount", 0),
            "unit": item["nutrient"].get("unitName", "")
        }

    return {
        "name": food["description"].lower(),
        "nutrients": nutrients
    }

nutrition_db = [extract(f) for f in foods]


# Food matcher

def find_food(label):
    label = label.lower()
    for food in nutrition_db:
        if label in food["name"]:
            return food
    return None


# UI

st.title("🥗Nutri-Vision")

uploaded_file = st.file_uploader("Upload an image of a fruit or vegetable", type=["jpg","png","jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)

    img = img.resize((224,224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    class_idx = np.argmax(preds)
    confidence = float(np.max(preds))

    food_label = idx_to_class[str(class_idx)]

    st.success(f"Prediction: {food_label}")
    st.write(f"Confidence: {confidence*100:.2f}%")

    
    # Nutrition lookup
    
    food_data = find_food(food_label)

    if food_data:
        st.subheader("Nutrition per 100g (USDA)")
        nutrients = food_data["nutrients"]

        important_nutrients = [
            "Energy",
            "Protein",
            "Total lipid (fat)",
            "Carbohydrate, by difference",
            "Fiber, total dietary",
            "Sugars, total",
            "Vitamin C, total ascorbic acid",
            "Vitamin A, RAE",
            "Potassium, K",
            "Iron, Fe"
    ]


        cols = st.columns(3)
        
        for i, key in enumerate(important_nutrients):
            if key in nutrients:
                v = nutrients[key]
                value = v.get("value", 0)

                if value in (None, "N/A", ""):
                    value = 0

                unit = v.get("unit", "")
                if key == "Energy" and unit == "kJ":
                    value = round(value / 4.184, 2)
                    unit = "kcal"

                cols[i % 3].metric(
                    label=key,
                    value=f"{value} {unit}"
             )

    else:
        st.warning("No nutrition data found for this food.")
    st.caption(
    "Nutrition values are approximate and sourced from USDA(JSON Dataset). "
                      "They may vary.")
    







