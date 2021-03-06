import requests
from bs4 import BeautifulSoup
import pickle

DESIRED_HUBS = []

ret = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(ret.text, 'html.parser')
posts = soup.find_all('article', class_='post')
POSTS = []


def view_posts():
    for post in posts:
        hubs = post.find_all('a', class_='hub-link')
        for hub in hubs:
            hub_lower = hub.text.lower()
            if any([hub_lower in desired for desired in DESIRED_HUBS]):
                title_element = post.find('a', class_='post__title_link')
                post_preview = title_element.text + " " + title_element.attrs.get('href')
                POSTS.append(post_preview)
    return POSTS


def clear_posts():
    POSTS.clear()


def view_hubs():
    try:
        with open('data.pickle', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return "Error!"


def add_hubs(message):
    with open('data.pickle', 'rb') as f:
        DESIRED_HUBS = pickle.load(f)
    DESIRED_HUBS.append(message.lower())
    with open('data.pickle', 'wb') as f:
        pickle.dump(DESIRED_HUBS, f)


def delete_hub(message):
        with open('data.pickle', 'rb') as f:
            DESIRED_HUBS = pickle.load(f)
        DESIRED_HUBS.remove(message.lower())
        with open('data.pickle', 'wb') as f:
            pickle.dump(DESIRED_HUBS, f)

