import random
import string

# Define a list of 200 unique topic IDs
topic_ids = list(range(1, 201)) * 2

# Shuffle the topic IDs to randomize their order
random.shuffle(topic_ids)

# Generate 400 lists with unique topic IDs and random data
lists = []
for i in range(1, 401):
    topic_id = topic_ids[i-1]
    random_data = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(64))
    lists.append([topic_id, random_data])

# Group the lists by topic ID
grouped_lists = {}
for lst in lists:
    topic_id = lst[0]
    if topic_id not in grouped_lists:
        grouped_lists[topic_id] = []
    grouped_lists[topic_id].append(lst)

# Print the lists in the desired order
for i in range(1, 201):
    for j in range(2):
        lst = grouped_lists[i][j]
        print(lst)
