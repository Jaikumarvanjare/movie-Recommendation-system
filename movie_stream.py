import streamlit as st
import pickle
import pandas as pd

# Load preprocessed data
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found in database."]
    
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]  # top 5 recommendations
    
    recommended_movies = [movies.iloc[i[0]].title for i in distances]
    return recommended_movies


# ----------------- STREAMLIT UI -----------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

st.title("🎬 Movie Recommendation System")
st.write("Find movies similar to your favorite ones!")

# Movie selection dropdown
movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie:", movie_list)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader("Top 5 Recommended Movies:")
    for i, movie in enumerate(recommendations, start=1):
        st.write(f"{i}. {movie}")
