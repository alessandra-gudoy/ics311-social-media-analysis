from network_components import *
from network import *
from generate_content import *

john = User("john", [], [], [], [])
alice = User("alice", [], [], [], [])
bob = User("bob", [], [], [], [])
peter = User("peter", [], [], [], [])
sarah = User("sarah", [], [], [], [])

network = Network([john, alice, bob, peter, sarah])

# make comments
make_comments(john, alice, bob, peter, sarah)

# make posts
make_posts(john, alice, bob, peter, sarah)

comments = {                                # length
    "john": john.get_comments(),            # 3
    "alice": alice.get_comments(),          # 0
    "bob": bob.get_comments(),              # 2
    "peter": peter.get_comments(),          # 1
    "sarah": sarah.get_comments()           # 2
}
posts = {                                   # length
    "john": john.get_published_posts(),     # 1
    "alice": alice.get_published_posts(),   # 3
    "bob": bob.get_published_posts(),       # 0
    "peter": peter.get_published_posts(),   # 2
    "sarah": sarah.get_published_posts()    # 1
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
posts["peter"][0].add_viewer(generate_view(bob, posts["peter"][0]))

posts["peter"][1].add_viewer(generate_view(sarah, posts["peter"][1]))

posts["sarah"][0].add_viewer(generate_view(john, posts["sarah"][0]))
posts["sarah"][0].add_viewer(generate_view(alice, posts["sarah"][0]))
posts["sarah"][0].add_viewer(generate_view(bob, posts["sarah"][0]))
posts["sarah"][0].add_viewer(generate_view(peter, posts["sarah"][0]))

for user in posts.items():
    posts = user[1]
    for post in posts:
        for viewer in post.get_viewers():
            viewer.get_who_viewed().add_viewed_post(post)


network.print_users()