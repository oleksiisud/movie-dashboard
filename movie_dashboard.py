import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib as plt
from process_data import clean_data
import visualizations as vis

st.set_page_config(
    page_title='Movie Ratings Dashboard',
    page_icon='🎥',
    layout='wide',
    initial_sidebar_state='collapsed',
)

@st.cache_data
def load_data():
    load_df = clean_data('data/movie_ratings.csv')
    return load_df

df = load_data()

st.title('Movie Ratings Dashboard')
st.markdown('A dashboard to explore movie ratings and trends between 1997 and 1998.')

with st.sidebar:
    st.header('Table of Contents')
    st.markdown('<a class="st-emotion-cache-nudlla eyqil1z2" href="#genres">Genres</a>', unsafe_allow_html=True)
    st.markdown('<a class="st-emotion-cache-nudlla eyqil1z2" href="#ratings">Ratings</a>', unsafe_allow_html=True)
    st.markdown('<a class="st-emotion-cache-nudlla eyqil1z2" href="#data">Data</a>', unsafe_allow_html=True)
    st.link_button('Data Source', url='https://grouplens.org/datasets/movielens/', width='stretch')

st.header('Genres', anchor='genres')
col1, col2 = st.columns(2)
with col1:
    st.subheader('Genre Popularity')
    st.markdown('Count of ratings per genre.')
    vis.genre_counts(df)
with col2:
    st.subheader('Best Genre by Rating')
    st.markdown('Which genres have the highest average ratings?')
    vis.best_genres(df)

st.divider()

st.header('Ratings', anchor='ratings')
col3, col4 = st.columns(2)
with col3:
    st.subheader('Ratings Over Years')
    st.markdown('Progression of ratings throughout the release years.')
    vis.ratings_over_years(df)
with col4:
    st.subheader('Best Movies by Ratings')
    st.markdown('Which genres have the highest average ratings based on minimum amount of ratings?')
    min_ratings = st.slider("Minimum number of ratings", 10, 1000, 50, step=10)
    vis.best_movies(df, min_ratings)

st.divider()

st.header('Dataframe', anchor='data')
st.dataframe(df)