from randomize_content import *


def make_comments(user1, user2, user3, user4, user5):
    user1_comm1 = generate_comment(user1)
    user1_comm2 = generate_comment(user1)
    user1_comm3 = generate_comment(user1)
    user1.add_comment(user1_comm1)
    user1.add_comment(user1_comm2)
    user1.add_comment(user1_comm3)

    user3_comm1 = generate_comment(user3)
    user3_comm2 = generate_comment(user3)
    user3.add_comment(user3_comm1)
    user3.add_comment(user3_comm2)

    user4_comm1 = generate_comment(user4)
    user4.add_comment(user4_comm1)

    user5_comm1 = generate_comment(user5)
    user5_comm2 = generate_comment(user5)
    user5.add_comment(user5_comm1)
    user5.add_comment(user5_comm2)


def make_posts(user1, user2, user3, user4, user5):
    user1_post1 = generate_post(user1)
    user1.add_published_post(user1_post1)

    user2_post1 = generate_post(user2)
    user2_post2 = generate_post(user2)
    user2_post3 = generate_post(user2)
    user2.add_published_post(user2_post1)
    user2.add_published_post(user2_post2)
    user2.add_published_post(user2_post3)

    user4_post1 = generate_post(user4)
    user4_post2 = generate_post(user4)
    user4.add_published_post(user4_post1)
    user4.add_published_post(user4_post2)

    user5_post1 = generate_post(user5)
    user5.add_published_post(user5_post1)


