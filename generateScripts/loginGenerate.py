# Generate 200 lists
lists = []
for i in range(1, 201):
    username = f"user{i}"
    password = f"pass{i}"
    lists.append([username, password])

# Print the lists
for lst in lists:
    print(lst)