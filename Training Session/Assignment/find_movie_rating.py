import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Initializing a dictionary
movies = {}


def navigate_to_movie_page(movie):
    """Function to navigate to movie page."""
    driver.get("https://www.imdb.com/")
    driver.implicitly_wait(10)

    search_box = driver.find_element(By.ID, "suggestion-search")
    search_button = driver.find_element(By.ID, "suggestion-search-button")
    search_box.send_keys(movie)
    driver.implicitly_wait(5)
    search_button.click()
    driver.implicitly_wait(5)

    link = driver.find_element(By.CLASS_NAME, "ipc-metadata-list-summary-item__t")
    driver.get(link.get_attribute("href"))


def get_movie_rating():
    """Function to get movie rating."""
    driver.implicitly_wait(5)
    rating = driver.find_element(By.XPATH,
                                        """/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/
                                        div[2]/div[2]/div/div[1]/a/span/div/div[2]/div[1]/span[1]""")
    return rating.text


def write_to_file():
    """Function to write all dictionary items to file."""
    with open("movies.txt", "w") as file:
        for key, value in movies.items():
            file.write(f"{key} : {value}\n")


while True:
    print("Menu driven pgm\n1. Get movie rating from IMDB\n2. Exit")
    user_choice = input("Select an option: ")

    if user_choice == "1":
        movie_name = input("Enter a movie name: ")

        try:
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

            try:
                navigate_to_movie_page(movie_name)
                movie_rating = get_movie_rating()

                # Add movie name and rating to dictionary
                movies[movie_name] = movie_rating
            except Exception as _:
                print(f"{movie_name} not found.")

            time.sleep(5)
            driver.quit()
        except Exception as _:
            print(f"API rate limit exceeded.")
    else:
        write_to_file()
        exit()





