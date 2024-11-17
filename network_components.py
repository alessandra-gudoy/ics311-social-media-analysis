from enum import Enum


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
    def __init__(self, user, content, time_created, date_created, comments, viewers):
        self.user = user
        self.author = user.get_username()
        self.content = content
        self.time_created = time_created
        self.date_created = date_created
        self.comments = comments
        self.viewers = viewers

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
    
    def get_summary(self):
        return f"{self.author} posted \"{self.content}\" at {self.time_created} on {self.date_created}"
    
    def add_comment(self, comment):
        self.comments.append(comment)
    
    def add_viewer(self, viewer):
        self.viewers.append(viewer)
    
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
    def __init__(self, username, published_posts, viewed_posts, comments, connections):
        self.username = username
        self.published_posts = published_posts
        self.viewed_posts = viewed_posts
        self.comments = comments
        self.connections = connections

    def get_username(self):
        return self.username

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

    def add_viewed_post(self, post):
        self.viewed_posts.append(post)

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_connection(self, connection):
        self.connections.append(connection)
    
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
