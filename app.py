import os
import pickle
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Amazon Beauty Product Recommendation", layout="wide")

# ---------- Helper to find correct file path ----------
def get_file_path(filename):
    # Check in current (root) folder
    if os.path.exists(filename):
        return filename
    
    # Check in Product_Recommendation folder
    folder_path = os.path.join("Product_Recommendation", filename)
    if os.path.exists(folder_path):
        return folder_path
    
    # If not found, return original (Streamlit will show error)
    return filename


# ---------- Load model files ----------
try:
    with open(get_file_path("svd_model.pkl"), "rb") as f:
        svd_model = pickle.load(f)

    with open(get_file_path("similarity_df.pkl"), "rb") as f:
        similarity_df = pickle.load(f)

    with open(get_file_path("ratings_matrix.pkl"), "rb") as f:
        ratings_matrix = pickle.load(f)

except Exception as e:
    st.error("❌ Model files not found! Please check your .pkl file location in GitHub.")
    st.stop()


# ---------- Title ----------
st.title("🛍️ Amazon Beauty Product Recommendation System")

st.markdown(
    f"""
    **Dataset matrix shape:** {ratings_matrix.shape}  
    Select a Product ID and get top recommended similar products.
    """
)

# ---------- Product selection ----------
product_ids = ratings_matrix.index.tolist()
selected_product = st.selectbox("Select a Product ID", product_ids)


# ---------- Recommendation Function ----------
def recommend_products(product_id, similarity_df, top_n=5):
    if product_id not in similarity_df.index:
        return ["Product not found in similarity matrix"]

    similarity_scores = similarity_df[product_id].sort_values(ascending=False)
    similar_products = similarity_scores.iloc[1: top_n+1].index.tolist()
    return similar_products


# ---------- Show recommendations ----------
if st.button("Get Recommendations"):
    recommendations = recommend_products(selected_product, similarity_df)

    st.subheader("✅ Recommended Products:")
    for product in recommendations:
        st.write(product)
