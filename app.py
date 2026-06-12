import streamlit as st
import pandas as pd
import requests
from recommendation import Engine

API_KEY = "b02a2e8e162f1f7729853c37d0bffa3e"

st.set_page_config(
    page_title="Movie Recommendation System",
    layout="wide"
)


@st.cache_resource
def load_engine():
    return Engine("cleaned_dataset.csv")

obj = load_engine()

df = pd.read_csv("cleaned_dataset.csv")

def fetch_poster(movie_id):
    try:
        
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path is None:
            return None
        return f"https://image.tmdb.org/t/p/w500{poster_path}"
    
    except Exception as e:
        print("Poster Error:", e)
        return None

st.title("🎬 Movie Recommendation System")
movie = st.selectbox(
    "Select Movie",
    df["title"].values
)

if st.button("Recommend Movies"):
    recommendations = obj.top_recommendations(movie)
    cols = st.columns(5)
    for idx, rec in enumerate(recommendations):
        with cols[idx]:
            poster = fetch_poster(rec["movie_id"])
            if poster:
                st.image(poster)
            else:
                st.write("❌ Poster Missing from TMDB 😢")
            st.write(rec["title"])
