from flask import Flask, render_template, request, jsonify, redirect, url_for
from recommender import MovieRecommender
import os

app = Flask(__name__)

# Initialize the recommender system
try:
    recommender = MovieRecommender('movies.csv')
except Exception as e:
    print(f"Error initializing recommender: {e}")
    recommender = None

@app.route('/')
def home():
    """
    Renders the home page with the movie search interface.
    """
    return render_template('index.html')

@app.route('/about')
def about():
    """
    Renders the about page describing the project, tech stack, and algorithms.
    """
    return render_template('about.html')

@app.route('/recommend')
def recommend():
    """
    Handles recommendation requests. Renders recommendations.html with the top 10 recommended
    movies, or redirects to home with an error message if the movie is not found.
    """
    movie_title = request.args.get('movie', '').strip()
    
    if not movie_title:
        return redirect(url_for('home'))
        
    if not recommender:
        return render_template('index.html', error="Recommendation engine is not initialized.")
        
    # Get recommendations
    recommendations = recommender.get_recommendations(movie_title)
    
    if recommendations is None:
        # If movie is not found, render home page with an error
        return render_template('index.html', error=f"Movie '{movie_title}' not found in our database. Please try another movie.")
        
    # Get selected movie details to show what we are recommending based on
    cleaned_title = movie_title.lower()
    selected_movie = None
    
    # Locate original movie details
    idx_series = recommender.indices.get(cleaned_title)
    if idx_series is not None:
        if not isinstance(idx_series, (int, float)) and hasattr(idx_series, 'iloc'):
            idx = idx_series.iloc[0]
        else:
            idx = idx_series
            
        row = recommender.df.iloc[idx]
        release_year = row['release_date'].split('-')[0] if row['release_date'] else ""
        selected_movie = {
            "title": row['title'],
            "genres": row['genres'],
            "overview": row['overview'],
            "vote_average": row['vote_average'],
            "release_year": release_year,
            "poster_url": row['poster_url']
        }
        
    return render_template('recommendations.html', 
                           movie_title=movie_title, 
                           selected_movie=selected_movie,
                           recommendations=recommendations)

@app.route('/api/suggest')
def suggest():
    """
    API endpoint for autocomplete suggestions.
    Returns a JSON list of movie titles matching the query string 'q'.
    """
    query = request.args.get('q', '').strip().lower()
    if not query or not recommender:
        return jsonify([])
        
    titles = recommender.get_all_titles()
    # Filter titles that contain the query substring, matching up to 5 suggestions
    suggestions = [t for t in titles if query in t.lower()]
    return jsonify(suggestions[:5])

if __name__ == '__main__':
    # Run the server locally on port 5000 in debug mode for easy development
    app.run(debug=True, port=5000)
