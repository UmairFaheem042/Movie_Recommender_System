import pandas as pd
import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def fetch_poster(movie_id):
    api_key = os.getenv('API_KEY')
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US')
    image = response.json()
    return "https://image.tmdb.org/t/p/w185" + image['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11] #=> 1:6 is top 5

    recommend_movies = []
    recommend_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))

    return recommend_movies, recommend_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox('Select Movie', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    st.write(f"Movies recommended based on ", selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0])
        st.text(names[0])
    with col2:
        st.image(posters[1])
        st.text(names[1])
    with col3:
        st.image(posters[2])
        st.text(names[2])
    with col4:
        st.image(posters[3])
        st.text(names[3])
    with col5:
        st.image(posters[4])
        st.text(names[4])
    with col1:
        st.image(posters[5])
        st.text(names[5])
    with col2:
        st.image(posters[6])
        st.text(names[6])
    with col3:
        st.image(posters[7])
        st.text(names[7])
    with col4:
        st.image(posters[8])
        st.text(names[8])
    with col5:
        st.image(posters[9])
        st.text(names[9])
