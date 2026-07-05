import streamlit as st
import pickle

from recommender import recommend

movies = pickle.load(
    open("models/movies.pkl","rb")
)

st.title("🎬 Movie Recommendation System")

movie_list = movies['title'].values

selected_movie = st.selectbox("Choose a movie", movie_list)

if st.button("Recommend" , key='recommend_btn_1'):

    recommendations = recommend(selected_movie)

    for movie in recommendations:
        st.write(movie)


movie_name = st.text_input("Enter movie name", placeholder="e.g. Avatar")

if st.button("Recommend" , key='recommend_btn_2'):

    if movie_name:
        recommendations = recommend(movie_name)

        for movie in recommendations:
            st.write(movie)
