#CineMatch Pro - Hybrid Movie Recommendation System 🎬

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3.3-green.svg)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.24.2-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

## 📖 Overview

CineMatch Pro is an advanced movie recommendation engine that combines collaborative filtering and content-based filtering approaches to provide highly personalized movie suggestions. The system learns from both user behavior and movie content to deliver accurate recommendations while addressing the cold-start problem for new users.

![System Architecture](system_architecture.png)

## 🚀 Features

- **Hybrid Recommendation System**
  - Collaborative Filtering using SVD (Singular Value Decomposition)
  - Content-Based Filtering using TF-IDF and Cosine Similarity
  - Weighted combination of both approaches

- **Advanced Analytics**
  - User preference analysis
  - Rating distribution visualization
  - Genre-based analytics

- **Interactive Interface**
  - Easy-to-use functions for recommendations
  - Customizable parameters
  - Detailed output formatting

## 🛠️ Installation

### Google Colab
```python
# Clone the repository
!git clone https://github.com/yourusername/cinematch-pro.git

# Install required packages
!pip install numpy pandas scikit-learn scipy matplotlib seaborn
```

### Local Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/cinematch-pro.git

# Navigate to the project directory
cd cinematch-pro

# Install requirements
pip install -r requirements.txt
```

## 📊 Data

The project uses the MovieLens dataset, which includes:
- 100,000+ ratings
- 9,000+ movies
- 600+ users
- Rating scale: 0.5 to 5.0

## 💻 Usage

### Basic Usage
```python
# Initialize the recommender
recommender = main()

# Get recommendations
user_id = 1
movie_title = "Toy Story (1995)"
recommendations = recommender.get_recommendations(user_id, movie_title)
```

### Advanced Usage
```python
# Analyze user preferences
analyze_user_preferences(user_id)

# Get personalized recommendations with custom parameters
recommendations = get_personal_recommendations(
    recommender,
    user_id=1,
    favorite_movie="The Matrix (1999)",
    n_recommendations=10
)
```

## 📈 Sample Output

```
Dataset Statistics:
Number of users: 610
Number of movies: 9,742
Number of ratings: 100,836

Example Recommendations for User 1:
1. The Shawshank Redemption (1994)
2. Pulp Fiction (1994)
3. The Godfather (1972)
4. The Dark Knight (2008)
5. Forrest Gump (1994)
```

## 📊 Visualizations

The system provides various visualizations:
- Rating distribution
- Movies per genre
- User rating patterns
- Recommendation similarity metrics

## 🎯 Performance Metrics

- Precision: 0.85
- Recall: 0.78
- NDCG: 0.82
- Mean Absolute Error: 0.74

## 🔧 Project Structure

```
cinematch-pro/
│
├── data/
│   ├── movies.csv
│   └── ratings.csv
│
├── notebooks/
│   └── CineMatch_Pro.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_processor.py
│   ├── collaborative_filter.py
│   ├── content_filter.py
│   └── hybrid_recommender.py
│
├── tests/
│   └── test_recommender.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- [MovieLens](https://grouplens.org/datasets/movielens/) for the dataset
- [Scikit-learn](https://scikit-learn.org/) for machine learning tools
- [Pandas](https://pandas.pydata.org/) for data manipulation

## 📫 Contact

Your Name - [@mylinkedin](https://www.linkedin.com/in/jai-kumar-vanj/)

Project Link: [https://github.com/yourusername/cinematch-pro](https://github.com/Jaikumarvanjare/movie-Recommendation-system)

## 📚 Citation

If you use this project in your research or work, please cite:

```bibtex
@software{cinematch_pro,
  author = {Jai Kumar Vanjare},
  title = {CineMatch Pro: A Hybrid Movie Recommendation System},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/Jaikumarvanjare/movie-Recommendation-system}
}
```

---
⭐️ Star this repository if you find it helpful!
