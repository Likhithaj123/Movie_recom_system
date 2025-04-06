import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load your dataset
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

movies = movies.merge(credits, on='title')

# Preprocess or combine features here...
movies['combined'] = movies['title'] + ' ' + movies['overview']  # just an example

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['combined'].fillna(''))

# Similarity matrix
similarity = cosine_similarity(vectors)

# Save similarity matrix
with open('similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)
