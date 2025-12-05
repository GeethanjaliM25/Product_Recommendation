import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

st.title("🛍️ Amazon Beauty Product Recommendation System")

# Load trained files
with open("svd_model.pkl", "rb") as f:
    svd = pickle.load(f)

with open("similarity_df.pkl", "rb") as f:
    similarity_df = pickle.load(f)

with open("ratings_matrix.pkl", "rb") as f:
    ratings_matrix = pickle.load(f)

st.write("Dataset used:", ratings_matrix.shape)

# Dropdown
selected_product = st.selectbox("Select a Product ID", ratings_matrix.index)

def recommend_products(product_id, n=5):
    scores = similarity_df[product_id].sort_values(ascending=False)
    return scores.iloc[1:n+1].index

if st.button("Recommend"):
    recommendations = recommend_products(selected_product)
    st.subheader("Recommended Products:")
    for product in recommendations:
        st.write(product)
