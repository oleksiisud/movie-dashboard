import streamlit as st
import altair as alt


def genre_counts(df):
    """
    genre_counts creates the plot for the first question to show the breakdown of genres for the movies that were rated.

    :param df: the movie dataframe
    """
    # Prepare data for Altair
    genre_count_df = df['genres'].value_counts().reset_index()

    # Create the chart
    chart = alt.Chart(genre_count_df).mark_bar().encode(
        x=alt.X('count:Q', title='Rating Count'),
        y=alt.Y('genres:N', sort='-x', title='Genre'),
        tooltip=['genres', 'count'],
        color=alt.value('#cb785c'),
    )
    st.altair_chart(chart)

def best_genres(df):
    """
    best_genres creates the plot for the second question to show which genres have the highest viewer satisfaction (highest ratings).

    :param df: the movie dataframe
    """
    gbg = df.groupby('genres')
    best_genre = gbg['rating'].mean().reset_index()
    chart = alt.Chart(best_genre).mark_bar().encode(
        x=alt.X('rating:Q', title='Average Rating'),
        y=alt.Y('genres:N', sort='-x', title='Genre'),
        tooltip=['genres', 'rating'],
        color=alt.value('#cb785c'),
    )
    st.altair_chart(chart)

def ratings_over_years(df):
    """
    ratings_over_years creates the plot for the third question to show how mean rating changes across movie release years.

    :param df: the movie dataframe
    """
    gby = df.groupby('year')
    df_means = gby['rating'].mean().reset_index()
    chart = alt.Chart(df_means).mark_line(point=True).encode(
        x=alt.X('year:O', title='Year'),
        y=alt.Y('rating:Q', title='Average Rating', scale=alt.Scale(zero=False)),
        tooltip=['year', 'rating'],
        color=alt.value('#cb785c'),
    )
    st.altair_chart(chart)

def best_movies(df, rating_amt):
    """
    best_movies creates the plot the fourth question to show the 5 best-rated movies that have at least rating_amt ratings

    :param df: the movie dataframe
    :param rating_amt: the minimum rating amount
    """
    gbm = df.groupby('title').filter(lambda x: len(x) >= rating_amt)
    gbm = gbm.groupby(['title'])
    best_movies = gbm['rating'].mean().sort_values().reset_index().head()
    chart = alt.Chart(best_movies).mark_bar().encode(
        x=alt.X('rating:Q', title='Average Rating'),
        y=alt.Y('title:N', sort='-x', title=None),
        tooltip=['title', 'rating'],
        color=alt.value('#cb785c'),
    )
    st.altair_chart(chart)