from network_components import *
from network import *
from generate_content import *
import pandas as pd
from max_heap import MaxHeap
from inverted_index import InvertedIndex
from attribute_filter import AttributeFilter
from post import Post
from user import User

john = User("john", 24, Gender.MALE, Region.NORTH, [], [], [], [])
alice = User("alice", 26, Gender.FEMALE, Region.EAST, [], [], [], [])
bob = User("bob", 24, Gender.MALE, Region.SOUTH, [], [], [], [])
peter = User("peter", 36, Gender.MALE, Region.NORTH, [], [], [], [])
sarah = User("sarah", 45, Gender.FEMALE, Region.WEST, [], [], [], [])

# connections
john.add_connection(Connection(john, alice, ConnectionType.FRIEND))
john.add_connection(Connection(john, bob, ConnectionType.COWORKER))
john.add_connection(Connection(john, peter, ConnectionType.FOLLOWER))
john.add_connection(Connection(john, sarah, ConnectionType.HAS_READ_POSTS_BY))

alice.add_connection(Connection(alice, john, ConnectionType.FRIEND))
alice.add_connection(Connection(alice, peter, ConnectionType.COWORKER))
alice.add_connection(Connection(alice, sarah, ConnectionType.FRIEND))

bob.add_connection(Connection(bob, john, ConnectionType.COWORKER))
bob.add_connection(Connection(bob, sarah, ConnectionType.FRIEND))

peter.add_connection(Connection(peter, alice, ConnectionType.COWORKER))
peter.add_connection(Connection(peter, sarah, ConnectionType.HAS_READ_POSTS_BY))

sarah.add_connection(Connection(sarah, john, ConnectionType.HAS_READ_POSTS_BY))
sarah.add_connection(Connection(sarah, alice, ConnectionType.FRIEND))
sarah.add_connection(Connection(sarah, bob, ConnectionType.FRIEND))

network = Network([john, alice, bob, peter, sarah])

# make comments
make_comments(john, alice, bob, peter, sarah)

# make posts
make_posts(john, alice, bob, peter, sarah)

comments = {  # length
    "john": john.get_comments(),  # 3
    "alice": alice.get_comments(),  # 0
    "bob": bob.get_comments(),  # 2
    "peter": peter.get_comments(),  # 1
    "sarah": sarah.get_comments()  # 2
}
posts = {  # length
    "john": john.get_published_posts(),  # 1
    "alice": alice.get_published_posts(),  # 3
    "bob": bob.get_published_posts(),  # 0
    "peter": peter.get_published_posts(),  # 2
    "sarah": sarah.get_published_posts()  # 1
}

# add views to posts
posts["john"][0].add_viewer(generate_view(alice, posts["john"][0]))
posts["john"][0].add_viewer(generate_view(bob, posts["john"][0]))
posts["john"][0].add_viewer(generate_view(sarah, posts["john"][0]))

posts["alice"][0].add_viewer(generate_view(john, posts["alice"][0]))

posts["alice"][1].add_viewer(generate_view(peter, posts["alice"][1]))
posts["alice"][1].add_viewer(generate_view(sarah, posts["alice"][1]))

posts["peter"][0].add_viewer(generate_view(john, posts["peter"][0]))
posts["peter"][0].add_viewer(generate_view(alice, posts["peter"][0]))
posts["peter"][0].add_viewer(generate_view(sarah, posts["peter"][0]))

posts["peter"][1].add_viewer(generate_view(sarah, posts["peter"][1]))

posts["sarah"][0].add_viewer(generate_view(john, posts["sarah"][0]))
posts["sarah"][0].add_viewer(generate_view(alice, posts["sarah"][0]))
posts["sarah"][0].add_viewer(generate_view(bob, posts["sarah"][0]))
posts["sarah"][0].add_viewer(generate_view(peter, posts["sarah"][0]))

for user in posts.items():
    for post in user[1]:
        for viewer in post.get_viewers():
            viewer.get_who_viewed().add_viewed_post(post)

# add comments to posts
posts["alice"][0].add_comment(comments["john"][0])
posts["peter"][0].add_comment(comments["john"][1])
posts["sarah"][0].add_comment(comments["john"][2])

posts["john"][0].add_comment(comments["bob"][0])
posts["sarah"][0].add_comment(comments["bob"][1])

posts["alice"][1].add_comment(comments["peter"][0])

posts["john"][0].add_comment(comments["sarah"][0])
posts["alice"][1].add_comment(comments["sarah"][1])

# network.print_users()

# print(network.users[0].all_posts)
network.create_wordcloud(["hello", "lamb"])
