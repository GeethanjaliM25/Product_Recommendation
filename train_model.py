# train_model.py
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load dataset
amazon_ratings = pd.read_csv("ratings_Beauty.csv")

# Reduce dataset size (for performance)
popular_products = amazon_ratings['ProductId'].value_counts().head(500).index
amazon_ratings = amazon_ratings[amazon_ratings['ProductId'].isin(popular_products)]

active_users = amazon_ratings['UserId'].value_counts().head(500).index
amazon_ratings = amazon_ratings[amazon_ratings['UserId'].isin(active_users)]

print("Dataset used:", amazon_ratings.shape)

# Create pivot table
ratings_matrix = amazon_ratings.pivot_table(
    values='Rating',
    index='ProductId',
    columns='UserId'
).fillna(0)

# Train SVD
svd = TruncatedSVD(n_components=15, random_state=42)
matrix = svd.fit_transform(ratings_matrix)

# Compute similarity
similarity = cosine_similarity(matrix)
similarity_df = pd.DataFrame(similarity,
                             index=ratings_matrix.index,
                             columns=ratings_matrix.index)

# Save trained model and similarity matrix
with open("svd_model.pkl", "wb") as f:
    pickle.dump(svd, f)

with open("similarity_df.pkl", "wb") as f:
    pickle.dump(similarity_df, f)

with open("ratings_matrix.pkl", "wb") as f:
    pickle.dump(ratings_matrix, f)

print("Training completed and model saved!")
