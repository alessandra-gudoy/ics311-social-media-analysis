class AttributesFilter:
    def __init__(self):
        self.user_posts = {}

    def add_post(self, post, user):
        key = (user.age, user.gender, user.region)
        if key not in self.user_posts:
            self.user_posts[key] = []
        self.user_posts[key].append(post)

    def get_posts_by_attributes(self, age=None, gender=None, region=None):
        filtered_posts = []
        for key, posts in self.user_posts.items():
            if (age is None or key[0] == age) and (gender is None or key[1] == gender) and (region is None or key[2] == region):
                filtered_posts.extend(posts)
        return filtered_posts