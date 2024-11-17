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


network.print_users()
