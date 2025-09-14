import pandas as pd
import numpy as np

def clean_data(path):
    """
    load_data loads the csv file and cleans it up for use

    :param path: the path of the csv file
    :return: returns the dataframe
    """
    df = pd.read_csv(path)

    #Fix unknown movies
    df['title'] = df['title'].replace('unknown', np.nan)

    # Fix missing years
    years = df['title'].str.extract(r'\((\d{4})\)', expand=False)
    years_numeric = pd.to_numeric(years, errors='coerce')
    df['year'] = df['year'].fillna(years_numeric)
    return df
