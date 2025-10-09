import pandas as pd
import streamlit as st
import requests
import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- CONFIGURATION & SETUP ---

# Set Streamlit page configuration
st.set_page_config(layout="wide")

# Securely load the API key from Streamlit's secrets manager
try:
    API_KEY_AUTH = st.secrets["TMDB_API_KEY"]
except KeyError:
    st.error("TMDb API key not found. Please add it to your Streamlit secrets.")
    st.stop()

# Constants for API and image URLs
POSTER_BASE_URL = "https://image.tmdb.org/t/p/w500/"
PLACEHOLDER_IMAGE_URL = "https://via.placeholder.com/500x750.png?text=Poster+Not+Available"

# Create a persistent session object to reuse connections for efficiency
session = requests.Session()


# --- DATA LOADING & MODELING (with Caching) ---

@st.cache_data
def load_data_and_build_model(data_path='data.csv'):
    """
    Loads the movie dataset, creates the recommendation model, and calculates the
    similarity matrix. The @st.cache_data decorator ensures this heavy computation
    only runs once.
    Returns:
        DataFrame, similarity_matrix, list of movie titles
    """
    try:
        df = pd.read_csv(data_path)
        
        # Create the feature vectors from the 'tags' column using CountVectorizer
        cv = CountVectorizer(max_features=5000, stop_words='english')
        vectors = cv.fit_transform(df['tags']).toarray()
        
        # Calculate the cosine similarity matrix
        similarity = cosine_similarity(vectors)
        
        titles = df['title'].values
        return df, similarity, titles
        
    except FileNotFoundError:
        st.error(f"The data file '{data_path}' was not found. Please make sure it's in the correct directory.")
        return None, None, None

# Load the data and model
df, similarity, titles = load_data_and_build_model()


# --- HELPER FUNCTIONS ---

def fetch_movie_details(movie_id):
    """
    Fetches movie poster and overview from the TMDb API. Includes a retry mechanism
    for robustness against transient network errors.
    """
    retries = 3
    for i in range(retries):
        try:
            url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY_AUTH}'
            response = session.get(url, timeout=10)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
            data = response.json()

            poster_path = POSTER_BASE_URL + data['poster_path'] if data.get('poster_path') else None
            overview = data.get('overview', 'No description available.')
            title = data.get('title', 'Title not found.')
            return title, poster_path, overview

        except requests.exceptions.RequestException as e:
            if i < retries - 1:
                time.sleep(0.5) # Wait before retrying
                continue
            else:
                # On final retry failure, return placeholder
                return "Error", PLACEHOLDER_IMAGE_URL, "Could not fetch movie details."

def get_recommendations(movie_title):
    """
    Finds top similar movies and fetches their details concurrently,
    filtering out any movies for which a poster could not be fetched.
    """
    if df is None:
        return []

    try:
        movie_index = df[df['title'] == movie_title].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:31]
        
        movie_ids_to_fetch = [df.iloc[i[0]]['movie_id'] for i in movies_list]
        
        recommendations = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_id = {executor.submit(fetch_movie_details, movie_id): movie_id for movie_id in movie_ids_to_fetch}
            
            for future in as_completed(future_to_id):
                try:
                    title, poster, overview = future.result()
                    if poster: # Only include movies with a valid poster
                        recommendations.append({'title': title, 'poster': poster, 'overview': overview})
                except Exception as exc:
                    st.error(f'An error occurred while fetching movie details: {exc}')

        return recommendations[:20] # Return the first 20 valid recommendations
        
    except (IndexError, KeyError):
        st.error(f"Movie '{movie_title}' not found in the dataset.")
        return []

@st.cache_data
def get_demo_movies():
    """
    Fetches details for a predefined list of popular movies to display on load.
    Results are cached to prevent re-fetching on every script rerun.
    """
    demo_movie_ids = [299534, 155, 680, 27205, 157336, 475557, 634649, 438631, 603, 13]
    
    demo_movies = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_id = {executor.submit(fetch_movie_details, movie_id): movie_id for movie_id in demo_movie_ids}
        for future in as_completed(future_to_id):
            try:
                title, poster, overview = future.result()
                if poster:
                    demo_movies.append({'title': title, 'poster': poster, 'overview': overview})
            except Exception:
                pass # Ignore errors for demo movies
    return demo_movies

# --- STREAMLIT UI ---

