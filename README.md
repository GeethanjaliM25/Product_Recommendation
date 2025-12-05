{"id":"53841","variant":"standard","title":"Amazon Beauty Product Recommendation System - README"}
# 🛍️ Amazon Beauty Product Recommendation System

This project is a **machine learning–based recommendation system** that suggests similar Amazon beauty products using collaborative filtering, Truncated SVD, and Cosine Similarity.  
It helps users discover related products based on product similarity and past ratings.

---

## 🔗 Live Streamlit App

👉 **Click here to try the app live:**  
https://appuctrecommendation-bcqjyyyhxjdbvau4dhdecv.streamlit.app/

---

## 📊 Dataset Information

- **Dataset Name (Kaggle):** Amazon Beauty Products Ratings
- **Data Size Used:** 447 × 500 (User-Product Matrix)
- **Source:** Kaggle – Amazon Product Reviews Dataset (Beauty category)
- **File used internally:** `ratings_Beauty.csv` (converted to matrix & trained)

The dataset contains:
- Product IDs (ASIN)
- User IDs
- Ratings (1–5 stars)

---

## 🔍 How the system works

1. The dataset is cleaned and converted into a **User–Product ratings matrix**
2. **Truncated SVD (Singular Value Decomposition)** is applied to reduce dimensions
3. **Cosine Similarity** finds the most similar products
4. When a user selects a product, the system displays **Top 5 recommended products**

✅ The model is already **trained in VS Code**  
✅ Saved as pickle files (`svd_model.pkl`, `similarity_df.pkl`, `ratings_matrix.pkl`)  
✅ Used directly in the Streamlit app  

---

## 💻 Technologies Used

- Python
- Pandas & NumPy
- Scikit-learn (Truncated SVD, Cosine Similarity)
- Streamlit
- VS Code
- GitHub

---

## 📂 Files in This Repository

- `app.py` → Streamlit application
- `train_model.py` → Model training file
- `svd_model.pkl` → Trained SVD model
- `similarity_df.pkl` → Product similarity matrix
- `ratings_matrix.pkl` → User-Product matrix
- `requirements.txt` → Required libraries

---

## ✅ Project Status

- ✔ Dataset cleaned and processed  
- ✔ Model successfully trained  
- ✔ Streamlit app successfully deployed  
- ✔ Recommendations working correctly  

**Status:** 🟢 Completed and Working

---

## 🚀 Future Improvements

- Add content-based filtering
- Add product images and names
- Improve UI with filters and categories
- Add user login system

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use, modify, and share.

```
MIT License

Copyright (c) 2025 Geethanjali M

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🙋‍♀️ Author

**Geethanjali M**  
B.E Student | Machine Learning Enthusiast  
GitHub: https://github.com/GeethanjaliM25

