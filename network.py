from network_components import *

import numpy as np
import pandas as pd
from os import path
from PIL import Image
# run pip install wordcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

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
    # def create_dataframe(self):
