class InvertedIndex:
    def __init__(self):
        self.index = {}

    def add_post(self, post):
        words = set(post.content.split())
        for word in words:
            if word not in self.index:
                self.index[word] = []
            self.index[word].append(post)

    def get_posts_by_keyword(self, keyword):
        return self.index.get(keyword, [])
