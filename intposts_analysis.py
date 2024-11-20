from queue import PriorityQueue

def bfs(G, start_node):
    visited = set()
    queue = [start_node]
    order = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(set(G[node]) - visited)
    
    return order

def find_important_posts(G, importance_criteria='comments'):
    pq = PriorityQueue()

    for node, data in G.nodes(data=True):
        if data['type'] == 'post':
            if importance_criteria == 'comments':
                priority = len(node.get_comments())
            elif importance_criteria == 'views':
                priority = len(node.get_viewers())
            else:
                priority = len(node.get_comments()) + len(node.get_viewers())
            pq.put((-priority, node.get_time(), node))  # The priority queue uses negative priority for max-heap behavior

    important_posts = []
    while not pq.empty():
        _, _, post = pq.get()
        important_posts.append(post)
    
    return important_posts
