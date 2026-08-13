import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

class MovieRecommender:
    def __init__(self, csv_path='movies.csv'):
        """
        Initializes the MovieRecommender by loading the dataset and
        precomputing the TF-IDF and Cosine Similarity matrices.
        """
        self.csv_path = csv_path
        self.df = None
        self.tfidf_matrix = None
        self.cosine_sim = None
        self.indices = None
        
        # Load data and prepare the model
        self.load_data()
        self.build_model()

    def load_data(self):
        """
        Loads the movies dataset from the CSV file.
        """
        if not os.path.exists(self.csv_path):
            raise FileNotFoundError(f"Dataset file not found at: {self.csv_path}")
        
        self.df = pd.read_csv(self.csv_path)
        
        # Fill missing values to avoid errors during text processing
        self.df['title'] = self.df['title'].fillna('').astype(str)
        self.df['genres'] = self.df['genres'].fillna('').astype(str)
        self.df['overview'] = self.df['overview'].fillna('').astype(str)
        self.df['vote_average'] = self.df['vote_average'].fillna(0.0).astype(float)
        self.df['release_date'] = self.df['release_date'].fillna('').astype(str)
        self.df['poster_url'] = self.df['poster_url'].fillna('').astype(str)

    def build_model(self):
        """
        Combines textual features (genres + overview), fits the TF-IDF Vectorizer,
        and computes the Cosine Similarity matrix.
        """
        # Create a combined features column
        # Adding weight to genres by repeating it helps improve content recommendation relevancy
        combined_features = self.df['genres'] + " " + self.df['genres'] + " " + self.df['overview']
        
        # Initialize TF-IDF Vectorizer and remove common English stop words
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(combined_features)
        
        # Compute the cosine similarity matrix
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
        
        # Create a mapping of movie titles (lowercase, stripped) to their DataFrame index
        self.indices = pd.Series(self.df.index, index=self.df['title'].str.strip().str.lower()).drop_duplicates()

    def get_all_titles(self):
        """
        Returns a list of all movie titles in the dataset.
        Useful for building search autocomplete.
        """
        if self.df is None:
            return []
        return self.df['title'].tolist()

    def get_recommendations(self, title, top_n=10):
        """
        Given a movie title, finds the top_n most similar movies based on content.
        Returns a list of dictionaries with recommended movie details and similarity scores,
        or None if the movie is not found.
        """
        # Clean the input title for reliable lookup
        cleaned_title = str(title).strip().lower()
        
        if cleaned_title not in self.indices:
            return None
        
        # Get the index of the movie that matches the title
        idx = self.indices[cleaned_title]
        
        # If there are multiple matches (duplicate titles in indices Series), select the first index
        if isinstance(idx, pd.Series):
            idx = idx.iloc[0]
            
        # Get the pairwise similarity scores of all movies with this movie
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        
        # Sort the movies based on similarity scores in descending order
        # Each item in sim_scores is (index, score)
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Filter out the input movie itself from the recommendations list
        # and limit to top_n recommendations
        recommendations = []
        for index, score in sim_scores:
            if index == idx:
                continue
            
            # Extract movie details
            movie_row = self.df.iloc[index]
            
            # Format release year from release date (YYYY-MM-DD)
            release_year = ""
            if movie_row['release_date']:
                release_year = movie_row['release_date'].split('-')[0]
                
            similarity_percentage = round(float(score) * 100, 1)
            
            recommendations.append({
                "title": movie_row['title'],
                "genres": movie_row['genres'],
                "overview": movie_row['overview'],
                "vote_average": movie_row['vote_average'],
                "release_year": release_year,
                "poster_url": movie_row['poster_url'],
                "similarity_score": similarity_percentage
            })
            
            if len(recommendations) == top_n:
                break
                
        return recommendations
