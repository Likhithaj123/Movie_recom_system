import pandas as pd
import pickle

# Load your CSVs
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

# Merge both datasets on title
movies = movies.merge(credits, on='title')

# Create a movie dictionary with titles and ids
movie_dict = {
    'title': movies['title'].tolist(),
    'movie_id': movies['id'].tolist()
}

# Save as pickle
with open('movie_dict.pkl', 'wb') as f:
    pickle.dump(movie_dict, f)

print("✅ movie_dict.pkl file saved successfully!")
