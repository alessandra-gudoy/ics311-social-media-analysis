import networkx as nx
import matplotlib.pyplot as plt

def create_graph(network):
    G = nx.DiGraph()

    for user in network.get_users():
        G.add_node(user.get_username(), label=user.get_username(), type='user')
        for post in user.get_published_posts():
            post_label = f"Post by {user.get_username()} at {post.get_time()}"
            G.add_node(post, label=post_label, type='post')
            G.add_edge(user.get_username(), post, connection='authored')
            for viewer in post.get_viewers():
                G.add_edge(viewer.get_who_viewed().get_username(), post, connection='viewed')

    return G

def draw_graph(G, important_posts):
    pos = nx.spring_layout(G, k=0.3)  # Adjust the k parameter to spread out the nodes more
    node_labels = nx.get_node_attributes(G, 'label')
    
    node_colors = []
    for node in G.nodes():
        if node in important_posts:
            node_colors.append('red')
        elif G.nodes[node]['type'] == 'user':
            node_colors.append('green')
        else:
            node_colors.append('blue')

    node_sizes = [700 if node in important_posts else 300 for node in G.nodes()]
    
    edge_colors = ['orange' if data['connection'] == 'authored' else 'purple' for _, _, data in G.edges(data=True)]
    
    nx.draw(G, pos, labels=node_labels, with_labels=True, node_color=node_colors, node_size=node_sizes, font_size=8, font_color='black', edge_color=edge_colors)
    
    edge_labels = nx.get_edge_attributes(G, 'connection')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

    handles = [plt.Line2D([0], [0], marker='o', color='w', label='User', markersize=10, markerfacecolor='green'),
               plt.Line2D([0], [0], marker='o', color='w', label='Post', markersize=10, markerfacecolor='blue'),
               plt.Line2D([0], [0], marker='o', color='w', label='Important Post', markersize=10, markerfacecolor='red'),
               plt.Line2D([0], [0], color='orange', lw=2, label='Authored'),
               plt.Line2D([0], [0], color='purple', lw=2, label='Viewed')]

    plt.legend(handles=handles, loc='best')
    plt.show()
