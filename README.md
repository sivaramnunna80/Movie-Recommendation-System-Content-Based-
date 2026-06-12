🎬 Movie Recommendation System

A content-based movie recommendation system built using Python, Pandas, Scikit-Learn, and Streamlit. The system recommends movies similar to the user's selected movie by analyzing movie metadata and calculating similarity scores.

🚀 Features
Recommend movies based on user selection
Content-based filtering approach
Displays movie posters using TMDB API
Fast recommendation generation
Interactive web interface built with Streamlit
Preprocessed movie dataset for improved accuracy
🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-Learn
NLTK
Streamlit
TMDB API


📂 Dataset
The project uses the TMDB Movies Dataset containing:
Movie titles
Genres
Keywords
Cast
Crew
Overview
Dataset Source:
The Movie Database (TMDB)


⚙️ How It Works
Data preprocessing and cleaning
Feature extraction from movie metadata
Text vectorization using CountVectorizer/TF-IDF
Similarity calculation using Cosine Similarity
Recommend top similar movies to the selected movie


📸 Project Demo
User selects a movie
        ↓
Feature Extraction
        ↓
Vectorization
        ↓
Cosine Similarity
        ↓
Top Recommended Movies


🔧 Installation
git clone <repository-link>
cd Movie-Recommendation-System
pip install -r requirements.txt
streamlit run app.py


📈 Future Improvements
Hybrid Recommendation System
Collaborative Filtering
User Authentication
Personalized Recommendations
Faster Similarity Search using FAISS
Deployment on Cloud Platforms
