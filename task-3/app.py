import types, sys
# --- Patch out pyarrow safely so pandas/sklearn don't crash ---
fake_pa = types.SimpleNamespace(__version__="0.0.0")
sys.modules["pyarrow"] = fake_pa
sys.modules["pyarrow.lib"] = fake_pa
sys.modules["pyarrow._feather"] = fake_pa
sys.modules["pyarrow.parquet"] = fake_pa
sys.modules["pyarrow.csv"] = fake_pa


import streamlit as st
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from openai import OpenAI

# ---- Load dataset ----
wine = load_wine()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = wine.target

# ---- Train model ----
model = RandomForestClassifier()
model.fit(X, y)

wine_names = {
    0: "Classical Barolo",
    1: "Richer Grignolino",
    2: "Fruity Barbera"
}

# ---- Streamlit UI ----
st.title("Wine Recommender App")
st.write("Adjust the sliders to describe your preferred wine characteristics, then click **Run** to see your recommended wine type!")

# Choose a few fun features to expose to the user
alcohol = st.slider("Alcohol", float(X.alcohol.min()), float(X.alcohol.max()), float(X.alcohol.mean()))
malic_acid = st.slider("Malic Acid", float(X["malic_acid"].min()), float(X["malic_acid"].max()), float(X["malic_acid"].mean()))
color_intensity = st.slider("Color Intensity", float(X["color_intensity"].min()), float(X["color_intensity"].max()), float(X["color_intensity"].mean()))
hue = st.slider("Hue", float(X["hue"].min()), float(X["hue"].max()), float(X["hue"].mean()))

if st.button("Run"):
    input_data = [[alcohol, malic_acid, color_intensity, hue] + [0]*(X.shape[1]-4)]
    prediction = model.predict(input_data)[0]
    wine_name = wine.target_names[prediction]
    
    st.success(f"Your ideal wine match might be: **{wine_name.capitalize()}** 🍇")

st.title("LLM Wine Assistant")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

prompt = st.text_area("Ask the AI anything about wine 🍷")

if st.button("Ask"):
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-4-turbo"
            messages=[{"role": "user", "content": prompt}]
        )
        st.markdown("### Response:")
        st.write(response.choices[0].message.content)


st.write("Wine tastes like a mix of fruit, acid, tannin, alcohol, and sweetness — and every type balances those differently.")