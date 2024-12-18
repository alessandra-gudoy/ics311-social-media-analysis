from enum import Enum
import pandas as pd

from attribute_filter import AttributeFilter
from inverted_index import InvertedIndex
from max_heap import MaxHeap

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

class Region(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"

class ConnectionType(Enum):
    FOLLOWER = "follower"
    FRIEND = "friend"
    COWORKER = "coworker"
    BLOCKED = "blocked"
    HAS_READ_POSTS_BY = "has_read_posts_by"


class Connection:
    def __init__(self, user, to_who, connection_type):
        self.user = user
        self.to_who = to_who
        self.connection_type = connection_type

    def get_user(self):
        return self.user.get_username()

    def get_to_who(self):
        return self.to_who.get_username()

    def get_connection_type(self):
        return self.connection_type


class View:
    def __init__(self, who_viewed, time_viewed, date_viewed, post_viewed):
        self.who_viewed = who_viewed
        self.time_viewed = time_viewed
        self.date_viewed = date_viewed
        self.post_viewed = post_viewed

    def get_who_viewed(self):
        return self.who_viewed

    def get_time(self):
        return self.time_viewed

    def get_date(self):
        return self.date_viewed

    def get_post_viewed(self):
        return self.post_viewed.get_summary()

    def get_summary(self):
        return f"{self.who_viewed.get_username()} viewed at {self.time_viewed} on {self.date_viewed}"


class Comment:
    def __init__(self, user, content, time_created, date_created):
        self.user = user
        self.author = user.get_username()
        self.content = content
        self.time_created = time_created
        self.date_created = date_created

    def get_author(self):
        return self.author

    def get_content(self):
        return self.content

    def get_time(self):
        return self.time_created

    def get_date(self):
        return self.date_created

    def get_summary(self):
        return f"{self.author} said: \"{self.content}\" at {self.time_created} on {self.date_created}"


class Post:
    def __init__(self, user, content, time_created, date_created, comments, viewers, engagement_score = 0):
        self.user = user
        self.author = user.get_username()
        self.content = content
        self.time_created = time_created
        self.date_created = date_created
        self.comments = comments
        self.viewers = viewers
        self.engagement_score = engagement_score

    def __lt__(self, other):
        return self.engagement_score < other.engagement_score

    def get_author(self):
        return self.author

    def get_content(self):
        return self.content

    def get_time(self):
        return self.time_created

    def get_date(self):
        return self.date_created

    def get_comments(self):
        return self.comments

    def get_viewers(self):
        return self.viewers

    def get_engagement_score(self):
        return self.engagement_score

    def get_summary(self):
        return f"{self.author} posted \"{self.content}\" at {self.time_created} on {self.date_created}"

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_viewer(self, viewer):
        self.viewers.append(viewer)

    def add_engagement(self, likes, shares, comments):
        self.engagement_score = likes + shares + comments

    def print_comments(self):
        comments = []
        for comment in self.comments:
            comments.append(comment.get_summary())
        print(comments)

    def print_viewers(self):
        viewers = []
        for viewer in self.viewers:
            viewers.append(viewer.get_who_viewed())
        print(viewers)


class User:
    all_posts = pd.DataFrame(columns=["age", "gender", "region", "content"])

    def __init__(self, username, age, gender, region, published_posts, viewed_posts, comments, connections):
        self.username = username
        self.age = age
        self.gender = gender
        self.region = region
        self.published_posts = published_posts
        self.viewed_posts = viewed_posts
        self.comments = comments
        self.connections = connections
        self.online = False
        self.trending_queue = MaxHeap()
        self.inverted_index = InvertedIndex()
        self.attribute_filter = AttributeFilter()

    def set_online(self):
        self.online = True

    def get_username(self):
        return self.username

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_region(self):
        return self.region

    def get_published_posts(self):
        return self.published_posts

    def get_viewed_posts(self):
        return self.viewed_posts

    def get_comments(self):
        return self.comments

    def get_connections(self):
        return self.connections

    def add_published_post(self, post):
        self.published_posts.append(post)
        if self.online:
            User.add_row_to_all_posts(self, post)
        self.trending_queue.insert(post) 

    def add_engagement_to_post(self, post, likes, shares, comments):
        post.add_engagement(likes, shares, comments)
        self.trending_queue.insert(post)

    def add_viewed_post(self, post):
        self.viewed_posts.append(post)

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_connection(self, connection):
        self.connections.append(connection)

    def add_row_to_all_posts(self, post):
        row = { "age":post.user.age, "gender":post.user.gender.value, "region":post.user.region.value, "content":post.content }
        User.all_posts = User.all_posts._append(row, ignore_index=True)

    def print_published_posts(self):
        published_posts = []
        for post in self.published_posts:
            published_posts.append(f"{post.get_content()} at {post.get_time()} on {post.get_date()}")
        print(published_posts)

    def print_viewed_posts(self):
        viewed_posts = []
        for post in self.viewed_posts:
            viewed_posts.append(post.get_summary())
        print(viewed_posts)

    def print_comments(self):
        comment_contents = []
        for comment in self.comments:
            comment_contents.append(f"{comment.get_content()} at {comment.get_time()} on {comment.get_date()}")
        print(comment_contents)

    def print_connections(self):
        connections = []
        for connection in self.connections:
            connections.append(
                f"{connection.get_to_who()}, {connection.get_connection_type()}"
            )
        print(connections)

    def print_trending_posts(self):
        trending_post = self.trending_queue.extract_max()
        if trending_post:
            print(f"Trending Post: {trending_post.get_summary()} by {trending_post.user.get_username()}")
        else:
            print("No trending posts available.")

    def print_keyword_filtered_posts(self, keyword):
        posts = self.inverted_index.search(keyword)
        for post in posts:
            print(post.get_summary())

    def print_filtered_posts_by_attribute(self, attribute, value):
        if attribute == "gender":
            posts = self.attribute_filter.filter_by_gender(value)
        elif attribute == "region":
            posts = self.attribute_filter.filter_by_region(value)
        elif attribute == "age":
            posts = self.attribute_filter.filter_by_age(value)

        for post in posts:
            print(post.get_summary())
