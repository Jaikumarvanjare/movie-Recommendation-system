# <p align='center'>Movie Recommender System</p>

A simple and intuitive **Movie Recommendation System** built with **Streamlit**.
This application helps users discover new movies based on their interests by suggesting films similar to one they've selected.

🔗 **Live Demo:** [Movie Recommender App](https://movie-recommendation-system-gzi2prtm5gxqq5hjnthstd.streamlit.app/)


## 🎥 Demo Video

<video width="100%" controls>
  <source src="https://github.com/Jaikumarvanjare/Movie-Recommendation-System/raw/main/Demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

[![Watch the Demo](https://github.com/Jaikumarvanjare/Movie-Recommendation-System/raw/main/demo_preview.png)](https://github.com/Jaikumarvanjare/Movie-Recommendation-System/raw/main/Demo.mp4)

---

## ✨ Features

* 🎨 **User-friendly Interface:** A clean and simple UI for easy navigation.
* 🎞️ **Vast Movie Selection:** Choose from a large database of movies.
* ⚡ **Instant Recommendations:** Get a list of 5 similar movies instantly.
* 🧩 **Content-Based Filtering:** Recommendations are generated using movie tags, genres, cast, and director to find stylistically similar films.

---

## 🧠 How It Works

This recommendation system uses a **content-based filtering** approach. Here's a simplified overview:

1. **Data Collection:**
   The model is trained on a movie dataset (TMDB 5000) containing genres, keywords, cast, and crew for each film.

2. **Feature Engineering:**
   Relevant features (like cast, director, and genres) are combined into a single text field called **“tags”** for each movie.

3. **Vectorization:**
   The tags are transformed into numerical vectors using **TF-IDF (Term Frequency–Inverse Document Frequency)**, representing each movie in multi-dimensional space.

4. **Similarity Calculation:**
   Using **cosine similarity**, the system computes how close one movie is to another in terms of content.

5. **Recommendation:**
   The top 20 most similar movies are displayed as recommendations.

---

## 🛠️ Technologies Used

| Technology                  | Purpose                                    |
| --------------------------- | ------------------------------------------ |
| **Python**                  | Core programming language                  |
| **Streamlit**               | Building and deploying the web app         |
| **Pandas**                  | Data manipulation and processing           |
| **Scikit-learn**            | TF-IDF vectorization and cosine similarity |
| **TMDB 5000 Movie Dataset** | Dataset powering the recommendations       |

---

## 🚀 How to Use

1. Visit the [Live App](https://movie-recommendation-system-gzi2prtm5gxqq5hjnthstd.streamlit.app/).
2. Select a movie from the dropdown list.
3. Click the **“Recommend”** button.
4. Instantly view the top 5 recommended movies below!

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│
├── app.py                # Main Streamlit application
├── movies.pkl            # Preprocessed movie data
├── demo.mp4              # Demo video
├── README.md             # Project documentation
└── requirements.txt      # Dependencies
```

---

## 📸 Preview

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/6f0fbce3-c6a2-4dc4-abd6-81a13284078e" />
---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a pull request.

---

## 🧾 License

This project is open-source and available under the [MIT License](LICENSE).

---

⭐ **If you like this project, consider giving it a star on GitHub!**
