import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, post):
        heapq.heappush(self.heap, (-post.engagement_score, post))

    def extract_max(self):
        return heapq.heappop(self.heap)[1] if self.heap else None

    def get_max(self):
        return self.heap[0][1] if self.heap else None

    def size(self):
        return len(self.heap)

    def print_heap(self):
        sorted_posts = sorted(self.heap, key=lambda x: -x[0])
        sorted_posts = sorted(self.heap, key=lambda x: x[0])  # x[0] is -engagement_score
        for score, post in sorted_posts:
            print(f"Engagement Score: {-score}, Post: {post}")

    def is_empty(self):
        return len(self.heap) == 0