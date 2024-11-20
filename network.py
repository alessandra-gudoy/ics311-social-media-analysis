from network_components import *

import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# may need to run in terminal
# pip install matplotlib
# pip install pandas
# pip install wordcloud


class Network:
    def __init__(self, users):
        self.users = users
        for user in users:
            user.set_online()
            for post in user.get_published_posts():
                User.add_row_to_all_posts(post)

    def get_users(self):
        return self.users

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
            user.set_online()
            for post in user.get_published_posts():
                User.add_row_to_all_posts(post)

    def get_user_info(self, user):
        if user in self.users:
            return (f"{user.get_username()} has {len(user.get_published_posts())} posts, {len(user.get_comments())} comments, viewed {len(user.get_viewed_posts())} posts, and has {len(user.get_connections())} connections.")

    def print_users(self):
        for user in self.users:
            print(self.get_user_info(user))

    # Credit: Word Cloud Implementation adapted from https://www.geeksforgeeks.org/generating-word-cloud-python/
    """
        keywords = list of words that should be in content of post

    """
    def create_wordcloud(self, keywords=[], gender=None, age=None, region=None):
        filtered_data = User.all_posts.copy()

        if age != None:
            filtered_data =  filtered_data[(filtered_data['age'] == age)]

        if gender != None:
            filtered_data =  filtered_data[(filtered_data['gender'] == gender)]

        if region != None:
            filtered_data =  filtered_data[(filtered_data['region'] == region)]

        if keywords != []:
            filtered_data = filtered_data[filtered_data['content'].str.contains('|'.join(keywords))]

        text = " ".join(filtered_data['content'])
        stopwords = set(STOPWORDS)
        wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

