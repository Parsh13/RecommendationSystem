# 🎬 Movie Recommendation System using Content-Based Filtering

A streamlined and intuitive **Streamlit web application** that recommends movies based on content similarity. Users can search for any movie and instantly receive personalized recommendations displayed with posters fetched via the TMDB API.

---

## 🚀 Live Demo

👉 **Try the app here:** *https://recommendationsystempj.streamlit.app/*  

---

## 📚 Overview

This project implements a **content-based movie recommendation system** using cosine similarity over movie metadata such as genres, keywords, cast, and crew. Recommendations are accompanied by movie posters fetched from **The Movie Database (TMDB)** API for an enhanced user experience.

The system is optimized using a compressed similarity matrix (`.pbz2` format) to ensure high performance during deployment.

---

## ✅ Features

- 🎥 **Search any movie** from a dropdown menu  
- 🧠 **Content-based recommendation engine**  
- ⚡ **Fast, optimized similarity lookup**  
- 🖼️ **High-quality posters via TMDB API**  
- 🌐 **Deployed on Streamlit Cloud**  
- 📦 **Lightweight UI with clean layout**  
- 🧩 **Git LFS support for large model files**

---

## 🛠️ Tech Stack

**Programming & Libraries**
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Pickle / BZ2 Compression  
- Streamlit  
- Requests  

**Tools & Services**
- Git + Git LFS  
- Streamlit Cloud  
- TMDB API  

**Dataset**
- Kaggle Movies Dataset (Credits + Movies Metadata)

---

## 📁 Project Structure

┣ 📜 app.py
┣ 📜 requirements.txt
┣ 📜 movie_list_compressed.pbz2
┣ 📜 similarity_compressed.pbz2
┣ 📜 .gitattributes
┣ 📜 .gitignore
┗ 📜 README.md



---

## 🧠 How the Recommendation System Works

1. **Dataset Preparation**
   - Imported movies metadata and credits dataset from Kaggle
   - Cleaned columns (eg: genres, keywords, cast, crew)
   - Combined them into a single textual representation

2. **Text Vectorization**
   - Used CountVectorizer to tokenize content

3. **Similarity Calculation**
   - Computed pairwise similarity using cosine similarity
   - Saved similarity matrix using BZ2 compression

4. **Recommendation Logic**
   - For selected movie:
     - Identify its index
     - Sort movies by similarity scores
     - Retrieve top 5 recommendations

5. **Poster Fetching**
   - Calls TMDB API using movie ID
   - Displays posters in a responsive layout

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Parsh13/Recommendation-System.git
cd Recommendation-System
```
### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the app locally
```bash
streamlit run app.py
```

## 📡 Deployment

This project is deployed on **Streamlit Cloud**, which provides:

- ✅ Support for large files via **Git LFS**
- ✅ Automatic dependency installation from `requirements.txt`
- ✅ Continuous deployment directly from GitHub

To deploy your own version:

1. Push your project to GitHub  
2. Go to https://share.streamlit.io  
3. Connect your repository  
4. Select `app.py` as the entrypoint  
5. Deploy!

---

## 🔒 API Usage Note

This application uses the **TMDB API** to fetch movie posters and additional metadata.

You must obtain your own API key from:

👉 https://www.themoviedb.org/documentation/api

After obtaining the API key, replace it in `app.py`:

```python
api_key = "YOUR_API_KEY"
