from network_components import *
from network import *
from content import *

john = User("john", [], [], [], [])
alice = User("alice", [], [], [], [])
bob = User("bob", [], [], [], [])
peter = User("peter", [], [], [], [])
sarah = User("sarah", [], [], [], [])

network = Network([john, alice, bob, peter, sarah])

network.print_users()
