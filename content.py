import datetime
import random

content = [
    'Peter Piper picked a peck of pickled peppers.',
    'She sells seashells by the seashore.',
    'How much wood would a woodchuck chuck if a woodchuck could chuck wood?',
    'I scream, you scream, we all scream for ice cream.',
    'Twinkle, twinkle, little star, how I wonder what you are.',
    'Mary had a little lamb, its fleece was white as snow.',
    'Itsy bitsy spider climbed up the water spout.',
    'Jack and Jill went up the hill to fetch a pail of water.',
    'Humpty Dumpty sat on a wall, Humpty Dumpty had a great fall.',
    'Baa, baa, black sheep, have you any wool?'
]


def random_datetime():
    start_date = datetime.datetime(2024, 1, 1)
    end_date = datetime.datetime(2024, 11, 17)
    num_days = (end_date - start_date).days
    
    random_date = start_date + datetime.timedelta(random.randint(0, num_days))
    
    hours = random.randint(0, 24)
    min_sec = random.randint(0, 60)
    
    random_time = datetime.time(hours, min_sec)
    return datetime.datetime.combine(random_date, random_time)