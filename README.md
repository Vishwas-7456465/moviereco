# 🎬 Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey.svg)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)

A beginner-friendly, full-stack Movie Recommendation System built using Python, Flask, and Machine Learning. The application provides content-based movie recommendations using TF-IDF and Cosine Similarity, presented in a clean, modern, and responsive web interface.

---

## ✨ Features

- **Personalized Recommendations:** Uses Content-Based Filtering to suggest movies similar to your favorites.
- **Modern UI/UX:** Clean, responsive, and intuitive interface with a dark-themed design.
- **Smart Search:** Autocomplete search suggestions as you type.
- **Resilient Image Handling:** Automatic SVG fallback placeholders for missing movie posters.
- **Lightweight Backend:** Fast and efficient Python Flask API.

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3 (Vanilla, Responsive Design)
- JavaScript (Fetch API, DOM Manipulation)

### Backend
- **Framework:** Python Flask
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (TF-IDF Vectorizer, Cosine Similarity)

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing.

### Prerequisites

Make sure you have Python installed on your system (Python 3.8+ recommended).

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vishwas-7456465/moviereco.git
   cd moviereco
   ```

2. **Create a virtual environment (Optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open the website**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## 🧠 How It Works

The recommendation engine uses **Content-Based Filtering**:
1. It analyzes the `genres` and `overview` of all movies in the dataset.
2. A `TfidfVectorizer` converts these text descriptions into numerical feature vectors.
3. When you search for a movie, the system calculates the **Cosine Similarity** between that movie's vector and all other movies.
4. It returns the top 5 most similar movies based on the similarity scores.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

## 📝 License

This project is open-source and available under the MIT License.
