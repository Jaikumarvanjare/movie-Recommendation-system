🎬 Movie Recommender System
A simple and intuitive movie recommendation system built with Streamlit. This application helps users discover new movies based on their interests by suggesting films similar to one they've selected.

Live Demo: https://movie-recommendation-system-gzi2prtm5gxqq5hjnthstd.streamlit.app/

✨ Features
User-friendly Interface: A clean and simple UI for easy navigation.

Vast Movie Selection: Choose from a large database of movies.

Instant Recommendations: Get a list of 5 similar movies instantly.

Content-Based Filtering: Recommendations are generated based on movie tags, genres, cast, and director to find stylistically similar films.

🧠 How It Works
This recommendation system uses a content-based filtering approach. Here's a simplified breakdown of the logic:

Data Collection: The model is trained on a movie dataset that includes details like genres, keywords, cast, and crew for each film.

Feature Engineering: Relevant text-based features (like cast, director, and genres) are combined into a single "tags" string for each movie.

Vectorization: The "tags" for all movies are converted into numerical vectors using a technique called TF-IDF (Term Frequency-Inverse Document Frequency). This allows us to represent each movie as a point in a multi-dimensional space.

Similarity Calculation: The cosine similarity is calculated between the vector of the user's selected movie and the vectors of all other movies. A higher cosine similarity score means the movies are more alike in content.

Recommendation: The top 5 movies with the highest similarity scores are returned as the recommendations.

🛠️ Technologies Used
Python: The core programming language.

Streamlit: For building and deploying the interactive web application.

Pandas: For data manipulation and processing.

Scikit-learn: For implementing TF-IDF vectorization and calculating cosine similarity.

TMDB 5000 Movie Dataset: The dataset used to power the recommendations.

🚀 How to Use
Navigate to the live application.

Click on the dropdown menu labeled "Select a movie you like".

Choose a movie from the list.

Click the "Recommend" button.

View the list of recommended movies that appears below!

This README was generated to provide documentation for the Streamlit application. Feel free to use and modify it.
