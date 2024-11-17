from network_components import *

class Network:
    def __init__(self, users):
        self.users = users
    
    def get_users(self):
        return self.users
    
    def add_user(self, user):
        self.users.append(user)
    
    def get_user_info(self, user):
        if user in self.users:
            return (f"{user.get_username()} has {len(user.get_published_posts())} posts, {len(user.get_comments())} comments, viewed {len(user.get_viewed_posts())} posts, and has {len(user.get_connections())} connections.")
    
    def print_users(self):
        for user in self.users:
            print(self.get_user_info(user))