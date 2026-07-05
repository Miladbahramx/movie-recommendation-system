import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pickle.load(open("D:/Python/GIT/movie recommendation system/models/movies.pkl", "rb"))

cv = CountVectorizer(max_features=5000, stop_words="english")

vectors = cv.fit_transform(movies["tags"]).toarray()

similarity = cosine_similarity(vectors)


def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []

    for movie in movies_list:
        recommendations.append(
            movies.iloc[movie[0]].title
        )

    return recommendations