<p align='center'>🎬 Movie Recommender System</p>
<p align="center">
<video controls autoplay muted loop width="800">
<source src="https://user-images.githubusercontent.com/104669486/201644731-a45a5806-eddd-46bb-97e6-29f1aa61354e.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
</p>

A simple and intuitive Movie Recommendation System built with Streamlit. This application helps users discover new movies based on their interests by suggesting films similar to one they've selected.

🔗 Live Demo: Movie Recommender App

✨ Features
🎨 User-friendly Interface: A clean and simple UI for easy navigation.

🎞️ Vast Movie Selection: Choose from a large database of movies.

⚡ Instant Recommendations: Get a list of 5 similar movies instantly.

🧩 Content-Based Filtering: Recommendations are generated using movie tags, genres, cast, and director to find stylistically similar films.

🧠 How It Works
This recommendation system uses a content-based filtering approach. Here's a simplified overview:

Data Collection:
The model is trained on a movie dataset (TMDB 5000) containing genres, keywords, cast, and crew for each film.

Feature Engineering:
Relevant features (like cast, director, and genres) are combined into a single text field called “tags” for each movie.

Vectorization:
The tags are transformed into numerical vectors using TF-IDF (Term Frequency–Inverse Document Frequency), representing each movie in multi-dimensional space.

Similarity Calculation:
Using cosine similarity, the system computes how close one movie is to another in terms of content.

Recommendation:
The top 5 most similar movies are displayed as recommendations.

🛠️ Technologies Used
Technology

Purpose

Python

Core programming language

Streamlit

Building and deploying the web app

Pandas

Data manipulation and processing

Scikit-learn

TF-IDF vectorization and cosine similarity

TMDB 5000 Movie Dataset

Dataset powering the recommendations

🚀 How to Use
Visit the Live App.

Select a movie from the dropdown list.

Click the “Recommend” button.

Instantly view the top 5 recommended movies below!

📂 Project Structure
Movie-Recommendation-System/
│
├── app.py             # Main Streamlit application
├── movies.pkl         # Preprocessed movie data
├── demo.mp4           # Demo video
├── README.md          # Project documentation
└── requirements.txt   # Dependencies

📸 Preview
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/6f0fbce3-c6a2-4dc4-abd6-81a13284078e" />

🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a pull request.

🧾 License
This project is open-source and available under the MIT License.

⭐ If you like this project, consider giving it a star on GitHub!
