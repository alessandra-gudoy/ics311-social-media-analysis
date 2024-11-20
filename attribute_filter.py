class AttributeFilter:
    def __init__(self):
        self.posts = []  # Initialize an empty list of posts

    def filter_by_gender(self, gender):
        filtered_posts = []
        for post in self.posts:
            if post.user.get_gender() == gender:  # Assuming post has a 'user' attribute with 'get_gender()' method
                filtered_posts.append(post)
        return filtered_posts

    def filter_by_region(self, region):
        filtered_posts = []
        for post in self.posts:
            if post.user.get_region() == region:
                filtered_posts.append(post)
        return filtered_posts

    def filter_by_age(self, age):
        filtered_posts = []
        for post in self.posts:
            if post.user.get_age() == age:
                filtered_posts.append(post)
        return filtered_posts
