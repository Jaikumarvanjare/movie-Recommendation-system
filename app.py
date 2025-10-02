# ----------------------------------------------------------------------
# MOVIE RECOMMENDER SYSTEM
# Author: JAIKUMAR J
# Last Updated: September 20, 2025
# ----------------------------------------------------------------------

import streamlit as st
import pickle
import requests
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# --- LOAD CUSTOM CSS ---
def local_css(file_name):
    """Loads a local CSS file for custom styling."""
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found. Please ensure '{file_name}' is in the '.streamlit' directory.")

local_css(".streamlit/style.css")

# --- DATA LOADING ---
@st.cache_data(show_spinner="Loading models...")
def load_data():
    """Loads movie data and similarity matrix from pickle files."""
    try:
        with open("movies_list.pkl", 'rb') as f:
            movies = pickle.load(f)
        with open("similarity.pkl", 'rb') as f:
            similarity = pickle.load(f)
        return movies, similarity
    except FileNotFoundError:
        st.error("Model files not found. Please ensure 'movies_list.pkl' and 'similarity.pkl' exist.")
        return None, None

# --- API FETCHING ---
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    """Fetches a movie poster URL from TMDb API, returning None on failure."""
    try:
        api_key = st.secrets["tmdb"]["api_key"]
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        return "https://image.tmdb.org/t/p/w500/" + poster_path if poster_path else None
    except (requests.RequestException, KeyError):
        return None

# --- CORE RECOMMENDATION LOGIC ---
def recommend(movie_title, movies_df, similarity_matrix):
    """Finds up to 5 recommendations that have valid posters."""
    try:
        movie_index = movies_df[movies_df['title'] == movie_title].index[0]
        distances = similarity_matrix[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:16]
        
        recommended_movies, recommended_posters = [], []
        
        for i in movies_list:
            if len(recommended_movies) >= 5:
                break
            movie_id = movies_df.iloc[i[0]].id
            poster_url = fetch_poster(movie_id)
            if poster_url:
                recommended_movies.append(movies_df.iloc[i[0]].title)
                recommended_posters.append(poster_url)
        return recommended_movies, recommended_posters
    except IndexError:
        st.error("Movie not found in the dataset.")
        return [], []

# --- MAIN APP INTERFACE ---
st.title('🎬 Movie Recommender System')

movies, similarity = load_data()

if movies is not None and similarity is not None:
    # --- STABLE IMAGE CAROUSEL ---
    
    # Initialize carousel movie list in session state if it doesn't exist
    if 'carousel_movies' not in st.session_state:
        try:
            sample_df = movies.sample(n=12)
            image_urls = [fetch_poster(movie_id) for movie_id in sample_df['id'].values]
            # Store the valid URLs in session state
            st.session_state.carousel_movies = [url for url in image_urls if url]
        except Exception:
            st.session_state.carousel_movies = []

    # Display the carousel using the list from session state
    if st.session_state.carousel_movies:
        try:
            imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")
            imageCarouselComponent(imageUrls=st.session_state.carousel_movies, height=250)
        except Exception as e:
            st.error(f"Error loading image carousel: {e}")

    # --- USER INPUT SECTION ---
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie you like to get a recommendation:", 
        movie_list,
        index=None,
        placeholder="Select a movie..."
    )

    # --- RECOMMENDATION DISPLAY ---
    if selected_movie:
        if st.button('Recommend', type="primary", use_container_width=True):
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader(f"Recommendations for '{selected_movie}':")
            
            names, posters = recommend(selected_movie, movies, similarity)
            
            if names:
                cols = st.columns(len(names), gap="large")
                for i, (name, poster) in enumerate(zip(names, posters)):
                    with cols[i]:
                        st.image(poster, use_column_width='always')
                        st.caption(name)
            else:
                st.warning("Could not find enough recommendations with available posters.")
