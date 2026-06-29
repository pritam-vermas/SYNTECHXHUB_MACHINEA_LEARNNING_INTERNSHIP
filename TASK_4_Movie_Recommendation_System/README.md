# 🎬 Movie Recommendation System

### 🚀 Live Demo

**Try the Project Here:**
**https://huggingface.co/spaces/pritamvermas/Movie_Recommendation_System**

---

## 📌 Project Overview

The Movie Recommendation System is a **Content-Based Recommendation System** developed using **Python** and **Machine Learning**. It recommends movies similar to the one selected by the user by analyzing movie metadata such as genres, keywords, cast, crew, and overview.

The project is deployed on **Hugging Face Spaces**, allowing users to interact with the recommendation system through a simple web interface.

---

## 🎯 Objective

The primary objective of this project is to build a recommendation engine that:

* Recommends similar movies based on content.
* Uses Natural Language Processing (NLP) techniques.
* Calculates similarity between movies using Cosine Similarity.
* Provides an interactive web interface for users.

---

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset**.

Files Used:

* tmdb_5000_movies.csv
* tmdb_5000_credits.csv

---

## 🔍 Data Preprocessing

The following preprocessing steps were performed:

* Merged movie and credits datasets.
* Removed unnecessary columns.
* Handled missing values.
* Extracted:

  * Genres
  * Keywords
  * Top 3 Cast Members
  * Director
* Combined all important information into a single **tags** column.
* Converted text to lowercase.
* Applied Porter Stemming.

---

## 🤖 Machine Learning Workflow

1. Data Cleaning
2. Feature Engineering
3. Text Vectorization using CountVectorizer
4. Cosine Similarity Calculation
5. Movie Recommendation Generation

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* NLTK
* Pickle
* Gradio
* Hugging Face Spaces

---

## 📈 Recommendation Algorithm

The recommendation system works using the following approach:

* Convert movie metadata into textual tags.
* Transform tags into numerical vectors using CountVectorizer.
* Compute similarity scores using Cosine Similarity.
* Recommend the Top 5 most similar movies.

---

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
```

---

## 🚀 Features

* Interactive movie selection
* Top 5 similar movie recommendations
* Fast recommendation generation
* Beginner-friendly implementation
* Hugging Face deployment

---

## 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Movie-Recommendation-System.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## 🌐 Live Demo

**Hugging Face Space**

YOUR_HUGGING_FACE_LINK

---

## 📚 Future Improvements

* Movie Posters
* IMDb Ratings
* Release Year
* Movie Trailers
* Search Suggestions
* Hybrid Recommendation System

---

## 👨‍💻 Author

**Pritam Verma**

Machine Learning Intern

---

## ⭐ Conclusion

This project demonstrates the complete workflow of building a Content-Based Movie Recommendation System using Machine Learning and Natural Language Processing. It covers data preprocessing, feature engineering, vectorization, similarity computation, and deployment through Hugging Face Spaces.
