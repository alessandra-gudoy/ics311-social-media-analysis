from network_components import *
from network import *

john = User("john", [], [], [], [])
john.add_comment(Comment(john, "Hello world!", "12:00", "11/17/2024"))

print(john.get_comments())
