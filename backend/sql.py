# import sqlite3


# conn = sqlite3.connect('bags.db')
# cur = conn.cursor()


# sql ="""
# CREATE TABLE bags (
#                     id INTEGER PRIMARY KEY,
#                     name TEXT NOT NULL,
#                     color TEXT NOT NULL,
#                     color_code TEXT NOT NULL,
#                     image_filename TEXT
#                 )"""


# cur.execute(sql)
# print("Taable has been created")
# conn.commit()


# conn.close()
# import sqlite3
# from faker import Faker
# import random
# import uuid

# conn = sqlite3.connect('bags.db')
# cur = conn.cursor()


# cur.execute('''CREATE TABLE IF NOT EXISTS bags (
#                     id INTEGER PRIMARY KEY,
#                     name TEXT NOT NULL,
#                     color TEXT NOT NULL,
#                     color_code TEXT NOT NULL,
#                     image_filename TEXT
#                 )''')


# fake = Faker()


# def generate_random_bag():
#     name = fake.word() + " Bag"
#     image_url = fake.image_url()
#     color = fake.color_name()
#     color_code = str(uuid.uuid4())  
#     return name, image_url, color, color_code


# for _ in range(10):  
#     name, image_url, color, color_code = generate_random_bag()
#     cur.execute("INSERT INTO bags (name, color, color_code, image_filename) VALUES (?, ?, ?, ?)",
#                 (name, color, color_code, image_url))

# conn.commit()
# conn.close()

# print("Random bags data has been generated and inserted into the database.")


import sqlite3
from faker import Faker
import random
import uuid

conn = sqlite3.connect('bags.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS bags (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    color TEXT NOT NULL,
                    color_code TEXT NOT NULL,
                    image_filename TEXT
                )''')

fake = Faker()

def generate_random_bag(name, image_url, colors):
    bag_data = []
    for color in colors:
        color_code = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{name}_{color}"))
        bag_data.append((name, color, color_code, image_url))
    return bag_data

bags = [
    {"name": "First", "image_url": "https://media.bergdorfgoodman.com/f_auto,q_auto:good,ar_5:7,c_fill,dpr_1.0,w_720/01/bg_3078984_100491_m", "colors": ["White", "Beige", "Black"]},
    {"name": "Second", "image_url": "https://katespade.scene7.com/is/image/KateSpade/KG016_001?$desktopProduct$", "colors": ["Blue", "Pink", "White"]},
    {"name": "Third", "image_url": "https://images.dsw.com/is/image/DSWShoes/562619_001_ss_01?impolicy=qlt-medium-high&imwidth=640&imdensity=2", "colors": ["Brown", "Black"]}
]

bag_entries = []
for bag in bags:
    bag_entries.extend(generate_random_bag(bag["name"], bag["image_url"], bag["colors"]))

cur.executemany("INSERT INTO bags (name, color, color_code, image_filename) VALUES (?, ?, ?, ?)", bag_entries)

conn.commit()
conn.close()

print("Bags data has been generated and inserted into the database.")

