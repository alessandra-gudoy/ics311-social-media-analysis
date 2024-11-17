from network_components import *
from network import *
from content import *

john = User("john", [], [], [], [])
alice = User("alice", [], [], [], [])
bob = User("bob", [], [], [], [])
peter = User("peter", [], [], [], [])
sarah = User("sarah", [], [], [], [])

network = Network([john, alice, bob, peter, sarah])

# make comments
john.add_comment(Comment(john, random_content(), random_datetime().time(), random_datetime().date()))
john.add_comment(Comment(john, random_content(), random_datetime().time(), random_datetime().date()))
john.add_comment(Comment(john, random_content(), random_datetime().time(), random_datetime().date()))

alice.add_comment(Comment(alice, random_content(), random_datetime().time(), random_datetime().date()))

bob.add_comment(Comment(bob, random_content(), random_datetime().time(), random_datetime().date()))
bob.add_comment(Comment(bob, random_content(), random_datetime().time(), random_datetime().date()))

peter.add_comment(Comment(peter, random_content(), random_datetime().time(), random_datetime().date()))

sarah.add_comment(Comment(sarah, random_content(), random_datetime().time(), random_datetime().date()))
sarah.add_comment(Comment(sarah, random_content(), random_datetime().time(), random_datetime().date()))

network.print_users()
