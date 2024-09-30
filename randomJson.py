import json
import random
import string

def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

data = {}
for i in range(10):
    name = random_string(10)
    data[name] = {
        "id": random.randint(1, 1000),
        "name": name,
        "random_value": random.random()
    }

with open('random_data.json', 'w') as f:
    json.dump(data, f)
