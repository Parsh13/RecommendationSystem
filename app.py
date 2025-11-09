import pickle
import streamlit as st

import requests



st.markdown("""

    <style>

    .stButton>button {

        background-color: #FF4B4B;

        color: white;

        border-radius: 10px;

        border: none;

        padding: 0.6em 1.2em;

        font-size: 16px;

        font-weight: 600;

        transition: all 0.3s ease;

        box-shadow: 0px 4px 8px rgba(255, 75, 75, 0.3);

    }

    .stButton>button:hover {

        background-color: #FF7373;

        transform: translateY(-2px);

        box-shadow: 0px 6px 12px rgba(255, 75, 75, 0.4);

    }

    </style>

    """, unsafe_allow_html=True)

# -----------------------------

# Helper Function to Fetch Poster

# -----------------------------

def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

    response = requests.get(url)

    data = response.json()

    poster_path = data.get('poster_path')

    if poster_path:

        return f"https://image.tmdb.org/t/p/w500/{poster_path}"

    else:

        return "https://via.placeholder.com/500x750?text=No+Image"



# -----------------------------

# Recommendation Function

# -----------------------------

def recommend(movie):

    index = movies[movies['title'] == movie].index[0]

    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]



    recommended_movie_names = []

    recommended_movie_posters = []

    for i in distances:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie_posters.append(fetch_poster(movie_id))

        recommended_movie_names.append(movies.iloc[i[0]].title)



    return recommended_movie_names, recommended_movie_posters



# -----------------------------

# Streamlit Page Configuration

# -----------------------------

st.set_page_config(

    page_title="🎥 Movie Recommender",

    page_icon="🎬",

    layout="wide",

    initial_sidebar_state="collapsed"

)



# -----------------------------

# Custom CSS for Styling

# -----------------------------

st.markdown("""

    <style>

        .main {

            background-color: #0E1117;

            color: #FAFAFA;

            font-family: 'Segoe UI', sans-serif;

        }

        h1 {

            text-align: center;

            color: #FF4B4B;

        }

        .stSelectbox label {

            font-size: 18px !important;

            color: #FFFFFF !important;

        }

        .movie-title {

            text-align: center;

            font-weight: bold;

            color: #FFFFFF;

        }

    </style>

""", unsafe_allow_html=True)



# -----------------------------

# Load Data

# -----------------------------

import bz2



# Load compressed data

with bz2.BZ2File('movie_list_compressed.pbz2', 'rb') as f:

    movies = pickle.load(f)



with bz2.BZ2File('similarity_compressed.pbz2', 'rb') as f:

    similarity = pickle.load(f)

movie_list = movies['title'].values



# -----------------------------

# UI Section

# -----------------------------

st.title("🎬 Movie Recommender System")

st.markdown("<h5 style='text-align:center; color:#FAFAFA;'>Find your next favorite movie!</h5>", unsafe_allow_html=True)





selected_movie = st.selectbox(

    "🎞️ Type or select a movie from the dropdown:",

    movie_list,

    index=None,

    placeholder="Select a movie..."

)



st.write("---")



if st.button('✨ Show Recommendations'):

    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)



    # Display movies in a responsive layout

    cols = st.columns(5)

    for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):

        with col:

            st.image(poster, width='content')

            st.markdown(f"<p class='movie-title'>{name}</p>", unsafe_allow_html=True)



else:

    st.markdown("<p style='text-align:center; color:gray;'>Select a movie and click 'Show Recommendations' to begin.</p>", unsafe_allow_html=True)

