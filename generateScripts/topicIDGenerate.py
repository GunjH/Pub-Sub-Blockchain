import random
import string

# Define a list of 200 unique topic names
topic_names = set()

# Generate unique topic names until we have 200
while len(topic_names) < 200:
    topic_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    topic_names.add(topic_name)

# Convert the set of unique topic names to a list and shuffle it
topic_names = list(topic_names)
random.shuffle(topic_names)

# Generate 200 lists
lists = []
for i in range(1, 201):
    topic_id = i
    topic_name = topic_names[i-1]
    lists.append([topic_id, topic_name])

# Print the lists
for lst in lists:
    print(lst)
