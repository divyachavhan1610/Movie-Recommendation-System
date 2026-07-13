import streamlit as st
import pickle
import requests
from config import API_KEY

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.markdown(
    """
    <h1 style='text-align:center;color:#E50914;'>
    🎬 Movie Recommendation System
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='text-align:center;color:gray;'>
    Find your next favorite movie using Artificial Intelligence
    </h4>
    """,
    unsafe_allow_html=True
)

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "🔍 Search Movie",
    movie_list,
    placeholder="Search your favorite movie..."
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

local_css("style.css")

def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    response = requests.get(url)
    data = response.json()

    poster = "https://image.tmdb.org/t/p/w500" + data['poster_path']
    rating = data['vote_average']
    release_date = data['release_date']
    overview = data['overview']
    genres = ", ".join([genre['name'] for genre in data['genres']])

    video_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}&language=en-US"

    video_response = requests.get(video_url)
    video_data = video_response.json()

    trailer = ""

    if video_data['results']:
        trailer = "https://www.youtube.com/watch?v=" + video_data['results'][0]['key']

    return poster, rating, release_date, overview, genres, trailer

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []
    recommended_ratings = []
    recommended_dates = []
    recommended_overviews = []
    recommended_genres = []
    recommended_trailers = []

    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id

        poster, rating, release_date, overview, genres, trailer = fetch_movie_details(movie_id)

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(poster)
        recommended_ratings.append(rating)
        recommended_dates.append(release_date)
        recommended_overviews.append(overview)
        recommended_genres.append(genres)
        recommended_trailers.append(trailer)

    return (
        recommended_movies,
        recommended_posters,
        recommended_ratings,
        recommended_dates,
        recommended_overviews,
        recommended_genres,
        recommended_trailers
    )

if st.button("🎥 Recommend Movies", use_container_width=True):

    names, posters, ratings, dates, overviews, genres, trailers = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.subheader(names[i])
            st.write(f"⭐ {ratings[i]}")
            st.write(f"📅 {dates[i]}")
            st.write(f"🎭 {genres[i]}")
            st.write(overviews[i][:120]+"...")
            st.link_button("▶ Watch Trailer", trailers[i])