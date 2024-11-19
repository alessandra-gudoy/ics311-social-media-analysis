import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, post):
        heapq.heappush(self.heap, (-post.engagement_score, post))

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None

    def peek(self):
        if self.heap:
            return self.heap[0][1]
        return None

    def size(self):
        return len(self.heap)

    def print_heap(self):
        sorted_posts = sorted(self.heap, key=lambda x: -x[0])
        for score, post in sorted_posts:
            print(post)