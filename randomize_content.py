from network_components import *

import datetime
import random

content = [
    "Peter Piper picked a peck of pickled peppers.",
    "She sells seashells by the seashore.",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
    "I scream, you scream, we all scream for ice cream.",
    "Twinkle, twinkle, little star, how I wonder what you are.",
    "Mary had a little lamb, its fleece was white as snow.",
    "Itsy bitsy spider climbed up the water spout.",
    "Jack and Jill went up the hill to fetch a pail of water.",
    "Humpty Dumpty sat on a wall, Humpty Dumpty had a great fall.",
    "Baa, baa, black sheep, have you any wool?",
]


def random_date():
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 11, 17)
    num_days = (end_date - start_date).days

    random_date = start_date + datetime.timedelta(random.randint(0, num_days))

    return random_date


def random_time():
    hours = random.randint(0, 23)
    min_sec = random.randint(0, 59)

    random_time = datetime.time(hours, min_sec)

    return random_time


def random_content():
    return random.choice(content)


def generate_comment(user):
    return Comment(user, random_content(), random_time(), random_date())


def generate_post(user):
    return Post(user, random_content(), random_time(), random_date(), [], [])


def generate_view(user, post):
    return View(user, random_time(), random_date(), post)
