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
john_comm1 = Comment(john, random_content(), random_datetime().time(), random_datetime().date())
john_comm2 = Comment(john, random_content(), random_datetime().time(), random_datetime().date())
john_comm3 = Comment(john, random_content(), random_datetime().time(), random_datetime().date())
john.add_comment(john_comm1)
john.add_comment(john_comm2)
john.add_comment(john_comm3)

bob_comm1 = Comment(bob, random_content(), random_datetime().time(), random_datetime().date())
bob_comm2 = Comment(bob, random_content(), random_datetime().time(), random_datetime().date())
bob.add_comment(bob_comm1)
bob.add_comment(bob_comm2)

peter_comm1 = Comment(peter, random_content(), random_datetime().time(), random_datetime().date())
peter.add_comment(peter_comm1)

sarah_comm1 = Comment(sarah, random_content(), random_datetime().time(), random_datetime().date())
sarah_comm2 = Comment(sarah, random_content(), random_datetime().time(), random_datetime().date())
sarah.add_comment(sarah_comm1)
sarah.add_comment(sarah_comm2)

# make posts
john_post1 = Post(john, random_content(), random_datetime().time(), random_datetime().date())
john.add_published_post(john_post1)

alice_post1 = Post(alice, random_content(), random_datetime().time(), random_datetime().date())
alice_post2 = Post(alice, random_content(), random_datetime().time(), random_datetime().date())
alice_post3 = Post(alice, random_content(), random_datetime().time(), random_datetime().date())
alice.add_published_post(alice_post1)
alice.add_published_post(alice_post2)
alice.add_published_post(alice_post3)

peter_post1 = Post(peter, random_content(), random_datetime().time(), random_datetime().date())
peter_post2 = Post(peter, random_content(), random_datetime().time(), random_datetime().date())
peter.add_published_post(peter_post1)
peter.add_published_post(peter_post2)

sarah_post1 = Post(sarah, random_content(), random_datetime().time(), random_datetime().date())
sarah.add_published_post(sarah_post1)


network.print_users()
