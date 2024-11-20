import random

names = ["name1", "name2", "name3"]
print(names[random.randint(0, len(names) - 1)])
    # or
print(random.choice(names))