if titles is not None:
    # Custom CSS for dark theme, carousels, and poster overlay effect
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
            
            /* Global Styles & Dark Theme */
            html, body, [class*="st-"], button { font-family: 'Poppins', sans-serif; }
            body, .stApp { background-color: #0e1117; color: #fafafa; }
            #MainMenu, footer, header { visibility: hidden; }

            /* Custom Button Style */
            div[data-testid="stButton"] > button {
                background-color: #d33639; color: white; border: none; border-radius: 8px;
                padding: 10px 20px; transition: background-color 0.3s ease;
            }
            div[data-testid="stButton"] > button:hover { background-color: #b02a2d; }

            /* Carousel Styling (for demo carousel) */
            .carousel-wrapper { position: relative; margin-bottom: 2rem; }
            .carousel-container { display: flex; overflow-x: auto; padding: 20px 10px;
                                 scroll-behavior: smooth; scrollbar-width: none; -ms-overflow-style: none; }
            .carousel-container::-webkit-scrollbar { display: none; }
            .carousel-item { flex: 0 0 auto; width: 220px; margin-right: 20px; }
            
            .carousel-button {
                position: absolute; top: 50%; transform: translateY(-50%);
                background-color: rgba(0, 0, 0, 0.5); color: white; border: none;
                border-radius: 50%; width: 40px; height: 40px; font-size: 24px;
                cursor: pointer; z-index: 10; display: flex; align-items: center; justify-content: center;
            }
            .carousel-button:hover { background-color: rgba(0, 0, 0, 0.8); }
            .carousel-button.prev { left: -15px; }
            .carousel-button.next { right: -15px; }

            /* Movie Card with Hover Overlay */
            .movie-card { position: relative; border-radius: 10px; overflow: hidden;
                          cursor: pointer; transition: transform 0.3s ease, box-shadow 0.3s ease; }
            .movie-card:hover { transform: scale(1.05); box-shadow: 0 8px 24px rgba(0,0,0,0.5); }
            .movie-card img { display: block; width: 100%; aspect-ratio: 2 / 3; object-fit: cover; }
            .overlay {
                position: absolute; top: 0; left: 0; right: 0; bottom: 0;
                background: linear-gradient(to top, rgba(0,0,0,0.95) 20%, rgba(0,0,0,0));
                color: white; opacity: 0; transition: opacity 0.3s ease; padding: 1rem;
                display: flex; flex-direction: column; justify-content: flex-end;
            }
            .movie-card:hover .overlay { opacity: 1; }
            .overlay-title { font-weight: 600; font-size: 1rem; margin-bottom: 0.25rem; }
            .overlay-overview {
                font-size: 0.75rem; max-height: 100px; overflow-y: auto;
                scrollbar-width: thin; scrollbar-color: #555 #262730;
            }
            .overlay-overview::-webkit-scrollbar { width: 5px; }
            .overlay-overview::-webkit-scrollbar-track { background: #262730; }
            .overlay-overview::-webkit-scrollbar-thumb { background-color: #555; border-radius: 6px; }
        </style>
    """, unsafe_allow_html=True)

    st.title('🎬 MOVIE ')

    # --- DEMO CAROUSEL ---
    st.subheader("Featured Movies")
    demo_movies = get_demo_movies()
    if demo_movies:
        demo_cards_html = ""
        for movie in demo_movies:
            demo_cards_html += f"""
            <div class="carousel-item">
                <div class="movie-card">
                    <img src="{movie['poster']}" alt="{movie['title']} poster">
                    <div class="overlay">
                        <p class="overlay-title">{movie['title']}</p>
                        <p class="overlay-overview">{movie['overview']}</p>
                    </div>
                </div>
            </div>
            """
        st.markdown(f"""
            <div class="carousel-wrapper">
                <button class="carousel-button prev" onclick="scrollCarousel('demoCarousel', 'prev')">&lt;</button>
                <div class="carousel-container" id="demoCarousel">{demo_cards_html}</div>
                <button class="carousel-button next" onclick="scrollCarousel('demoCarousel', 'next')">&gt;</button>
            </div>
        """, unsafe_allow_html=True)

    # --- RECOMMENDATION SECTION ---
    st.subheader("Get Personal Recommendations")
    selected_movie = st.selectbox(
        'Select a movie you like, and I will recommend similar ones:',
        options=titles,
        key='movie_select'
    )

    if 'recommendations' not in st.session_state:
        st.session_state.recommendations = None

    if st.button('Recommend Movies'):
        with st.spinner('Finding recommendations for you...'):
            recommendations = get_recommendations(selected_movie)
            if recommendations:
                st.session_state.recommendations = recommendations
            else:
                st.session_state.recommendations = None
                st.warning("Could not generate recommendations. Please try another movie.")

    if st.session_state.recommendations:
        recs = st.session_state.recommendations
        
        # Define the number of columns for the grid
        num_cols = 5
        # Calculate the number of rows needed
        num_rows = (len(recs) + num_cols - 1) // num_cols

        # Create a grid of recommendations
        for i in range(num_rows):
            cols = st.columns(num_cols)
            for j in range(num_cols):
                movie_index = i * num_cols + j
                if movie_index < len(recs):
                    with cols[j]:
                        movie = recs[movie_index]
                        st.markdown(f"""
                            <div class="movie-card" style="margin-bottom: 20px;">
                                <img src="{movie['poster']}" alt="{movie['title']} poster">
                                <div class="overlay">
                                    <p class="overlay-title">{movie['title']}</p>
                                    <p class="overlay-overview">{movie['overview']}</p>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
    
    # --- JAVASCRIPT FOR CAROUSEL ---
    st.markdown("""
        <script>
            function scrollCarousel(carouselId, direction) {
                const carousel = document.getElementById(carouselId);
                if (carousel) {
                    const scrollAmount = 240; // Width of item + margin
                    if (direction === 'prev') {
                        carousel.scrollLeft -= scrollAmount;
                    } else {
                        carousel.scrollLeft += scrollAmount;
                    }
                }
            }
        </script>
    """, unsafe_allow_html=True)

