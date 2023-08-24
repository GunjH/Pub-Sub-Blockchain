metamask_account_number = '1585e70d1e6B43B35AFD15c4811838591B172d01'

# Generate 200 lists
lists = []
for i in range(1, 201):
    username = f"user{i}"
    password = f"pass{i}"
    email = f"user{i}@example.com"
    lists.append([username, password, email, metamask_account_number])

# Print the lists
for lst in lists:
    print(lst)
