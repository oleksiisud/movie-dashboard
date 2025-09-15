# Movie Ratings Analysis Dashboard

This is an interactive web application built with Streamlit for visualizing and analyzing movie ratings data. The dashboard provides insights into movie trends, genre popularity, and top-rated films based on a dataset of ratings made between 1997 and 1998.

## Features

- **Interactive UI**: A clean and user-friendly interface built with Streamlit.
- **Genre Analysis**:
    - **Genre Popularity**: A bar chart displaying the total number of ratings for each movie genre.
    - **Best Genres by Rating**: A sorted bar chart showing the average rating for each genre.
- **Ratings Analysis**:
    - **Ratings Over Years**: A line chart illustrating the trend of average movie ratings by their release year.
    - **Best Movies by Ratings**: A dynamic chart showing the top-rated movies. Users can interact with a slider to set the minimum number of ratings required for a movie to be included.
- **Data Exploration**: A section to view the complete, cleaned DataFrame used for the analysis.

![Screenshot of the Movie Ratings Dashboard](https://imgur.com/PvVZVaF.png)

*(Image is a representative example of a Streamlit dashboard)*

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.8+
-   `pip` package manager

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/oleksiisud/movie-dashboard.git
    cd movie-dashboard
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    A `requirements.txt` file should be created with the following content:
    ```txt
    streamlit
    pandas
    numpy
    seaborn
    matplotlib
    altair
    ```
    Then, install the packages using pip:
    ```sh
    pip install -r requirements.txt
    ```

4.  **Data Setup:**
    Ensure you have the `movie_ratings.csv` file inside a `data/` directory in the project's root folder.

    ```
    .
    ├── .streamlit/
    │   └── config.toml
    ├── static/
    │   ├── Inter-Italic-VariableFont_opsz_wght.ttf
    │   └── Inter-VariableFont_opsz_wght.ttf
    ├── data/
    │   └── movie_ratings.csv
    ├── movie_dashboard.py
    ├── process_data.py
    ├── README.md
    ├── requirements.txt
    └── visualizations.py
    ```

### Usage

To run the Streamlit application, execute the following command in your terminal from the project's root directory:

```sh
streamlit run movie_dashboard.py