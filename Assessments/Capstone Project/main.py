# Create a movie review fetcher application using selenium and integrate with streamlit with various options


import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_movie_rating_from_imdb(movie):
    """Function to get movie rating from IMDb page."""
    driver.get(f"https://www.imdb.com/find/?q={movie}&ref_=nv_sr_sm")
    driver.implicitly_wait(10)

    link = driver.find_element(By.CLASS_NAME, "ipc-metadata-list-summary-item__t")
    driver.get(link.get_attribute("href"))

    # Get movie rating
    driver.implicitly_wait(5)
    rating = driver.find_element(By.XPATH,
                                 """/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/
                                 div[2]/div[2]/div/div[1]/a/span/div/div[2]/div[1]/span[1]""")
    return rating.text


def get_movie_rating_from_rotten_tomatoes(movie):
    """Function to get movie rating from rotten tomatoes page."""
    driver.get(f"https://www.rottentomatoes.com/search?search={movie}")
    driver.implicitly_wait(10)

    # Get movie rating
    driver.implicitly_wait(5)
    rating = driver.find_element(By.XPATH, """//*[@id="search-results"]/search-page-result[1]/ul/
    search-page-media-row[1]""")
    return rating.text


def get_movie_rating_from_letterboxd(movie):
    """Function to get movie rating from letterboxd page."""
    driver.get(f"https://letterboxd.com/search/{movie}/")
    driver.implicitly_wait(10)

    link = driver.find_element(By.XPATH, """//*[@id="search-table-body"]/ul/li[1]/div[2]/h2/span/a""")
    driver.get(link.get_attribute("href"))

    # Get movie rating
    driver.implicitly_wait(5)
    rating = driver.find_element(By.XPATH,
                                 """//*[@id="film-page-wrapper"]/div[2]/aside/section[2]/span/a""")

    return rating.text


def get_movie_rating_from_metacritic(movie):
    """Function to get movie rating from metacritic page."""
    driver.get(f"https://www.metacritic.com/search/{movie}")
    driver.implicitly_wait(10)

    # Get movie rating
    driver.implicitly_wait(5)
    rating = driver.find_element(By.XPATH,
                                 """//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/a/div[3]/div/div/span""")
    return rating.text


selected_website = st.selectbox("Select a website", ["IMDb", "Rotten tomatoes", "Letterboxd", "Metacritic"])
user_input_movie_name = st.text_input("Movie", placeholder="Enter movie name")

if st.button("Get review", type="primary"):
    if selected_website == "IMDb":
        try:
            driver = webdriver.Firefox()

            try:
                movie_rating = get_movie_rating_from_imdb(user_input_movie_name)

                st.text(f"Movie rating: {movie_rating}")
            except Exception as _:
                st.text(f"Movie rating for {user_input_movie_name} not found.")

            time.sleep(5)
            driver.quit()
        except Exception as _:
            st.text(f"API rate limit exceeded.")

    elif selected_website == "Rotten tomatoes":
        try:
            driver = webdriver.Firefox()

            try:
                movie_rating = get_movie_rating_from_rotten_tomatoes(user_input_movie_name)

                st.text(f"Movie rating: {movie_rating}")
            except Exception as _:
                st.text(f"Movie rating for {user_input_movie_name} not found.")

            time.sleep(5)
            driver.quit()
        except Exception as _:
            st.text(f"API rate limit exceeded.")

    elif selected_website == "Letterboxd":
        try:
            driver = webdriver.Firefox()

            try:
                movie_rating = get_movie_rating_from_letterboxd(user_input_movie_name)

                st.text(f"Movie rating: {movie_rating}")
            except Exception as _:
                st.text(f"Movie rating for {user_input_movie_name} not found.")

            time.sleep(5)
            driver.quit()
        except Exception as _:
            st.text(f"API rate limit exceeded.")

    elif selected_website == "Metacritic":
        try:
            driver = webdriver.Firefox()

            try:
                movie_rating = get_movie_rating_from_metacritic(user_input_movie_name)

                st.text(f"Movie rating: {movie_rating}")
            except Exception as _:
                st.text(f"Movie rating for {user_input_movie_name} not found.")

            time.sleep(5)
            driver.quit()
        except Exception as _:
            st.text(f"API rate limit exceeded.")
